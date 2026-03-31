**Cách tối ưu đường truyền từ thiết bị của bạn (HCMC, VN) → Proxy VPS (Dante trên EC2 Ubuntu)** là tập trung giảm **latency (RTT)** và tăng **throughput** trên đoạn đầu tiên (client → proxy). Đoạn sau (proxy → TikTok server) do AWS xử lý tốt rồi.

Dưới đây là các cách hiệu quả nhất, xếp theo mức độ cải thiện (từ cao nhất):

### 1. Chuyển EC2 sang Region gần nhất: **ap-southeast-1 (Singapore)**

Đây là region gần Việt Nam nhất hiện tại (2026). AWS chưa có Region chính thức ở VN, chỉ có **Local Zone Hanoi** (ap-southeast-1-han-1a) – nhưng Hanoi cách HCMC ~1.100–1.300 km, Singapore gần HCMC hơn về khoảng cách mạng và routing thực tế.

- **Hiệu quả**: Giảm latency từ 100–300ms (nếu bạn đang ở US/EU) xuống còn **30–60ms**.
- **Cách làm**:
  1. Tạo snapshot AMI của instance hiện tại.
  2. Launch instance mới ở **ap-southeast-1**.
  3. Cài lại Dante (hoặc restore config `/etc/sockd.conf`).
  4. Cập nhật IP proxy trên thiết bị của bạn.

Nếu bạn đang ở region xa → đây là thay đổi lớn nhất, miễn phí (chỉ tốn data transfer khi migrate).

### 2. Dùng **AWS Global Accelerator** (Khuyến nghị mạnh nhất – cải thiện 40–60%)

Đây là cách tối ưu “đường truyền internet” mà không cần đổi VPS. Traffic từ thiết bị bạn sẽ:

- Vào **anycast IP** của GA (edge location gần VN nhất, thường Singapore).
- Đi qua **backbone AWS** (siêu nhanh, ít congestion).
- Đến EC2 của bạn.

Kết quả: latency ổn định hơn, jitter thấp, throughput cao hơn rất nhiều so với public IP EC2 thông thường.

- **Hỗ trợ**: Hoàn toàn tương thích với Dante (TCP port 1080, SOCKS5).
- **Cách triển khai nhanh** (khoảng 10–15 phút):
  1. Vào AWS Console → Global Accelerator → Create accelerator.
  2. Thêm **Listener**: TCP, port 1080 (hoặc range 1080-1080).
  3. Thêm **Endpoint Group**: Chọn region ap-southeast-1.
  4. Thêm **Endpoint**: Chọn EC2 instance của bạn (weight 100, preserve client IP nếu muốn).
  5. Copy 2 static IP của Accelerator → thay thế IP cũ trong config proxy trên thiết bị.

Sau khi active, bạn chỉ cần trỏ proxy sang IP của Global Accelerator (giữ nguyên port 1080). Không cần thay đổi Dante.

### 3. Chọn Instance type có bandwidth cao + Enable Enhanced Networking

- Tránh **t3/t4.micro** (bandwidth chỉ ~1–5 Gbps, dễ nghẽn khi xem TikTok).
- Dùng: **c6i.large / m6i.large / c5.large** (10–25 Gbps, hỗ trợ ENA).

### 4. Tune TCP trên Ubuntu (server side – miễn phí & hiệu quả rõ)

Chạy các lệnh sau trên EC2:

```bash
# Bật BBR (congestion control tốt nhất hiện nay)
sudo modprobe tcp_bbr
echo "net.core.default_qdisc = fq" | sudo tee -a /etc/sysctl.conf
echo "net.ipv4.tcp_congestion_control = bbr" | sudo tee -a /etc/sysctl.conf

# Tăng buffer (rất quan trọng cho streaming)
echo "net.core.rmem_max = 16777216" | sudo tee -a /etc/sysctl.conf
echo "net.core.wmem_max = 16777216" | sudo tee -a /etc/sysctl.conf
echo "net.ipv4.tcp_rmem = 4096 87380 16777216" | sudo tee -a /etc/sysctl.conf
echo "net.ipv4.tcp_wmem = 4096 65536 16777216" | sudo tee -a /etc/sysctl.conf

sudo sysctl -p
```

Sau đó restart Dante:

```bash
sudo systemctl restart danted
```

### 5. Các tối ưu nhỏ khác

- **Security Group**: Chỉ mở port 1080 từ IP của bạn (hoặc /32) → tránh scan.
- **MTU**: Đặt MTU 9001 trên network interface EC2 (default của AWS).
- **Trên thiết bị**:
  - Dùng Proxifier (Windows) / Socks5 proxy app (Android) hỗ trợ UDP associate (Dante hỗ trợ).
  - Test latency: `ping <proxy_ip>` hoặc dùng tool như `tcping` port 1080.
- Nếu TikTok vẫn chậm: Dante là SOCKS → overhead hơi cao. Nhiều người chuyển sang **WireGuard** trên cùng VPS (UDP, latency thấp hơn, dễ config hơn cho streaming).

### Tóm tắt thứ tự làm (tăng tốc nhanh nhất)

1. Chuyển region → ap-southeast-1 (nếu chưa).
2. Thêm Global Accelerator (cải thiện lớn nhất).
3. Đổi instance type + tune BBR.
