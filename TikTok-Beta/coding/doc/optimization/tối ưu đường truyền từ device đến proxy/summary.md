Để tối ưu đường truyền từ thiết bị (device) đến proxy VPS, các tài liệu đều tập trung vào việc giảm độ trễ (latency/RTT), giảm mất gói tin (packet loss) và tăng thông lượng (throughput). Dưới đây là các phương pháp chung được đề xuất nhiều nhất:

**1. Chọn Region (Vị trí đặt máy chủ) gần nhất**
Đây được đánh giá là yếu tố quan trọng hàng đầu tạo ra sự khác biệt rõ rệt nhất. Các tài liệu đều khuyên nên đặt VPS ở **Singapore (ap-southeast-1)** hoặc **Hong Kong (ap-east-1)** để có khoảng cách vật lý gần Việt Nam nhất, giúp giảm độ trễ xuống mức tối ưu (khoảng 30-60ms).

**2. Kích hoạt thuật toán TCP BBR trên VPS**
Việc bật tính năng kiểm soát tắc nghẽn BBR của Google trên hệ điều hành Ubuntu là bước tối ưu máy chủ được nhắc đến ở hầu hết các tài liệu. BBR đặc biệt hiệu quả trong việc tăng băng thông và giảm nghẽn mạng trên các kết nối đường dài, hay bị rớt gói tin (packet loss) như từ Việt Nam đến AWS.

**3. Thay đổi giao thức: Dùng UDP hoặc Tunneling thay vì SOCKS5 TCP "trần"**
Mặc định proxy SOCKS5 (như Dante) chạy trên TCP và dễ bị các nhà mạng (ISP) tại Việt Nam bóp băng thông (throttling) thông qua kiểm tra gói tin sâu (DPI). Các tài liệu đề xuất mạnh mẽ việc chuyển sang:

- **WireGuard**: Cực kỳ nhanh, độ trễ thấp, chạy trên nền UDP, là lựa chọn lý tưởng nhất cho các ứng dụng video streaming như TikTok.
- **Shadowsocks / V2Ray (VMess/VLESS)**: Các giao thức có mã hóa giúp luồng dữ liệu vượt qua hệ thống kiểm soát của ISP mượt mà và ổn định hơn.

**4. Tối ưu tài nguyên mạng và phần cứng trên AWS**

- **Sử dụng Instance và ENA mạnh mẽ:** Khuyến nghị tránh các dòng EC2 quá yếu (như t3/t4.micro) mà nên dùng các instance có tối ưu mạng (như t3.small, c6g, c6i.large). Cần đảm bảo tính năng **ENA (Elastic Network Adapter)** đã được bật để tránh bị bóp hiệu năng mạng và giảm latency.
- **AWS Global Accelerator:** Một giải pháp cao cấp giúp cải thiện 40-60% tốc độ bằng cách cho phép luồng dữ liệu đi qua mạng lưới backbone siêu nhanh của AWS thay vì internet công cộng thông thường.

**5. Tối ưu thông số Kernel Linux và MTU**

- **Hệ điều hành:** Điều chỉnh file `/etc/sysctl.conf` để tăng giới hạn file mở (File Descriptors), tối ưu dải cổng (Port Range) và tăng kích thước bộ đệm TCP (Buffer) cho các kết nối đường dài.
- **MTU (Maximum Transmission Unit):** Chỉnh sửa MTU để tránh việc gói tin bị phân mảnh làm chậm tốc độ. Các mức khuyến nghị có thể là hạ xuống 1400, 1450 hoặc dùng MTU 9001 mặc định của hệ thống AWS tùy trường hợp.

**6. Tối ưu cấu hình Proxy (Dante) và phía thiết bị**

- **Trên Dante VPS:** Giảm mức độ ghi log (chỉ giữ lại log lỗi) để tránh nghẽn I/O, tăng số lượng worker, và cấu hình keep-alive (hoặc đặt reverse proxy phía trước) để giữ kết nối, giảm thời gian TCP handshake.
- **Trên thiết bị cá nhân:** Dùng mạng Wi-Fi hoặc LAN có độ ổn định cao thay vì mạng 4G. Sử dụng tính năng **Split tunneling** (chỉ định tuyến duy nhất app TikTok qua proxy) để giảm tải cho VPS, đồng thời thiết lập QoS trên router để ưu tiên băng thông cho thiết bị kết nối proxy. Sử dụng các ứng dụng proxy client tối ưu trên máy như Shadowrocket, V2RayNG, hoặc Proxifier.
