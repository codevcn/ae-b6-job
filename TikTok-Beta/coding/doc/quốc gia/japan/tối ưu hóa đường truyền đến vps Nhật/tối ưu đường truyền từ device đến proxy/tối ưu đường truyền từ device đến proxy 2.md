Việc tối ưu hóa đường truyền từ thiết bị cá nhân đến Proxy VPS trên AWS EC2 là một bước quan trọng để giảm độ trễ (latency) và tăng tốc độ tải dữ liệu, đặc biệt là với các ứng dụng tiêu tốn băng thông và nhạy cảm về độ trễ như TikTok.

Dưới đây là các giải pháp tối ưu hóa từ mức độ hệ điều hành đến cấu hình phần mềm mà bạn nên áp dụng:

---

## 1. Kích hoạt TCP BBR (Bottleneck Bandwidth and RTT)

Đây là bước **quan trọng nhất** trên Ubuntu. BBR là thuật toán kiểm soát tắc nghẽn do Google phát triển, giúp tăng đáng kể băng thông và giảm độ trễ trên các kết nối có tỉ lệ mất gói tin (packet loss).

**Cách thực hiện:**

1. Kiểm tra xem BBR đã bật chưa:
   ```bash
   sysctl net.ipv4.tcp_congestion_control
   ```
2. Nếu chưa phải là `bbr`, hãy thêm các dòng sau vào file `/etc/sysctl.conf`:
   ```text
   net.core.default_qdisc=fq
   net.ipv4.tcp_congestion_control=bbr
   ```
3. Lưu lại và áp dụng: `sudo sysctl -p`

---

## 2. Tối ưu hóa các thông số Kernel Linux

Mặc định, Ubuntu không được tối ưu cho các tác vụ làm Proxy với số lượng kết nối lớn. Bạn nên điều chỉnh các giới hạn hệ thống trong `/etc/sysctl.conf`:

- **Tăng giới hạn file mở (File Descriptors):** Mỗi kết nối qua Dante được tính là một file.
- **Tối ưu dải cổng (Port Range):** Mở rộng số lượng cổng khả dụng để tránh tình trạng nghẽn kết nối.
- **Tối ưu Buffer:** Tăng kích thước bộ đệm TCP cho các kết nối đường dài.

**Các dòng thông số gợi ý thêm vào `/etc/sysctl.conf`:**

```text
fs.file-max = 1000000
net.core.somaxconn = 4096
net.ipv4.tcp_max_syn_backlog = 8192
net.ipv4.tcp_slow_start_after_idle = 0
net.ipv4.tcp_tw_reuse = 1
net.ipv4.ip_local_port_range = 1024 65535
```

---

## 3. Cấu hình Dante (danted.conf) tối ưu

Dante có thể chạy nhanh hơn nếu bạn tinh chỉnh cách nó xử lý các luồng (threads) và phương thức kiểm tra:

- **Sử dụng nhiều worker:** Tùy vào số CPU của gói EC2, hãy tăng số lượng `workers`.
  ```text
  # Ví dụ với VPS 2-4 vCPU
  workers: 4
  ```
- **Tắt log không cần thiết:** Việc ghi log mọi kết nối sẽ làm chậm quá trình xử lý I/O. Chỉ nên log các lỗi nghiêm trọng.
  ```text
  # logoutput: stderr  # Tắt log vào file nếu không cần debug
  ```

---

## 4. Sử dụng Tunneling thay vì Proxy "trần" (OBC)

Một vấn đề phổ biến là các nhà mạng (ISP) tại Việt Nam có thể bóp băng thông (throttling) các kết nối SOCKS5 truyền thống nếu họ nhận diện được giao thức qua DPI (Deep Packet Inspection).

**Giải pháp:** Thay vì kết nối trực tiếp từ thiết bị đến Dante, bạn có thể thiết lập một đường truyền mã hóa như **Shadowsocks** hoặc **V2Ray (VLESS/VMess)**.

- **Cấu trúc mới:** Thiết bị $\rightarrow$ Tunnel (Mã hóa) $\rightarrow$ VPS $\rightarrow$ Dante/Socks5 $\rightarrow$ TikTok.
- Việc này giúp dữ liệu đi qua lớp kiểm soát của ISP một cách trơn tru hơn, tránh bị bóp tốc độ vào giờ cao điểm.

---

## 5. Lựa chọn Vị trí địa lý (Location)

Tốc độ từ thiết bị của bạn đến Proxy phụ thuộc rất lớn vào khoảng cách vật lý:

- Nếu bạn ở Việt Nam, hãy ưu tiên các Region của AWS tại **Singapore (ap-southeast-1)** hoặc **Hong Kong (ap-east-1)**.
- Nếu Proxy ở Mỹ hoặc Châu Âu, độ trễ $RTT$ (Round Trip Time) chắc chắn sẽ cao (thường > 200ms), gây hiện tượng giật lag khi lướt TikTok.

---

## 6. Điều chỉnh MTU (Maximum Transmission Unit)

Đôi khi việc gói tin bị phân mảnh do sai lệch MTU giữa thiết bị của bạn và AWS EC2 sẽ làm giảm tốc độ.

- Thử giảm MTU trên interface mạng của VPS xuống mức **1400** hoặc **1450** thay vì 1500 mặc định để kiểm tra xem độ ổn định có cải thiện không.
  ```bash
  sudo ifconfig eth0 mtu 1450 up
  ```

**Lời khuyên:** Bạn nên bắt đầu với **Bước 1 (BBR)** và **Bước 5 (Vị trí)** trước, vì đây là hai yếu tố mang lại sự khác biệt rõ rệt nhất ngay lập tức.
