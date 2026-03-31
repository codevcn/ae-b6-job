Chào Lợi, việc chuyển đổi sang **AWS Global Accelerator (AGA)** là một bước nâng cấp đáng kể về độ ổn định cho hệ thống của bạn. Thay vì phải duy trì và xử lý lỗi định tuyến trên "trạm trung chuyển" Singapore, bạn sẽ sử dụng mạng lưới Anycast toàn cầu của AWS để đi vào đường truyền riêng (Backbone) của họ ngay tại điểm gần Việt Nam nhất.

Dưới đây là quy trình chuẩn A-Z để thiết lập hệ thống này thay thế cho mô hình 2-hop cũ.

---

## 📋 Giai đoạn 1: Khởi tạo AWS Global Accelerator

Đây là bước tạo ra "cổng vào" thông minh cho gói tin của bạn.

- **Bước 1.1:** Truy cập vào **AWS Console**, tìm kiếm dịch vụ **Global Accelerator**.
- **Bước 1.2:** Nhấn **Create accelerator**. Đặt tên dễ nhớ như `WireGuard-Tokyo-Accelerator`.
- **Bước 1.3:** Chọn loại **Standard accelerator**. Phần IP address type giữ nguyên là **IPv4**.
- **Bước 1.4:** Sau khi nhấn tạo, AWS sẽ cấp cho bạn **2 Static IP addresses** cố định. Hãy lưu lại 2 IP này để dùng cho thiết bị đầu cuối.

---

## 📋 Giai đoạn 2: Cấu hình Listener và Endpoint Group

Phần này định nghĩa cách AGA đón và điều hướng dữ liệu đến Tokyo.

- **Bước 2.1 - Tạo Listener:**
  - **Protocol:** Chọn **UDP** (vì WireGuard chạy trên giao thức này).
  - **Port ranges:** Điền **51820** (hoặc port bạn đang dùng cho WireGuard trên máy Tokyo).
  - **Client affinity:** Chọn **Source IP**. Điều này đảm bảo kết nối từ thiết bị của bạn luôn được giữ ổn định trên một luồng dữ liệu duy nhất.
- **Bước 2.2 - Tạo Endpoint Group:**
  - **Region:** Chọn **ap-northeast-1 (Tokyo)**.
  - Các thông số về Health check có thể để mặc định, tuy nhiên với VPN bạn nên cân chỉnh lại để tránh việc AGA hiểu nhầm VPS bị "down" khi bạn đang không sử dụng.
- **Bước 2.3 - Thêm Endpoint:**
  - **Endpoint type:** Chọn **EC2 Instance**.
  - **Endpoint:** Chọn chính xác Instance Tokyo của bạn (hiện đang có IP là `13.193.91.19`).
  - **Lưu ý cực kỳ quan trọng:** Bạn **phải tắt (Uncheck)** ô **"Preserve client IP address"**. Nếu bật tính năng này, EC2 Tokyo sẽ thấy IP gốc từ Việt Nam của bạn và gây ra lỗi định tuyến vòng lặp, khiến bạn không thể truy cập internet.

---

## 📋 Giai đoạn 3: Cấu hình Security Group tại Tokyo

Vì bây giờ dữ liệu sẽ đi từ hạ tầng của AGA vào EC2, bạn cần mở cửa cho nó.

- **Bước 3.1:** Vào phần **Security Groups** của Instance Tokyo.
- **Bước 3.2:** Thêm một **Inbound Rule** mới:
  - **Type:** Custom UDP.
  - **Port range:** 51820.
  - **Source:** `0.0.0.0/0` (Nếu muốn bảo mật hơn, bạn có thể chỉ cho phép dải IP của AWS Global Accelerator, nhưng để test nhanh thì dùng `0.0.0.0/0` là ổn nhất).

---

## 📋 Giai đoạn 4: Cấu hình trên thiết bị (Windows 11 / Phone)

Bạn không cần tạo tunnel mới, chỉ cần sửa file config hiện tại của bạn.

- **Bước 4.1:** Mở phần mềm WireGuard trên máy tính hoặc điện thoại.
- **Bước 4.2:** Tìm đến dòng `Endpoint` trong file cấu hình.
- **Bước 4.3:** Thay thế IP của Singapore (`18.140.133.115`) hoặc IP của Tokyo (`13.193.91.19`) bằng **một trong hai IP tĩnh** mà AGA đã cấp ở Giai đoạn 1.
  - Ví dụ: `Endpoint = 1.2.3.4:51820` (với `1.2.3.4` là IP của Accelerator).
- **Bước 4.4:** Lưu lại và nhấn **Activate**.

---

## 📋 Giai đoạn 5: Kiểm tra và Dọn dẹp

- **Kiểm tra IP:** Sử dụng lệnh `curl.exe -4 ifconfig.me` trên Windows để đảm bảo kết quả vẫn trả về IP của Tokyo `13.193.91.19`.
- **Kiểm tra lộ trình:** Chạy lệnh `tracert -d -4 8.8.8.8`. Bạn sẽ thấy số lượng hop giảm xuống rõ rệt so với mô hình 2-hop cũ, vì gói tin đã "nhảy" thẳng vào mạng của Amazon.
- **Dọn dẹp:** Sau khi AGA đã hoạt động ổn định, bạn có thể **Terminate (Xóa)** Instance Singapore để tiết kiệm chi phí thuê VPS hàng tháng.

> [!IMPORTANT]
> **Lưu ý về chi phí:** AWS Global Accelerator có phí duy trì cố định khoảng **$18/tháng** cộng với phí truyền tải dữ liệu (Data Transfer-Premium). Bạn hãy cân nhắc nếu ngân sách cho việc "nuôi" proxy này không quá dư dả.

Bạn có muốn mình hướng dẫn cách thiết lập **Health Check** chi tiết để đảm bảo kết nối không bị ngắt quãng khi bạn xem video dung lượng lớn trên TikTok không?
