Dưới đây là bản tổng hợp chi tiết toàn bộ quá trình chúng ta đã cùng nhau thực hiện để thiết lập thành công hệ thống Proxy trên Google Cloud Platform (GCP). Bạn có thể lưu file này lại dưới dạng `.md` để làm tài liệu hướng dẫn (Cheat Sheet) cho các dự án sau này.

---

# Tài liệu Thiết lập Proxy SOCKS5 (Dante) trên GCP Ubuntu VM

Tài liệu này ghi lại quá trình từ lúc khởi tạo, xử lý lỗi hệ thống cho đến khi hoàn thiện cấu hình Proxy chạy đa giao thức (TCP/UDP) và không yêu cầu xác thực.

## 1. Thông tin hệ thống (Environment)

- **Local Machine:** Windows 11 (Dell Vostro).
- **Cloud Provider:** Google Cloud Platform (GCP).
- **VM Instance Name:** `proxy-b6-beta`.
- **Operating System:** Ubuntu 24.04 LTS (Đã chuyển từ Debian 13 Trixie).
- **External Static IP:** `35.198.236.166`.
- **Target Port:** `1080` (SOCKS5).

---

## 2. Quản lý SSH và Quyền truy cập (SSH Key Management)

Để kết nối từ Windows 11 vào VM, chúng ta đã sử dụng cặp khóa RSA và xử lý lỗi bảo mật file khóa.

### Lệnh cấp quyền cho Private Key trên Windows 11:

Khi gặp lỗi `Bad permissions` (file khóa quá "mở"), chúng ta đã siết lại quyền bằng PowerShell:

```powershell
# Ngắt kế thừa quyền từ thư mục cha
icacls "D:\D-Documents\Credentials\ae-b6\proxy-b6-beta-gcp\gcp_key" /inheritance:r

# Chỉ cho phép User hiện tại (dell) có quyền đọc (Read)
icacls "D:\D-Documents\Credentials\ae-b6\proxy-b6-beta-gcp\gcp_key" /grant:r "$($env:username):R"
```

### Lệnh kết nối SSH:

```powershell
ssh -i "D:\D-Documents\Credentials\ae-b6\proxy-b6-beta-gcp\gcp_key" codevcn@35.198.236.166
```

---

## 3. Cấu hình hạ tầng GCP (Networking & Firewall)

Để Proxy có thể "nhìn thấy" Internet, các quy tắc tường lửa đã được chốt như sau:

- **Static IP:** Đã gán IP tĩnh `35.198.236.166` cho VM để tránh thay đổi IP khi khởi động lại.
- **Firewall Rule:**
  - **Name:** `allow-socks5-proxy` (hoặc tương đương).
  - **Port:** `1080` (Cả **TCP** và **UDP**).
  - **Source Filter:** Đã giới hạn về IP cá nhân của người dùng để bảo mật (thay vì `0.0.0.0/0`) do Proxy đang chạy chế độ không mật khẩu.

---

## 4. Cài đặt và Cấu hình Dante Server

Đây là phần cốt lõi của hệ thống. Chúng ta đã thống nhất sử dụng phiên bản Dante v1.4.3.

### Cài đặt:

```bash
sudo apt update && sudo apt install dante-server nano -y
```

### Cấu hình chuẩn (`/etc/danted.conf`):

Chúng ta đã chốt cấu hình "No Auth" và sửa lỗi cú pháp `client pass` (phải có dấu cách).

```conf
logoutput: syslog
user.privileged: root
user.unprivileged: proxy

# Interface lắng nghe và card mạng xuất dữ liệu
internal: 0.0.0.0 port = 1080
external: ens4

# Phương thức xác thực: NONE (Test thoải mái)
socksmethod: none
clientmethod: none

# Quy tắc cho phép kết nối (Lưu ý: client pass có dấu cách)
client pass {
    from: 0.0.0.0/0 to: 0.0.0.0/0
    log: connect error
}

# Quy tắc truyền dẫn mọi giao thức (TCP/UDP)
socks pass {
    from: 0.0.0.0/0 to: 0.0.0.0/0
    command: bind connect udpassociate
    log: connect error
}
```

---

## 5. Quy trình Kiểm tra và Vận hành (Workflow)

Mọi thay đổi cấu hình đều được thực hiện qua các bước chuẩn:

1.  **Ghi đè cấu hình:** Dùng lệnh `tee` để dán nội dung vào file hệ thống.
2.  **Kiểm tra lỗi cú pháp (Quan trọng):**
    ```bash
    sudo danted -V -f /etc/danted.conf
    ```
3.  **Khởi động lại dịch vụ:**
    ```bash
    sudo systemctl restart danted && sudo systemctl status danted
    ```

---

## 6. Xác nhận kết quả (Verification)

Sử dụng `curl` từ máy cá nhân để kiểm tra tính thông suốt của Proxy:

```powershell
curl -v -x socks5h://35.198.236.166:1080 https://ifconfig.me
```

- **Kết quả mong đợi:** Trả về IP của máy ảo (`35.198.236.166`).
- **Trạng thái:** Thành công.

---

## 7. Các lỗi đã xử lý (Troubleshooting History)

- **Lỗi Hệ điều hành:** Debian Trixie thiếu gói `dante-server` -> Đã chuyển sang Ubuntu 24.04 LTS.
- **Lỗi SSH Host Identification:** Do giữ nguyên IP nhưng thay đổi OS -> Xử lý bằng `ssh-keygen -R [IP]`.
- **Lỗi `token "c"`:** Do cú pháp Dante bản mới yêu cầu `client pass` (có dấu cách) thay vì `clientpass`.
- **Lỗi Read-only Log:** Chuyển từ ghi file `/var/log/danted.log` sang `syslog` để tránh xung đột quyền ghi của user `proxy`.

---

_Tài liệu được khởi tạo vào ngày 31/03/2026 bởi sự phối hợp giữa Lợi và Gemini và Claude._
