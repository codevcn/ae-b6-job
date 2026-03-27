# 📊 Dự Toán Chi Phí Kling AI API (Developer) - Team 8 Người

Tài liệu này phân tích ngân sách khi sử dụng API để tạo 90 video mỗi tháng (03 video/ngày), mỗi video dài 1 phút với định dạng 720p.

## 1. Cơ Chế Tính Phí API

Kling AI API sử dụng đơn vị **Computing Units (CU)** hoặc **Credits**. Theo chính sách dành cho Developer:

- **Giá đơn vị:** Khoảng **$0.01 / Credit** (khi nạp các gói lớn như $100 cho 10.000 Credits).
- **Tiêu hao cho 01 video 1 phút (Standard Mode):**
  - 10 giây đầu tiên: 20 Credits.
  - Mở rộng (Extend) 50 giây tiếp theo (10 lần x 5 giây): 10 Credits × 10 = 100 Credits.
  - **Tổng cộng:** **120 Credits / video.**

---

## 2. Tổng Chi Phí Hằng Tháng (90 Video)

Việc tính toán được thực hiện cho hai kịch bản chất lượng khác nhau để nhóm bạn có lựa chọn phù hợp:

### Kịch bản A: Chế độ Tiêu chuẩn (Standard Mode - 720p)

Đây là chế độ phù hợp nhất cho các nội dung mạng xã hội số lượng lớn.

- **Tổng Credit/tháng:** 90 video × 120 Credits = **10.800 Credits.**
- **Tổng chi phí (USD):** **$108.00 / tháng.**
- **Tổng chi phí (VNĐ):** **2.700.000 VNĐ / tháng.**

### Kịch bản B: Chế độ Chuyên nghiệp (Professional Mode)

Dành cho yêu cầu độ chân thực cao và chuyển động phức tạp hơn.

- **Tiêu hao/video:** 70 (gốc) + 350 (extend) = 420 Credits.
- **Tổng Credit/tháng:** 90 video × 420 Credits = **37.800 Credits.**
- **Tổng chi phí (USD):** **$378.00 / tháng.**
- **Tổng chi phí (VNĐ):** **9.450.000 VNĐ / tháng.**

---

## 3. Phân Chia Chi Phí Cho Nhóm 08 Người

Dưới đây là số tiền mỗi thành viên cần đóng góp dựa trên kịch bản phổ biến nhất là **Standard Mode**:

| Hạng mục            | Tổng chi phí nhóm | Chi phí mỗi người (1/8) |
| :------------------ | :---------------- | :---------------------- |
| **Mỗi tháng (USD)** | **$108.00**       | **$13.50**              |
| **Mỗi tháng (VNĐ)** | **2.700.000 VNĐ** | **337.500 VNĐ**         |

_Tỷ giá quy đổi ước tính: 1 USD ≈ 25.000 VNĐ._

---

## 4. So Sánh Kinh Tế: API vs Web vs Grok

| Nền tảng                    | Tổng chi phí/tháng (90p video) | Ưu điểm                                               |
| :-------------------------- | :----------------------------- | :---------------------------------------------------- |
| **Kling AI API (Standard)** | **2.700.000 VNĐ**              | Rẻ nhất, dễ tích hợp vào Server.                      |
| **Kling AI Web (Gói Pro)**  | **~6.250.000 VNĐ**             | Có giao diện kéo thả, dễ dùng cho người không chuyên. |
| **Grok Imagine API**        | **6.750.000 VNĐ**              | Tốc độ xử lý nhanh, engine suy luận thông minh.       |

# 📑 So Sánh: Extend Video vs. Independent Clips (API)

Khi bạn chia nhỏ 1 phút phim thành 6 đoạn độc lập (mỗi đoạn 10 giây):

## 1. Phân Tích Chi Phí (Credits)

Kling AI API tính phí dựa trên tổng thời lượng render.

- **Cách 1 (Extend):** 10 giây đầu (20 credits) + 50 giây mở rộng (100 credits) = **120 Credits**.
- **Cách 2 (6 Clips độc lập):** 10 giây $\times$ 6 lần tạo = $6 \times 20 = \mathbf{120 \text{ Credits}}$.

> **Kết luận:** Tổng chi phí cho nhóm 8 người vẫn giữ nguyên ở mức **~337.500 VNĐ/người/tháng** (cho kịch bản 90 video 1 phút/tháng).

---

## 2. Ưu và Nhược điểm của kỹ thuật nối Last Frame

Việc bạn dùng kỹ thuật lấy khung hình cuối (Last Frame) của clip 1 làm khung hình đầu (First Frame) cho clip 2 là một chiến thuật thông minh.

### ✅ Ưu điểm (Tại sao bạn nên chọn cách này):

- **Tiết kiệm khi lỗi (Failure Isolation):** Nếu bạn Extend đến giây thứ 50 mà AI "làm hỏng" chuyển động ở đoạn cuối, bạn có nguy cơ phải làm lại cả quá trình hoặc chấp nhận một kết thúc tệ. Với clip độc lập, nếu clip thứ 5 xấu, bạn chỉ cần bỏ 20 Credits để tạo lại đúng 10 giây đó.
- **Kiểm soát nội dung tốt hơn:** Bạn có thể thay đổi Prompt cho từng đoạn 10 giây để lái câu chuyện theo ý muốn (ví dụ: chuyển từ cảnh đặc tả sang cảnh toàn) dễ dàng hơn là dùng một Prompt dài cho tính năng Extend.
- **Song song hóa (Parallel Processing):** Với API, bạn có thể gửi lệnh tạo cả 6 clip cùng một lúc (nếu tài khoản đủ Tier). Việc này nhanh hơn nhiều so với việc chờ clip 1 xong mới bấm Extend clip 2.

### ❌ Nhược điểm & Thách thức kỹ thuật:

- **Xử lý hậu kỳ:** Bạn sẽ cần viết code (dùng **FFmpeg**) để nối 6 tệp `.mp4` lại thành một video hoàn chỉnh.
- **Độ mượt (Consistency):** Dù dùng Last Frame, đôi khi AI vẫn có thể gây ra hiện tượng "nháy" nhẹ (flicker) ở điểm nối giữa các clip nếu ánh sáng hoặc hạt nhiễu (noise) của hai lần tạo không đồng nhất.
- **Quản lý Storage:** Bạn sẽ phải quản lý nhiều file nhỏ trong Server (**YtoSub Server**) trước khi gộp chúng lại.

---

## 3. Bảng Tổng Hợp Chi Phí Cập Nhật (Dành cho Team 8 người)

Dưới đây là bảng chi phí nếu nhóm quyết định đi theo hướng tạo các clip 10 giây độc lập rồi nối lại:

| Thông số                       | Chi tiết                     |
| :----------------------------- | :--------------------------- |
| **Số đoạn cho 1 video 1 phút** | 6 đoạn (mỗi đoạn 10 giây)    |
| **Giá mỗi đoạn (Standard)**    | 20 Credits                   |
| **Tổng Credit/Video 1 phút**   | **120 Credits**              |
| **Tổng tiền nhóm (90 video)**  | **$108.00 (~2.700.000 VNĐ)** |
| **Mỗi thành viên đóng (1/8)**  | **337.500 VNĐ**              |
