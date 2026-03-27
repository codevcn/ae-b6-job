**Đề xuất mô hình kiếm tiền (Monetization Model) cho game**

Dựa trên toàn bộ tài liệu gameplay bạn cung cấp, game là một phiên bản **2048 ASMR** cực kỳ tập trung vào trải nghiệm cảm giác (hình ảnh + âm thanh), album ảnh theo mùa/trend/drama, và yếu tố viral/social. Đây là điểm mạnh lớn để kiếm tiền vì:

- Game có tính “hook” cao (ASMR + trend hot → dễ lan tỏa).
- Nội dung có thể update liên tục (album mới theo sự kiện Tết, Halloween, drama viral).
- Người chơi sẵn sàng chi tiền để có trải nghiệm “thú vị hơn” (âm thanh hay hơn, hình đẹp hơn, undo thoải mái hơn).

### 1. Mô hình chính khuyến nghị: **Freemium + Hybrid (Ads + IAP + Subscription)**

Đây là mô hình phù hợp nhất với thể loại casual puzzle ASMR hiện nay (2048, Merge Mansion, ASMR games…).

| Nguồn thu                         | Tỷ lệ dự kiến            | Chi tiết triển khai (liên kết trực tiếp với gameplay)                                                                                                                                                                                                                               | Lý do phù hợp                                                                                    |
| --------------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Quảng cáo (Ads)**               | 40–50% doanh thu ban đầu | - Rewarded Video: +1 Undo (từ 3 lên 4–5), +1 Hint, nhân đôi điểm 1 lần<br>- Interstitial: sau mỗi ván thắng/thua<br>- Banner nhẹ ở màn hình chính                                                                                                                                   | Người chơi chấp nhận xem quảng cáo để “cứu ván” vì game có undo giới hạn và phạt -5 khi vuốt hụt |
| **In-App Purchase (IAP)**         | 30–35%                   | - Gói Undo vĩnh viễn (199k / 499k)<br>- Album Premium (mỗi album 149k–299k): album Tết VIP, Halloween Horror ASMR, Drama Hot (có hiệu ứng + sound đặc biệt)<br>- Skin ASMR Pack: thay đổi hiệu ứng gộp (pháo hoa, trái tim, hiệu ứng 3D…)<br>- Remove Ads vĩnh viễn (299k one-time) | Album ảnh là điểm nổi bật nhất của game → người chơi rất muốn sở hữu album “đẹp + viral”         |
| **Subscription (Monthly/Yearly)** | 15–20% (tăng dần)        | - **ASMR Pass** (49k/tháng hoặc 399k/năm)<br> • Unlimited Undo<br> • Mở khóa tất cả album hiện tại + album mới tự động<br> • Âm thanh & hiệu ứng ASMR độc quyền (cấp độ cao hơn)<br> • Badge đặc biệt trên bảng xếp hạng                                                            | Người chơi “nghiện” ASMR sẽ muốn trải nghiệm mượt mà, không giới hạn                             |
| **Sự kiện & Cosmetic**            | 5–10%                    | - Battle Pass theo mùa (Tết, Halloween…): miễn phí + trả phí (99k)<br>- Album collab với brand (Lì xì ngân hàng, meme thương hiệu…)                                                                                                                                                 | Dễ bán vì game đã có cơ chế cập nhật album theo trend                                            |

### 2. Các tính năng kiếm tiền cụ thể (đã khớp hoàn toàn với gameplay bạn mô tả)

- **Undo** là “cần câu vàng”: hiện tại chỉ cho 3 lần → bán thêm undo cực kỳ dễ (người chơi 2048 rất ghét mất ván vì 1 nước sai).
- **Album ảnh** là core asset:
  - Album miễn phí: 1–2 album mặc định (ví dụ Tết cơ bản).
  - Album trả phí hoặc Subscription: album “Trend Drama” (cập nhật mỗi 2–4 tuần), album ASMR cao cấp (hình ảnh chất lượng cao + sound effect đặc biệt khi gộp).
- **Bảng xếp hạng thời gian thực**:
  - Top 100 tháng có badge “ASMR Legend” (chỉ người có Subscription mới có).
  - Leaderboard riêng cho người dùng Premium (tăng động lực chi tiền).
- **Gộp hình ảnh + sound effect**: mỗi album premium có sound effect riêng (ví dụ gộp lì xì = tiếng lì xì xì xụp, gộp bí ngô = tiếng cười ma quái ASMR…).

### 3. Mô hình thay thế (nếu muốn thử)

- **Premium One-time Purchase** (699k): mở khóa toàn bộ album + unlimited undo + remove ads vĩnh viễn. Phù hợp nếu team muốn game “không quảng cáo” hoàn toàn.
- **Pure Subscription** (ASMR Club): chỉ bán subscription, game hoàn toàn free nhưng muốn trải nghiệm tốt nhất phải trả phí hàng tháng. Rất hợp với ASMR (người chơi coi như “Netflix ASMR”).
- **Brand Sponsorship + Collab**: bán slot album cho thương hiệu (ví dụ: Shopee Tết, ngân hàng lì xì, TikTok drama…). Đây là nguồn thu thụ động rất lớn ở Việt Nam.

### 4. Gợi ý triển khai giai đoạn đầu (để test)

1. **Tuần 1–4**: Chỉ chạy Ads + gói Undo nhỏ + Remove Ads (dễ implement).
2. **Tháng 2**: Ra album Tết Premium (rất kịp thời).
3. **Tháng 3**: Thêm Subscription ASMR Pass.
4. **Sau 3 tháng**: Theo dõi ARPU, retention, churn → điều chỉnh giá.

**Dự báo doanh thu thô (ước tính)**:

- 100.000 DAU → ARPU 8–12k/tháng là khả thi (vì game Việt + trend mạnh).
- Tháng Tết có thể tăng gấp 3–4 lần nhờ album Tết.
