Chào bạn Lợi, thật tuyệt vời khi thấy hệ thống của bạn đã đi đến hồi kết thúc mỹ mãn và hoạt động ổn định. Để giúp bạn lưu trữ và quản lý dự án **b6-team.site** chuyên nghiệp hơn, mình đã tổng hợp toàn bộ quá trình, các cấu hình then chốt và những bài học "xương máu" về quyền hạn hệ thống mà chúng ta đã cùng nhau vượt qua.

Dưới đây là tài liệu chi tiết cho hệ thống của bạn.

---

# 📑 Tài liệu Triển khai Hệ thống Phản hồi Email Tự động (Auto-Reply)

**Dự án:** b6-team.site  
**Ngày hoàn thiện:** 23/03/2026  
**Môi trường:** Ubuntu VPS, Postfix, Dovecot, Python 3, SQLite3.

## 1. Tổng quan kiến trúc

Hệ thống sử dụng cơ chế **Pipe** của Postfix để chuyển tiếp luồng dữ liệu email đến một kịch bản Python. Kịch bản này chịu trách nhiệm phân tích email, kiểm tra các quy tắc chống lặp (Loop Protection), kiểm tra giới hạn tần suất (Rate Limiting) và gửi lại email phản hồi thông qua máy chủ SMTP cục bộ.

---

## 2. Cấu hình tệp tin hệ thống

### 2.1. Tệp cấu hình tham số (`config.json`)

Lưu trữ các thông tin định danh và giới hạn của dịch vụ.

- **Vị trí:** `/etc/postfix/auto_reply/config.json`
- **Nội dung:**

```json
{
  "processing_time": "trong vòng 24–48 giờ làm việc",
  "faq_link": "https://faq.b6-team.site",
  "team_name": "Đội ngũ kỹ thuật B6-Team",
  "contact_info": "Hotline: 0123.456.789 | Email: support@b6-team.site",
  "limit_hours": 1,
  "limit_count": 10
}
```

### 2.2. Tệp điều hướng Mail (`/etc/aliases`)

Cấu hình để Postfix vừa lưu thư vào hộp thư người dùng, vừa kích hoạt kịch bản xử lý.

- **Nội dung:**

```text
support: \support, "|/usr/bin/python3 /etc/postfix/auto_reply/reply.py"
```

- **Lưu ý:** Dấu `\` trước `support` giúp tránh vòng lặp bí danh và đảm bảo thư được đưa vào Outlook/Dovecot. Sau khi sửa tệp này, luôn chạy lệnh `sudo newaliases`.

---

## 3. Mã nguồn xử lý chính (`reply.py`)

Kịch bản được tối ưu hóa để xử lý luồng (threading), chống thư rác và quản lý lỗi im lặng để không gây phiền hà cho người dùng.

```python
import sys
import json
import smtplib
import sqlite3
import os
import logging
from datetime import datetime, timedelta
from email import message_from_string
from email.mime.text import MIMEText
from email.utils import parseaddr

# --- CẤU HÌNH ---
WORKING_DIR = '/etc/postfix/auto_reply'
CONFIG_PATH = os.path.join(WORKING_DIR, 'config.json')

# Đảm bảo thư mục chứa cơ sở dữ liệu cấp đủ quyền ghi cho user chạy script (ví dụ: nobody hoặc postfix)
DB_PATH = '/var/lib/auto_reply/reply_history.db'
SENDER_EMAIL = 'support@b6-team.site'
LOG_PATH = '/var/lib/auto_reply/auto_reply.log'

# Cấu hình hệ thống ghi log
logging.basicConfig(filename=LOG_PATH, level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Kiểm tra sự tồn tại của file DB trước khi thực hiện logic
def check_and_init():
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        curr = conn.cursor()
        curr.execute('''CREATE TABLE IF NOT EXISTS history
                        (email TEXT, timestamp DATETIME)''')
        conn.commit()
        conn.close()

def is_rate_limited(sender_email, limit_hours, limit_count):
    # Chỉ mở kết nối 1 lần duy nhất trong suốt vòng đời script
    conn = sqlite3.connect(DB_PATH)
    curr = conn.cursor()

    try:
        time_threshold = (datetime.now() - timedelta(hours=limit_hours)).strftime('%Y-%m-%d %H:%M:%S')

        curr.execute("SELECT COUNT(*) FROM history WHERE email = ? AND timestamp > ?",
                     (sender_email, time_threshold))
        count = curr.fetchone()[0]

        if count >= limit_count:
            return True

        curr.execute("INSERT INTO history (email, timestamp) VALUES (?, ?)",
                     (sender_email, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()
        return False
    finally:
        conn.close()

def send_auto_reply():
    try:
        # 1. Đọc và phân tích Email đầu vào
        raw_email = sys.stdin.read()
        if not raw_email.strip():
            return

        msg_incoming = message_from_string(raw_email)

        # Lấy địa chỉ người gửi
        _, sender_address = parseaddr(msg_incoming.get('From', ''))
        if not sender_address:
            return

        sender_lower = sender_address.lower()

        # --- TÍNH NĂNG 1: CHỐNG LẶP VÀ CHẶN DAEMON ---
        # Bỏ qua các email tự động từ hệ thống hoặc cấu trúc thư rỗng
        if sender_lower.startswith('mailer-daemon') or sender_lower.startswith('postmaster') or sender_address == '<>':
            return

        auto_submitted = msg_incoming.get('Auto-Submitted', '').lower()
        precedence = msg_incoming.get('Precedence', '').lower()

        if auto_submitted in ['auto-replied', 'auto-generated'] or precedence in ['bulk', 'junk', 'list']:
            return # Dừng lại, không phản hồi email tự động

        # Lấy Message-ID để tạo luồng thư (threading)
        original_message_id = msg_incoming.get('Message-ID', '').strip()

        # 2. Đọc tệp cấu hình
        if not os.path.exists(CONFIG_PATH):
            logging.error("Không tìm thấy tệp cấu hình.")
            return

        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            config = json.load(f)

        # --- TÍNH NĂNG 2: CHỐNG SPAM (RATE LIMITING) ---
        # Chỉ check init khi file không tồn tại
        check_and_init()

        if is_rate_limited(sender_address, config.get('limit_hours', 24), config.get('limit_count', 3)):
            return # Đã gửi quá số lần quy định, không gửi thêm

        # 3. Chuẩn bị nội dung email phản hồi
        original_subject = msg_incoming.get('Subject', '')
        subject = original_subject if original_subject.lower().startswith('re:') else f"Re: {original_subject}"
        if not subject.strip() or subject == "Re: ":
            subject = "Re: Yêu cầu hỗ trợ"

        # --- Plain text fallback (cho mail client cũ không render HTML) ---
        body_plain = f"""Xin chào {sender_address},

        Cảm ơn bạn đã liên hệ với đội ngũ hỗ trợ của chúng tôi.
        Đội ngũ kỹ thuật đang xem xét và sẽ phản hồi trong {config.get('processing_time', '24–48 giờ')}.

        Trân trọng,
        {config.get('team_name', 'Đội ngũ hỗ trợ')}
        {config.get('contact_info', '')}"""

        # --- HTML body: đọc template rồi thay placeholder ---
        if not os.path.exists(TEMPLATE_PATH):
            logging.error("Không tìm thấy file template.html.")
            body_html = f"<p>{body_plain}</p>"  # fallback tạm
        else:
            with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
                body_html = f.read()

            body_html = body_html.replace('[Tên người dùng]',      sender_address)
            body_html = body_html.replace('[TICKET_ID]',           str(int(datetime.now().timestamp())))
            body_html = body_html.replace('[TIMESTAMP]',           datetime.now().strftime('%d/%m/%Y %H:%M'))
            body_html = body_html.replace('[VD: trong vòng 24–48 giờ làm việc]', config.get('processing_time', '24–48 giờ làm việc'))
            body_html = body_html.replace('[Link FAQ/Help Center]', config.get('faq_link', '#'))
            body_html = body_html.replace('[Team/Company Name]',   config.get('team_name', 'B6-Team'))
            body_html = body_html.replace('[Contact Information]', config.get('contact_info', ''))

        # 4. Thực hiện gửi mail qua Postfix Local
        msg_reply = MIMEMultipart('alternative')   # ← thay MIMEText bằng dòng này
        msg_reply['Subject'] = subject
        msg_reply['From']    = SENDER_EMAIL
        msg_reply['To']      = sender_address
        msg_reply['Auto-Submitted'] = 'auto-replied'

        if original_message_id:
            msg_reply['In-Reply-To'] = original_message_id
            msg_reply['References']  = original_message_id

        # Thứ tự quan trọng: plain trước, html sau
        # Mail client sẽ ưu tiên render phần cuối cùng (HTML)
        msg_reply.attach(MIMEText(body_plain, 'plain', 'utf-8'))
        msg_reply.attach(MIMEText(body_html,  'html',  'utf-8'))

        with smtplib.SMTP('localhost') as server:
            server.send_message(msg_reply)

    except Exception as e:
        # Ghi nhận lỗi nhưng không để script crash, tránh Postfix gửi thư cảnh báo lỗi về cho người dùng
        logging.error(f"Lỗi hệ thống: {str(e)}")
        sys.exit(0) # Thoát an toàn

if __name__ == "__main__":
    send_auto_reply()
```

- **Vị trí:** `/etc/postfix/auto_reply/reply.py`
- **Các thư viện chính:** `sqlite3` (lưu lịch sử), `smtplib` (gửi thư), `email` (phân tích cấu trúc thư).
- **Tính năng đặc biệt:**
  - **Loop Protection:** Chặn các mail có header `Auto-Submitted` hoặc từ `mailer-daemon`.
  - **Rate Limiting:** Sử dụng SQLite để đếm số lượng mail gửi đến trong N giờ.
  - **Email Threading:** Sử dụng `In-Reply-To` và `References` để gộp thư phản hồi vào đúng cuộc hội thoại của người dùng.

---

## 4. Quản lý quyền hạn và Lưu trữ (Cực kỳ quan trọng)

Đây là phần phức tạp nhất trong quá trình triển khai do Postfix thường thực thi script dưới quyền người dùng **`nobody`**.

### 4.1. Cấu trúc thư mục dữ liệu

Do SQLite cần quyền tạo tệp tin tạm (`-journal`) khi ghi dữ liệu, chúng ta đã chuyển các tệp tin biến đổi sang thư mục `/var/lib` để tuân thủ tiêu chuẩn Linux và tránh rào cản từ AppArmor.

| Thành phần      | Đường dẫn                              | Quyền sở hữu     | Quyền truy cập |
| :-------------- | :------------------------------------- | :--------------- | :------------- |
| Thư mục dữ liệu | `/var/lib/auto_reply/`                 | `nobody:nogroup` | `775`          |
| Cơ sở dữ liệu   | `/var/lib/auto_reply/reply_history.db` | `nobody:nogroup` | `664`          |
| Nhật ký (Log)   | `/var/lib/auto_reply/auto_reply.log`   | `nobody:nogroup` | `664`          |

### 4.2. Các lệnh thiết lập quyền nhanh

```bash
sudo mkdir -p /var/lib/auto_reply
sudo chown -R nobody:nogroup /var/lib/auto_reply
sudo chmod -R 775 /var/lib/auto_reply
```

---

## 5. Nhật ký gỡ lỗi (Troubleshooting)

Trong quá trình thực hiện, chúng ta đã xử lý các lỗi phổ biến sau:

1.  **Permission Denied (Log):** Xảy ra khi file log được tạo bởi `root` nhưng script chạy bằng `nobody`. Giải quyết bằng cách `chown` cho `nobody`.
2.  **Readonly Database:** Do SQLite không có quyền ghi vào **thư mục** chứa file `.db` để tạo file journal. Giải quyết bằng cách cấp quyền ghi cho thư mục `/var/lib/auto_reply`.
3.  **Command died with status 1:** Lỗi crash script. Luôn kiểm tra `/var/log/mail.log` để biết chính xác dòng code bị lỗi.

---

## 6. Hướng dẫn bảo trì

- **Kiểm tra lịch sử gửi mail:**
  ```bash
  sudo sqlite3 /var/lib/auto_reply/reply_history.db "SELECT * FROM history;"
  ```
- **Xem nhật ký lỗi:**
  ```bash
  sudo cat /var/lib/auto_reply/auto_reply.log
  ```
- **Reset giới hạn cho người dùng:**
  ```bash
  sudo sqlite3 /var/lib/auto_reply/reply_history.db "DELETE FROM history;"
  ```
