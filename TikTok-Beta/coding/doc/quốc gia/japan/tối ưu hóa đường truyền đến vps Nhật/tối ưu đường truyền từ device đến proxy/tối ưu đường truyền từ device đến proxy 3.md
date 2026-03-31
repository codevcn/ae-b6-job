Bạn đang đi đúng hướng rồi — bottleneck thường nằm ở đoạn **device → proxy VPS**, không phải từ VPS → TikTok (vì AWS khá mạnh). Muốn tối ưu đoạn này, bạn cần giảm **latency + packet loss + overhead**. Dưới đây là các cách hiệu quả nhất (ưu tiên từ dễ → nâng cao):

---

## 1. Chọn region AWS gần bạn nhất (cực kỳ quan trọng)

Nếu VPS không gần Việt Nam thì mọi tối ưu khác gần như vô nghĩa.

👉 Nên dùng:

- **ap-southeast-1 (Singapore)** → tốt nhất cho VN
- **ap-east-1 (Hong Kong)** → cũng ổn

❌ Tránh:

- US, EU (ping cao → lag ngay)

📌 Test nhanh:

```bash
ping <ip-vps>
```

- < 50ms → tốt
- 50–100ms → chấp nhận
- > 100ms → nên đổi region

---

## 2. Đổi giao thức proxy (Dante SOCKS5 chưa phải tối ưu nhất)

Dante (SOCKS5) ổn nhưng **không tối ưu cho tốc độ + ổn định mobile network**.

👉 Nâng cấp lên:

### 🔥 Option tốt hơn:

- **Shadowsocks (SS)** → nhẹ, nhanh, ổn định
- **V2Ray (VMess/VLESS)** → linh hoạt hơn
- **WireGuard (VPN)** → nhanh nhất (khuyên dùng nếu bạn control cả 2 đầu)

📊 So sánh nhanh:

| Protocol    | Speed      | Stability | Latency    |
| ----------- | ---------- | --------- | ---------- |
| SOCKS5      | Trung bình | OK        | Trung bình |
| Shadowsocks | Nhanh      | Tốt       | Thấp       |
| WireGuard   | Rất nhanh  | Rất tốt   | Rất thấp   |

👉 Nếu mục tiêu là TikTok → **WireGuard = best choice**

---

## 3. Bật TCP BBR trên VPS (tăng throughput rõ rệt)

Ubuntu trên EC2 có thể chưa bật.

👉 Check:

```bash
sysctl net.ipv4.tcp_congestion_control
```

👉 Nếu chưa phải `bbr` thì bật:

```bash
echo "net.core.default_qdisc=fq" >> /etc/sysctl.conf
echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.conf
sysctl -p
```

📌 Hiệu quả:

- Tăng tốc độ tải
- Giảm nghẽn mạng
- Rất hữu ích khi mạng VN → AWS

---

## 4. Tối ưu MTU (giảm fragmentation)

Sai MTU → packet bị chia nhỏ → chậm.

👉 Test MTU:

```bash
ping -M do -s 1472 <ip-vps>
```

👉 Nếu fail → giảm dần (1460, 1450…)

👉 Sau đó set:

```bash
ip link set dev eth0 mtu 1450
```

---

## 5. Dùng UDP thay vì TCP (nếu có thể)

TikTok dùng nhiều UDP (video streaming).

👉 Dante chủ yếu TCP → hạn chế
👉 WireGuard / Shadowsocks hỗ trợ UDP → mượt hơn

---

## 6. Giảm hop mạng (routing)

Đôi khi ISP VN route đi vòng → lag.

👉 Cách check:

```bash
traceroute <ip-vps>
```

👉 Nếu hop > 15 hoặc đi vòng quốc tế → thử:

- đổi mạng (4G vs WiFi)
- đổi ISP (VNPT, Viettel, FPT)

---

## 7. Bật keepalive + tối ưu Dante (nếu vẫn dùng)

Trong config Dante:

```conf
tcp.connecttimeout: 5
tcp.keepalive: yes
```

---

## 8. Dùng instance AWS có network tốt hơn

Không phải EC2 nào cũng giống nhau.

👉 Nên dùng:

- t3.small trở lên
- hoặc **c6g / c7g (Graviton)** → network tốt + rẻ

---

## 9. Bật ENA (Elastic Network Adapter)

👉 Check:

```bash
ethtool -i eth0
```

Nếu chưa có ENA → performance bị bóp.

---

## 10. Tối ưu phía device (ít ai để ý)

- Dùng mạng **WiFi ổn định hơn 4G**
- Tắt app chạy nền
- Nếu Android → dùng app proxy tốt (Shadowrocket, V2RayNG…)

---

## Kết luận (quan trọng nhất)

Nếu bạn chỉ làm 3 thứ này thôi đã khác biệt lớn:

1. ✔ Chuyển VPS sang **Singapore**
2. ✔ Đổi từ Dante → **WireGuard hoặc Shadowsocks**
3. ✔ Bật **BBR**
