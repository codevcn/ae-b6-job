# Mô hình kiếm tiền cho game 2048 bản gộp hình

> Tổng hợp các cách kiếm tiền từ game 2048 bản gộp hình, bao gồm quảng cáo, mua hàng trong ứng dụng, và các chiến lược khác để tối ưu hóa doanh thu.

## 1. Quảng cáo trong ứng dụng (In-App Advertising)

### Rewarded Ads (Quảng cáo có thưởng)

> Player xem quảng cáo để nhận phần thưởng.

- thêm lượt undo
- hồi sinh, tiếp tục chơi sau khi thua
- kéo dài thời gian chơi thêm một lượng thời gian nhất định
- thêm 1 hình mới vào bàn chơi
- xóa 1 hình không mong muốn
- move 1 hình sang vị trí khác

### Interstitial Ads (Quảng cáo xen kẽ)

> Hiển thị quảng cáo toàn màn hình.

- Hiển thị sau mỗi 3 lượt chơi
- Hiển thị ở lượt chơi thành công (đạt max điểm) lần thứ 1
- Hiển thị ở lượt chơi thất bại lần thứ 3

### Banner Ads (Quảng cáo banner)

> Hiển thị quảng cáo ở vị trí cố định.

- Đặt ở màn hình menu

## 2. Mua hàng trong ứng dụng (In-App Purchases)

> Cho phép người chơi mua các gói nâng cấp hoặc vật phẩm để cải thiện trải nghiệm chơi game.

1. Gói gỡ bỏ quảng cáo

- Gỡ toàn bộ quảng cáo trong game

2. Gói hỗ trợ chơi

- lượt undo không giới hạn (dành cho ai muốn try-hard trong giải đấu)
- ko có giới hạn thời gian chơi
