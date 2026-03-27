# 🔧 Báo Cáo Fix Lỗi: SMTP SASL Authentication trên b6-team.site

**Ngày:** 23/03/2026  
**Hệ thống:** Postfix + Dovecot trên Ubuntu VPS  
**Domain:** `b6-team.site` | **IP:** `160.25.81.154`  
**Tài khoản test:** `support@b6-team.site`

---

## 1. Triệu chứng ban đầu

- ✅ Đăng nhập **IMAP (Port 993)** thành công → nhận mail được bình thường
- ❌ Đăng nhập **SMTP Submission (Port 587)** thất bại → Outlook báo "Không thể đăng nhập"
- Log `/var/log/mail.log` hiển thị:
  ```
  warning: SASL authentication failure: Password verification failed
  warning: unknown[...]: SASL PLAIN authentication failed: authentication failure
  ```

---

## 2. Quá trình chẩn đoán

### Bước 2.1 — Test SMTP thủ công bằng `swaks`

```bash
swaks --to support@b6-team.site --from support@b6-team.site \
  --server mail.b6-team.site --port 587 --tls \
  --auth LOGIN \
  --auth-user support \
  --auth-password 'MẬT_KHẨU'
```

**Kết quả:** Cũng thất bại với lỗi `535 5.7.8 Error: authentication failed`  
**Kết luận:** Lỗi nằm ở **server**, không phải Outlook hay mạng di động.

---

### Bước 2.2 — Kiểm tra Dovecot có xác thực được không

```bash
sudo doveadm auth test support MẬT_KHẨU
```

**Kết quả:**

```
passdb: support auth succeeded
extra fields:
  user=support
```

**Kết luận:** Dovecot xác thực password **hoàn toàn đúng** → vấn đề nằm ở **cầu nối Postfix ↔ Dovecot**.

---

### Bước 2.3 — Kiểm tra cấu hình SASL trong Postfix

```bash
sudo postconf | grep smtpd_sasl
```

**Kết quả phát hiện 3 lỗi nghiêm trọng:**

| Tham số                  | Giá trị sai | Giá trị đúng   |
| :----------------------- | :---------- | :------------- |
| `smtpd_sasl_auth_enable` | `no`        | `yes`          |
| `smtpd_sasl_type`        | `cyrus`     | `dovecot`      |
| `smtpd_sasl_path`        | `smtpd`     | `private/auth` |

---

## 3. Nguyên nhân gốc rễ (Root Cause)

Postfix được cài mặc định với **Cyrus SASL** — một engine xác thực khác hoàn toàn với Dovecot. Trong khi đó, hệ thống đã cài Dovecot làm backend xác thực nhưng **chưa chỉ cho Postfix biết điều đó**.

Cụ thể:

- `smtpd_sasl_auth_enable = no` → **SASL bị tắt hoàn toàn**, Postfix không hề hỏi ai về mật khẩu
- `smtpd_sasl_type = cyrus` → Postfix đang cố dùng Cyrus (không được cài / không có socket)
- `smtpd_sasl_path = smtpd` → Đường dẫn socket sai, không trỏ đến Dovecot

Dovecot đã tạo sẵn socket tại `/var/spool/postfix/private/auth` (xác nhận bằng `ls -la`), nhưng Postfix không biết để dùng nó.

---

## 4. Cách fix

Sửa file `/etc/postfix/main.cf`:

```bash
sudo nano /etc/postfix/main.cf
```

Thêm / cập nhật các dòng sau:

```ini
# Bật SASL Authentication
smtpd_sasl_auth_enable = yes

# Dùng Dovecot làm backend xác thực (thay vì Cyrus mặc định)
smtpd_sasl_type = dovecot

# Trỏ đúng đường dẫn socket của Dovecot
smtpd_sasl_path = private/auth

# Không cho phép đăng nhập ẩn danh
smtpd_sasl_security_options = noanonymous

# Chỉ cho phép AUTH sau khi đã mã hóa TLS
smtpd_tls_auth_only = yes
```

Sau đó restart Postfix:

```bash
sudo systemctl restart postfix
```

---

## 5. Xác nhận fix thành công

Chạy lại swaks:

```bash
swaks --to support@b6-team.site --from support@b6-team.site \
  --server mail.b6-team.site --port 587 --tls \
  --auth PLAIN --auth-user support --auth-password 'MẬT_KHẨU'
```

**Kết quả sau fix:**

```
~> AUTH PLAIN AHN1cHBvcnQA...
<~ 235 2.7.0 Authentication successful
<~ 250 2.0.0 Ok: queued as 634964DBB
```

✅ Xác thực thành công, mail được gửi đi.  
✅ Đăng nhập Outlook Android thành công.

---

## 6. Thông số cấu hình Mail Client

| Thông số                   | Giá trị                |
| :------------------------- | :--------------------- |
| **Email Address**          | `support@b6-team.site` |
| **Username**               | `support`              |
| **Incoming Server (IMAP)** | `mail.b6-team.site`    |
| **Incoming Port**          | `993` — SSL/TLS        |
| **Outgoing Server (SMTP)** | `mail.b6-team.site`    |
| **Outgoing Port**          | `587` — STARTTLS       |

---

## 7. Bài học rút ra

> **Khi cài Postfix + Dovecot trên Ubuntu, Postfix KHÔNG tự động dùng Dovecot để xác thực.**  
> Phải cấu hình thủ công 3 tham số: `smtpd_sasl_auth_enable`, `smtpd_sasl_type`, `smtpd_sasl_path`.

Checklist kiểm tra nhanh khi gặp lỗi SASL tương tự:

1. `sudo postconf | grep smtpd_sasl` → kiểm tra 3 tham số trên
2. `sudo doveadm auth test USERNAME PASSWORD` → xác nhận Dovecot OK
3. `sudo ls -la /var/spool/postfix/private/auth` → xác nhận socket tồn tại
4. `swaks --port 587 --tls --auth PLAIN ...` → test SMTP trực tiếp trên server

---

_Fix hoàn tất lúc 00:34, 23/03/2026_
