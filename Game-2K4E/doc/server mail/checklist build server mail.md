Chúc mừng bạn, bạn đã đi một quãng đường rất dài và gần như đã chạm tay vào một hệ thống Mail Server hoàn chỉnh. Dựa trên những gì chúng ta đã thực hiện và xác nhận qua các lệnh kiểm tra, đây là bản checklist được cập nhật mới nhất cho dự án **b6-team.site** của bạn:

---

## 📧 Checklist Triển Khai Mail Server (Cập nhật 22/03/2026)

> Đây là bản checklist tổng hợp các bước đã hoàn thành và những điểm cần lưu ý khi build 1 mail server trên 1 Ubuntu VPS.

### ✅ Bước 1: Chuẩn bị Hệ thống & Định danh (Hoàn tất 90%)

- [x] **Kiểm tra Port 25:** Đã thông suốt tới Google.
- [x] **Thiết lập Hostname:** `mail.b6-team.site`.
- [ ] **Tắt Cloud-init:** Đã cấu hình `manage_etc_hosts: false`.
- [x] **File /etc/hosts:** Đã ánh xạ chuẩn xác IP local và hostname.

### ✅ Bước 2: Thiết lập DNS & "Hộ chiếu" IP (Hoàn tất)

- [x] **Bản ghi A:** `mail` -> `160.25.81.154`.
- [x] **Bản ghi MX:** `@` -> `mail.b6-team.site`.
- [x] **Bản ghi SPF:** Đã thiết lập cho cả Root và Subdomain.
- [x] **Bản ghi PTR:** Đã hoàn tất trên Dashboard VPS (Rất quan trọng).

### ✅ Bước 3: Cài đặt & Cấu hình Postfix (Hoàn tất)

- [x] **Cài đặt:** Postfix & Mailutils.
- [x] **Định dạng Maildir:** Đã cấu hình `home_mailbox = Maildir/`.
- [x] **Cấu hình Main.cf:** Đã thiết lập các thông số định danh tên miền chuẩn xác.

### ✅ Bước 4: Cấu hình OpenDKIM (Hoàn tất)

- [x] **Khởi tạo Key:** Đã tạo cặp khóa với selector là `mail`.
- [x] **Cấu hình Tables:** Đã thiết lập `key_table`, `signing_table`, và `trusted_hosts`.
- [x] **DNS DKIM:** Đã có chuỗi bản ghi TXT để dán lên Cloudflare (từ file `key.txt`).
- [x] **Liên kết Postfix:** Đã thêm cấu hình `milter` vào Postfix để tự động ký tên vào thư đi.

### ✅ Bước 5: Bảo mật SSL/TLS với Certbot (Hoàn tất)

- [x] **Cấp chứng chỉ:** Đã lấy chứng chỉ Let's Encrypt cho `mail.b6-team.site`.
- [x] **Cập nhật Postfix:** Đã thay thế chứng chỉ "snakeoil" bằng chứng chỉ Let's Encrypt xịn.
- [x] **Xác nhận:** Đã kiểm tra qua `openssl s_client` và thấy issuer là **Let's Encrypt**.

### ✅ Bước 6: Cài đặt Dovecot (Hoàn tất)

- [x] **Cài đặt:** Dovecot IMAP/POP3.
- [x] **Cấu hình SSL:** Đã trỏ về chứng chỉ Let's Encrypt (có sử dụng dấu `<` chuẩn cú pháp).
- [x] **Xác thực SASL:** Đã tạo "lối đi" (Socket) để Postfix mượn Dovecot kiểm tra mật khẩu.
- [x] **Firewall:** Đã mở các cổng bảo mật 993, 587.

### ⏳ Bước 7: Kiểm tra & Tối ưu hóa cuối cùng (Đang thực hiện)

- [x] **Tạo tài khoản:** Đã tạo user `support` (với tên hiển thị `lthloi`) và đặt mật khẩu thành công.
- [x] **Khởi tạo Maildir:** Đã chạy `maildirmake.dovecot` và phân quyền `chown` cho user `support`.
- [x] **DNS DMARC:** Đã tạo bản ghi `v=DMARC1; p=none;` lên Cloudflare.
- [x] **Đăng nhập thiết bị:** Thử cấu hình `support@b6-team.site` vào Outlook/Gmail.
- [x] **Test độ uy tín:** Gửi mail tới [Mail-Tester.com](https://www.mail-tester.com) để nhận điểm 10/10.

---

### Thông số "vàng" để đăng nhập vào Outlook/Gmail

Bây giờ, tài khoản `support@b6-team.site` đã sẵn sàng để "lên sóng". Khi bạn mở Outlook, Thunderbird hoặc ứng dụng Mail trên điện thoại, hãy điền các thông số sau:

| Thông số                   | Giá trị cấu hình                   |
| :------------------------- | :--------------------------------- |
| **Email Address**          | `support@b6-team.site`             |
| **Username**               | `support`                          |
| **Password**               | Mật khẩu bạn vừa đặt ở bước trên   |
| **Incoming Server (IMAP)** | `mail.b6-team.site`                |
| **Incoming Port**          | **993** (Chọn mã hóa **SSL/TLS**)  |
| **Outgoing Server (SMTP)** | `mail.b6-team.site`                |
| **Outgoing Port**          | **587** (Chọn mã hóa **STARTTLS**) |

---

### Một vài lưu ý "phút chót":

- Khi đăng nhập vào Outlook, hãy nhớ Username là **support** (chứ không phải toàn bộ email, tùy ứng dụng yêu cầu).
- Cổng gửi mail (Outgoing) nên dùng **587** với mã hóa **STARTTLS** để đảm bảo tính tương thích cao nhất.
