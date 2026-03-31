Đây là bài toán **giảm latency + tăng throughput** trên đoạn `my device → proxy VPS`. Có vài hướng:

---

## 1. Tối ưu giao thức truyền tải

### QUIC / UDP thay vì TCP

Mặc định SOCKS5/HTTP proxy chạy trên TCP. Có thể dùng tunnel chạy trên UDP để giảm latency:

- **WireGuard** — nhẹ, latency thấp, chạy trên UDP
- **TUIC** — proxy protocol chạy trên QUIC (UDP), chống TCP head-of-line blocking

### TCP tuning trên VPS

```bash
# /etc/sysctl.conf
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
net.ipv4.tcp_congestion_control = bbr   # BBR thay vì CUBIC
net.ipv4.tcp_fastopen = 3               # Giảm RTT khi mở connection
```

```bash
sudo sysctl -p
```

**BBR** đặc biệt hiệu quả khi đường truyền có **packet loss** hoặc **latency cao** (như từ VN đến AWS).

---

## 2. Chọn đúng AWS Region

Nếu VPS đang ở region xa (us-east-1 chẳng hạn), đây là yếu tố lớn nhất ảnh hưởng latency. Region gần VN nhất:

| Region                     | Latency từ HCM (ước tính) |
| -------------------------- | ------------------------- |
| ap-southeast-1 (Singapore) | ~30ms                     |
| ap-northeast-1 (Tokyo)     | ~70ms                     |
| us-east-1 (N. Virginia)    | ~200ms+                   |

---

## 3. Nén dữ liệu trên tunnel

Nếu bạn đang dùng SSH tunnel hoặc VPN, bật compression:

```bash
# SSH tunnel
ssh -C -D 1080 user@vps  # -C = enable compression
```

Tuy nhiên với HTTPS traffic (TikTok dùng HTTPS) thì **nén gần như vô tác dụng** vì data đã được encrypt + compress sẵn.

---

## 4. Connection pooling / Keep-alive

Dante mặc định không giữ connection. Có thể đặt một **reverse proxy nhẹ** (như Nginx hoặc HAProxy) trước Dante để:

- Keep-alive connection giữa device và VPS
- Giảm overhead TCP handshake mỗi request

---

## 5. Phía thiết bị của bạn

- **Dùng SOCKS5 thay vì HTTP proxy** — ít overhead hơn, không cần parse HTTP header
- **Tránh proxy toàn bộ traffic** — chỉ route TikTok qua proxy (split tunneling), giảm tải cho VPS và giảm latency cho các traffic khác

---

## Ưu tiên thực tế

```
1. AWS Region gần (Singapore)     ← tác động lớn nhất
2. Bật BBR                        ← dễ làm, hiệu quả rõ
3. SOCKS5 thay HTTP proxy         ← nếu chưa dùng
4. Split tunneling                ← chỉ route TikTok qua proxy
```
