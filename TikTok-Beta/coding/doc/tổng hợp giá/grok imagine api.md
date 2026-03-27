# 📊 Bảng Dự Toán Chi Phí Sản Xuất Video - Grok Imagine API

Tài liệu này phân tích chi tiết ngân sách cần thiết để duy trì việc tạo video tự động hàng ngày với cấu hình chuẩn **720p**, được tính toán dựa trên quy mô nhóm **08 người**.

## 1. Thông Số Cấu Hình & Đơn Giá

Dựa trên bảng giá cập nhật năm 2026 của xAI:

- **Độ phân giải:** 720p (HD).
- **Tỷ lệ khung hình:** 9:16 (Dọc).
- **Đơn giá:** **$0.05 / giây**.
- **Thời lượng mỗi video:** 1 phút (**60 giây**).
- **Tần suất:** Ít nhất 03 video/ngày.

---

## 2. Chi Tiết Tính Toán Tổng Lực

Việc tính toán được chia theo các cấp độ thời gian để quản lý dòng tiền tổng quát:

- **Chi phí cho 01 Video:** $60 \text{ giây} \times \$0.05 = \mathbf{\$3.00}$
- **Chi phí hằng ngày (03 Video):** $3 \times \$3.00 = \mathbf{\$9.00}$
- **Tổng chi phí hằng tháng (30 ngày):** $30 \times \$9.00 = \mathbf{\$270.00}$

---

## 3. Phân Chia Chi Phí Nhóm (Team Split)

Giả định chi phí được chia đều cho tất cả **08 thành viên** trong nhóm:

> **Công thức:** $\text{Tổng chi phí tháng} \div 8$

| Chỉ số               | Chi phí cho 8 người (Tổng) | Chi phí cho mỗi người |
| :------------------- | :------------------------- | :-------------------- |
| **Hằng tháng (USD)** | **$270.00**                | **$33.75**            |
| **Hằng tháng (VNĐ)** | **6.750.000 VNĐ**          | **843.750 VNĐ**       |

_Lưu ý: Giá quy đổi VNĐ ước tính theo tỷ giá 1 USD ≈ 25.000 VNĐ._

---

## 4. Bảng Quy Đổi Tổng Hợp

| Thời gian   | Tổng chi phí (USD) | Tổng chi phí (VNĐ) | Mỗi người đóng (VNĐ) |
| :---------- | :----------------- | :----------------- | :------------------- |
| **1 Ngày**  | $9.00              | 225.000 VNĐ        | 28.125 VNĐ           |
| **1 Tuần**  | $63.00             | 1.575.000 VNĐ      | 196.875 VNĐ          |
| **1 Tháng** | **$270.00**        | **6.750.000 VNĐ**  | **843.750 VNĐ**      |
