**Anycast Routing** là một kỹ thuật định tuyến mạng trong đó cùng một địa chỉ IP được quảng bá từ nhiều địa điểm vật lý khác nhau trên thế giới. Khi bạn gửi một yêu cầu đến địa chỉ đó, mạng (thông qua BGP) sẽ tự động đưa bạn đến máy chủ _gần nhất_ hoặc _tối ưu nhất_ — không phải gần về địa lý, mà gần về cấu trúc mạng.

Hãy xem sơ đồ hoạt động dưới đây:Điểm mấu chốt của Anycast là **không phải client chọn máy chủ** — mà BGP tự động làm điều đó dựa trên AS-Path ngắn nhất.

**Cách nó hoạt động từng bước:**

Mỗi máy chủ Anycast quảng bá cùng một prefix IP (ví dụ `1.2.3.4/32`) lên BGP từ các vị trí khác nhau. Khi bạn ở Hà Nội gõ `1.2.3.4`, router của Viettel nhận thấy có hai đường đến địa chỉ đó: một qua 3 AS đến Frankfurt, một qua 1 AS đến Hà Nội. BGP chọn đường ngắn hơn → bạn kết nối đến Hà Nội mà không hay biết gì.

**Ứng dụng thực tế:**

Đây là kỹ thuật nền tảng của hầu hết hạ tầng Internet hiện đại. Cloudflare dùng Anycast cho toàn bộ mạng CDN và DNS `1.1.1.1` của họ — hơn 300 địa điểm cùng quảng bá một địa chỉ IP, người dùng toàn cầu đều kết nối dưới 20ms. Google cũng dùng Anycast cho `8.8.8.8`. Khi một node bị tấn công DDoS, traffic tự động phân tán sang các node khác mà không cần can thiệp thủ công.

**Điểm khác biệt với các kỹ thuật tương tự:**

|               | Unicast          | Anycast                   | Multicast              |
| ------------- | ---------------- | ------------------------- | ---------------------- |
| Máy nhận      | 1 cố định        | 1 gần nhất                | Nhiều máy cùng lúc     |
| Dùng cho      | Web thông thường | DNS, CDN, DDoS mitigation | Video streaming nội bộ |
| Phụ thuộc BGP | Không            | Có                        | Không                  |

Điều làm Anycast đặc biệt là nó hoàn toàn trong suốt với người dùng. Bạn gõ `1.1.1.1` và nghĩ rằng mình đang kết nối đến một máy chủ duy nhất — nhưng thực ra Cloudflare có hơn 300 máy chủ trên thế giới, tất cả đều trả lời địa chỉ đó. BGP là người quyết định âm thầm phía sau: nó so sánh số bước nhảy qua các AS và chọn con đường ngắn nhất, tức là máy chủ "gần" nhất về mặt mạng.

Có ba hệ quả thực tế rất quan trọng từ thiết kế này. Thứ nhất là tốc độ — bạn ở Hà Nội kết nối đến node Hà Nội thay vì phải đi vòng qua Mỹ, độ trễ giảm từ 200ms xuống còn 5–10ms. Thứ hai là khả năng chịu tải — khi một node bị tấn công DDoS với hàng triệu request, traffic tự động phân tán sang các node khác mà không cần cấu hình gì thêm. Thứ ba là tính dự phòng — nếu một datacenter mất điện, BGP lập tức định tuyến lại sang datacenter kế tiếp, người dùng hầu như không cảm nhận được sự gián đoạn.
