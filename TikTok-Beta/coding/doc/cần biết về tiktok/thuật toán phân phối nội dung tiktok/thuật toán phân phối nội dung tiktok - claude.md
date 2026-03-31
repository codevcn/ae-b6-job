Đây là một chủ đề thú vị và phức tạp. Hãy để mình mổ xẻ từng lớp của thuật toán TikTok.

---

## Thuật toán phân phối nội dung của TikTok: Mổ xẻ toàn diện

Mục tiêu cốt lõi của thuật toán TikTok chỉ có một: **maximize watch time và engagement** bằng cách đưa đúng nội dung đến đúng người vào đúng thời điểm. Nghe đơn giản, nhưng cơ chế bên dưới cực kỳ tinh vi.

---

### Tầng 1 — Ba nhóm tín hiệu đầu vào

Thuật toán TikTok phân tích ba nhóm tín hiệu chính: **user interactions** (những gì người dùng xem, thích, chia sẻ, bình luận, hoặc bỏ qua), **video information** (caption, hashtag, âm thanh, hiệu ứng, lượt xem), và **user information** (ngôn ngữ, quốc gia, loại thiết bị và cài đặt).

Trong số đó, các tín hiệu tương tác người dùng được xem là mạnh nhất. Likes là chỉ báo cơ bản. Comments thể hiện sự gắn kết sâu hơn, đặc biệt là comments có nội dung có giá trị. Shares là tín hiệu mạnh cho thấy người dùng thấy nội dung đủ giá trị để chia sẻ. Saves (lưu lại) là chỉ số ngày càng quan trọng, cho thấy nội dung có giá trị tham khảo lại. Re-watches — khi người dùng xem một video nhiều lần — là một trong những tín hiệu mạnh nhất mà thuật toán ưu tiên hàng đầu.

Hãy xem sơ đồ tổng quan cơ chế phân phối:

[Sơ đồ phân phối nội dung TikTok](./tiktok_distribution_algorithm.png)

### Tầng 2 — Cơ chế "Wave" phân phối theo từng giai đoạn

Đây là phần thú vị nhất và ít được hiểu nhất của thuật toán TikTok.

Thuật toán TikTok hoạt động theo nguyên lý thử-sai (trial-and-error). Khi một video mới được đăng, nó được test bằng cách chiếu cho một nhóm nhỏ người dùng xem trước. Mức độ engagement của nhóm này sẽ quyết định video có được mở rộng ra audience lớn hơn hay không. Các tín hiệu quan trọng gồm: tỉ lệ xem hết video và các tương tác như like, comment, share.

Nếu video vượt qua được nhóm test đầu tiên, nó bước vào cơ chế gọi là **virality loop** hay **snowball effect** — thuật toán đẩy video qua một loạt các "wave" phân phối ngày càng lớn hơn. Mỗi wave là một bài test mới ở quy mô lớn hơn. Nếu video không vượt qua được nhóm test ban đầu, phân phối của nó bị chậm lại đáng kể, và hành trình viral của video về cơ bản kết thúc tại đây.

Video có engagement cao trong những giờ đầu tiên có cơ hội tiếp cận nhiều người dùng hơn. Hook 3 giây đầu tiên quyết định liệu người xem có tiếp tục theo dõi hay vuốt qua. Nếu người xem xem lại, comment, hoặc chia sẻ, thuật toán xem video đó là nội dung có giá trị. Đặc biệt, một video cũ vẫn có thể "sống lại" vì TikTok tái đánh giá nội dung dựa trên engagement mới.

---

### Tầng 3 — Cập nhật 2025: Micro-niche thay vì viral đại trà

Năm 2025, TikTok đã thay đổi đáng kể với chiến lược **micro-niche push**: nhóm người dùng đầu tiên được chiếu video không còn là một mẫu ngẫu nhiên nữa, mà là một nhóm được nhắm mục tiêu cực kỳ chính xác dựa trên sở thích của họ. Điều này có nghĩa là ít có những video viral bất ngờ hơn — thay vào đó, hầu hết người dùng sẽ thấy nội dung phù hợp chính xác với niche của họ.

Hootsuite gọi xu hướng này là "**micro-virality**" — và nó đang thay đổi cách các thương hiệu phát triển trên TikTok. Thay vì theo đuổi những hit viral khó đoán và rộng lớn, nội dung nhắm vào cộng đồng niche cụ thể (như #BookTok, #SportsOnTikTok) sẽ được khuếch đại mạnh hơn trong những cộng đồng đó. TikTok data cho thấy video chất lượng cao có tốc độ tăng follower gấp 40 lần so với video chất lượng thấp.

---

### Tầng 4 — Những gì thuật toán KHÔNG quan tâm (Counter-intuitive)

Đây là những điều nhiều creator hiểu sai:

**Số follower không phải yếu tố xếp hạng trực tiếp.** Follower count và hiệu suất video trong quá khứ không phải là yếu tố trực tiếp trong hệ thống gợi ý — điều này tạo ra môi trường mà một creator mới có zero follower vẫn có cơ hội thực sự để video đi viral.

**Vị trí địa lý chỉ là tín hiệu yếu.** Việc ở cùng quốc gia với người tạo nội dung chỉ được TikTok coi là "chỉ báo yếu" cho thấy bạn sẽ quan tâm đến video đó.

**Like/unlike cũng được ghi nhận.** Ngay cả khi người dùng thích rồi bỏ thích, theo dõi rồi hủy theo dõi, bình luận rồi xóa — thuật toán TikTok vẫn ghi nhận tất cả những hành động đó.

---

### Tóm lại: Công thức thực tế

Nếu phải rút gọn thành một framework, thuật toán TikTok vận hành theo logic:

> **Nội dung phù hợp niche** × **Hook mạnh (3 giây đầu)** × **Watch time / completion rate cao** × **Engagement có chiều sâu (save, share > like)** = Được đẩy lên wave lớn hơn

Âm nhạc và âm thanh trending cũng tác động đáng kể — trending audio làm tăng mức độ ưu tiên của thuật toán và khả năng khám phá nội dung. Thuật toán theo dõi watch time để hiển thị nội dung phù hợp với sở thích người dùng, giữ người xem gắn kết lâu hơn.

Điều làm TikTok khác biệt so với Instagram hay YouTube là nó **không ưu tiên social graph** (mạng lưới bạn bè/người theo dõi), mà ưu tiên **interest graph** (đồ thị sở thích) — điều này giải thích tại sao FYP của mỗi người lại khác nhau hoàn toàn và tại sao một người mới vẫn có thể viral ngang với creator triệu follow.
