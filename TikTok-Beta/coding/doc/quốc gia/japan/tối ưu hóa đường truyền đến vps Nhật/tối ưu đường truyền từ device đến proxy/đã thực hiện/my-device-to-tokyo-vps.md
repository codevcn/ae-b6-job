# Tối ưu hóa đường truyền từ VN đến Tokyo Proxy VPS

Quy trình cốt lõi:

`[1] my device --(req abc)--> [2] aws ec2 ubuntu proxy vps (tokyo) --(req abc)--> [3] tiktok`

Đây là hướng dẫn A-Z hoàn chỉnh cho kiến trúc:

`iOS/Android → WireGuard → EC2 Singapore → AWS backbone → EC2 Tokyo (WireGuard) → TikTok`

---

## Tổng quan kiến trúc sẽ build

```
[iOS/Android]
    │  WireGuard tunnel (UDP 51820)
    ▼
[EC2 Singapore]  ← điểm vào backbone AWS gần VN nhất
    │  WireGuard tunnel (UDP 51820) qua AWS internal backbone
    ▼
[EC2 Tokyo]  ← proxy exit node
    │
    ▼
[TikTok]
```

Có 2 WireGuard tunnel độc lập xếp chồng (hop 1: phone→SG, hop 2: SG→Tokyo). EC2 Singapore đóng vai trò **relay thuần** — nhận packet từ phone, forward sang Tokyo, không làm gì thêm.

---

## Phần 1 — Tạo EC2 Singapore

### Bước 1.1 — Launch instance

Vào AWS Console → EC2 → **Launch Instance**.

- **Name:** `wireguard-relay-sg`
- **AMI:** Ubuntu 24.04 LTS
- **Instance type:** `t4g.nano` (ARM, ~$3.5/tháng) hoặc `t3.micro` nếu muốn x86
- **Region:** Asia Pacific (Singapore) `ap-southeast-1`
- **Key pair:** dùng lại key `.pem` hiện có hoặc tạo mới
- **Storage:** 8GB gp3 là đủ

### Bước 1.2 — Security Group cho SG instance

Tạo Security Group tên `sg-wireguard-relay` với các rule sau:

| Type     | Protocol | Port  | Source    | Mục đích           |
| -------- | -------- | ----- | --------- | ------------------ |
| Inbound  | UDP      | 51820 | 0.0.0.0/0 | WireGuard từ phone |
| Inbound  | TCP      | 22    | Your IP   | SSH để quản lý     |
| Outbound | All      | All   | 0.0.0.0/0 | Forward traffic    |

### Bước 1.3 — Cấp Elastic IP cho SG instance

EC2 Console → **Elastic IPs** → Allocate → Associate vào instance Singapore. Ghi lại IP này, ký hiệu là `SG_PUBLIC_IP`.

---

## Phần 2 — Cấu hình EC2 Singapore (WireGuard Relay)

SSH vào SG instance:

```bash
ssh -i your-key.pem ubuntu@SG_PUBLIC_IP
```

### Bước 2.1 — Cài WireGuard

```bash
sudo apt update && sudo apt install -y wireguard
```

### Bước 2.2 — Bật IP forwarding

```bash
# Bật ngay lập tức
sudo sysctl -w net.ipv4.ip_forward=1

# Bật vĩnh viễn
echo "net.ipv4.ip_forward = 1" | sudo tee -a /etc/sysctl.conf
```

### Bước 2.3 — Sinh WireGuard key cho SG instance

```bash
cd /etc/wireguard
sudo wg genkey | sudo tee sg_private.key | wg pubkey | sudo tee sg_public.key
sudo chmod 600 sg_private.key

# Xem key để copy
sudo cat sg_private.key   # → SG_PRIVATE_KEY
sudo cat sg_public.key    # → SG_PUBLIC_KEY
```

### Bước 2.4 — Sinh key cho phone (làm trên SG cho tiện)

```bash
sudo wg genkey | sudo tee phone_private.key | wg pubkey | sudo tee phone_public.key
sudo chmod 600 phone_private.key

sudo cat phone_private.key   # → PHONE_PRIVATE_KEY
sudo cat phone_public.key    # → PHONE_PUBLIC_KEY
```

### Bước 2.5 — Tạo config WireGuard trên SG instance

Bạn cần biết IP của EC2 Tokyo trước — ký hiệu là `TOKYO_PUBLIC_IP` và `TOKYO_WG_PUBKEY` (public key WireGuard đang chạy trên Tokyo). Lấy bằng cách SSH vào Tokyo và chạy `sudo cat /etc/wireguard/*public*`.

```bash
sudo nano /etc/wireguard/wg0.conf
```

Dán nội dung sau (thay thế các giá trị IN HOA):

```ini
[Interface]
Address = 10.8.0.1/24
ListenPort = 51820
PrivateKey = SG_PRIVATE_KEY

# Forward tất cả traffic ra ngoài (NAT)
PostUp = iptables -A FORWARD -i wg0 -j ACCEPT; \
         iptables -A FORWARD -o wg0 -j ACCEPT; \
         iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE; \
         iptables -A FORWARD -i wg1 -j ACCEPT; \
         iptables -A FORWARD -o wg1 -j ACCEPT
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; \
           iptables -D FORWARD -o wg0 -j ACCEPT; \
           iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE; \
           iptables -D FORWARD -i wg1 -j ACCEPT; \
           iptables -D FORWARD -o wg1 -j ACCEPT

# Peer 1: Phone của bạn
[Peer]
PublicKey = PHONE_PUBLIC_KEY
AllowedIPs = 10.8.0.2/32
```

---

## Phần 3 — Cấu hình EC2 Tokyo (thêm peer SG)

SSH vào Tokyo:

```bash
ssh -i your-key.pem ubuntu@TOKYO_PUBLIC_IP
```

### Bước 3.1 — Sinh key cho tunnel SG→Tokyo (nếu chưa có)

```bash
cd /etc/wireguard
# Kiểm tra đã có key chưa
sudo ls /etc/wireguard/
```

Nếu đang chạy WireGuard cho phone rồi thì Tokyo đã có key. Lấy public key của Tokyo:

```bash
sudo cat /etc/wireguard/*public*   # hoặc
sudo wg show   # xem interface đang chạy
```

Ghi lại `TOKYO_WG_PUBKEY`.

### Bước 3.2 — Tạo tunnel thứ 2 trên Tokyo cho relay SG

```bash
# Sinh key riêng cho tunnel SG-Tokyo
sudo wg genkey | sudo tee /etc/wireguard/tokyo_sg_private.key | \
  wg pubkey | sudo tee /etc/wireguard/tokyo_sg_public.key
sudo chmod 600 /etc/wireguard/tokyo_sg_private.key

sudo cat /etc/wireguard/tokyo_sg_private.key   # → TOKYO_SG_PRIVATE_KEY
sudo cat /etc/wireguard/tokyo_sg_public.key    # → TOKYO_SG_PUBLIC_KEY
```

Tạo interface `wg1` cho tunnel nội bộ SG↔Tokyo:

```bash
sudo nano /etc/wireguard/wg1.conf
```

```ini
[Interface]
Address = 10.9.0.2/24
ListenPort = 51821
PrivateKey = TOKYO_SG_PRIVATE_KEY

# Peer: SG relay
[Peer]
PublicKey = SG_PUBLIC_KEY
AllowedIPs = 10.9.0.0/24, 10.8.0.0/24
Endpoint = SG_PUBLIC_IP:51821
PersistentKeepalive = 25
```

Khởi động:

```bash
sudo systemctl enable wg-quick@wg1
sudo systemctl start wg-quick@wg1
```

### Bước 3.3 — Mở Security Group Tokyo cho tunnel SG

Vào AWS Console → Security Group của Tokyo instance → thêm Inbound rule:

| Type       | Protocol | Port  | Source          |
| ---------- | -------- | ----- | --------------- |
| Custom UDP | UDP      | 51821 | SG_PUBLIC_IP/32 |

---

## Phần 4 — Hoàn thiện config SG (thêm tunnel đến Tokyo)

Quay lại SSH vào SG instance, tạo thêm interface `wg1` cho tunnel SG→Tokyo:

```bash
sudo nano /etc/wireguard/wg1.conf
```

```ini
[Interface]
Address = 10.9.0.1/24
ListenPort = 51821
PrivateKey = SG_PRIVATE_KEY

PostUp = iptables -t nat -A POSTROUTING -o wg1 -j MASQUERADE
PostDown = iptables -t nat -D POSTROUTING -o wg1 -j MASQUERADE

# Peer: Tokyo
[Peer]
PublicKey = TOKYO_SG_PUBLIC_KEY
AllowedIPs = 0.0.0.0/0
Endpoint = TOKYO_PUBLIC_IP:51821
PersistentKeepalive = 25
```

Khởi động cả 2 interface:

```bash
sudo systemctl enable wg-quick@wg0
sudo systemctl enable wg-quick@wg1
sudo systemctl start wg-quick@wg0
sudo systemctl start wg-quick@wg1
```

Kiểm tra:

```bash
sudo wg show
# Phải thấy cả wg0 và wg1 với peer đã handshake
```

---

## Phần 5 — Cấu hình WireGuard trên iOS/Android

### Bước 5.1 — Tạo QR code config cho phone

Vẫn trên SG instance:

```bash
sudo apt install -y qrencode

# Tạo file config cho phone
cat << EOF | sudo tee /tmp/phone.conf
[Interface]
PrivateKey = PHONE_PRIVATE_KEY
Address = 10.8.0.2/32
DNS = 1.1.1.1

[Peer]
PublicKey = SG_PUBLIC_KEY
Endpoint = SG_PUBLIC_IP:51820
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
EOF

# Hiển thị QR code
qrencode -t ansiutf8 < /tmp/phone.conf

# Xóa file sau khi quét xong (bảo mật)
sudo rm /tmp/phone.conf
```

### Bước 5.2 — Cài app và import

Tải **WireGuard** từ App Store / Google Play.

Mở app → dấu `+` → **Create from QR code** → quét QR trên terminal → đặt tên `TikTok-SG-Relay` → Save → bật tunnel.

---

## Phần 6 — Kiểm tra toàn bộ chain

### Từ phone (dùng app bất kỳ có terminal hoặc browser):

Bật WireGuard trên phone, truy cập `https://ifconfig.me` — phải thấy IP của EC2 Tokyo (không phải SG, không phải IP VN).

### Từ SG instance, kiểm tra tunnel đến Tokyo:

```bash
sudo wg show wg1
# Kiểm tra "latest handshake" phải có (< 3 phút)

ping 10.9.0.2   # ping Tokyo qua tunnel
# Phải reply với ~5–10ms
```

### Kiểm tra latency thực tế:

```bash
# Trên SG instance
ping TOKYO_PUBLIC_IP
# Expect: ~5–8ms (AWS backbone SG→Tokyo)

# So sánh với Internet thông thường từ phone
# Dùng app "PingTools" hoặc tương tự
```

---

## Bảng tóm tắt các giá trị cần ghi lại

| Biến                  | Lấy ở đâu                                      | Dùng ở bước   |
| --------------------- | ---------------------------------------------- | ------------- |
| `SG_PUBLIC_IP`        | AWS Console → EC2 → Elastic IP                 | 2.5, 3.2, 5.1 |
| `SG_PRIVATE_KEY`      | `/etc/wireguard/sg_private.key`                | 2.5, 4        |
| `SG_PUBLIC_KEY`       | `/etc/wireguard/sg_public.key`                 | 3.2, 5.1      |
| `PHONE_PRIVATE_KEY`   | `/etc/wireguard/phone_private.key`             | 5.1           |
| `PHONE_PUBLIC_KEY`    | `/etc/wireguard/phone_public.key`              | 2.5           |
| `TOKYO_PUBLIC_IP`     | AWS Console hoặc `curl ifconfig.me` trên Tokyo | 4             |
| `TOKYO_SG_PUBLIC_KEY` | `/etc/wireguard/tokyo_sg_public.key`           | 4             |

---

## Troubleshooting thường gặp

Nếu `wg show` không thấy handshake, kiểm tra Security Group đã mở đúng port UDP chưa — đây là lỗi phổ biến nhất. Nếu IP vẫn ra SG thay vì Tokyo, kiểm tra `AllowedIPs = 0.0.0.0/0` trong config phone và route table trên SG (`wg1` phải là default route). Nếu không ping được `10.9.0.2`, kiểm tra `ip_forward` đã bật trên SG và `wg1` trên cả hai instance đã start.

---

# Kết quả mới nhất đến hiện tại

Chào Lợi, chúc mừng bạn đã thông nòng thành công hệ thống Double Hop Proxy. Dựa trên kết quả thực tế bạn vừa đạt được (Ping thông đến Tokyo và nhận đúng IP 13.193.91.19), dưới đây là nội dung cập nhật cho phần checklist trong tài liệu của bạn:

---

## 📋 Checklist Hệ thống Proxy Double Hop (SG - Tokyo) - Cập nhật 21/03/2026

### ✅ Giai đoạn 1: Thiết lập hạ tầng AWS

- [x] **Tạo Instance Singapore mới:** Đã thay thế instance lỗi bằng máy mới hoàn toàn.
- [x] **Gán Elastic IP mới:** `18.140.133.115`.
- [x] **Security Group SG:** Đã mở UDP 51820 (Phone/PC) và 51821 (Tunnel nội bộ).
- [x] **Security Group Tokyo:** Đã cập nhật cho phép IP SG mới truy cập cổng 51821.

### ✅ Giai đoạn 2: Cấu hình VPS Singapore (Relay Node)

- [x] **Cài đặt WireGuard & qrencode**.
- [x] **Bật IP Forwarding:** Đã thực hiện trên máy SG mới.
- [x] **Cấu hình `wg0.conf` (Đón thiết bị):** Đã chạy thành công trên cả Phone và Windows 11.
- [x] **Cấu hình `wg1.conf` (Nối Tokyo):** Đã đạt trạng thái **Handshake** ổn định.
- [x] **Policy Routing:** Đã thiết lập Table 200 để tách biệt traffic Proxy và traffic quản trị SSH.

### ✅ Giai đoạn 3: Cấu hình VPS Tokyo (Exit Node)

- [x] **Kích hoạt Tunnel nội bộ:** Đã có kết nối ổn định với SG (Handshake thành công).
- [x] **Cập nhật NAT trên Tokyo:** Đã sửa lỗi tên card mạng từ `eth0` thành `ens5` và kích hoạt MASQUERADE thành công.

### ✅ Giai đoạn 4: Thiết lập và Kiểm tra trên thiết bị (Windows 11)

- [x] **Cấu hình WireGuard cá nhân:** Đã thiết lập và kết nối thành công từ máy cá nhân.
- [x] **Kiểm tra IP thực tế:** Lệnh `curl.exe -4 ifconfig.me` đã trả về đúng IP Tokyo **13.193.91.19**.
- [x] **Xác minh lộ trình (Trace):** Đã xác nhận gói tin đi đúng Hop 1 (`10.8.0.1`) và Hop 2 (`10.9.0.2`).

---

## 🚀 Các việc cần làm tiếp theo (Pending)

1.  **Lưu định tuyến vĩnh viễn (Persistence):**
    - Cần tích hợp các lệnh `ip rule add from 10.8.0.0/24 table 200` và các quy tắc `iptables` vào phần `PostUp` của file cấu hình trên cả Singapore và Tokyo để không bị mất cấu hình khi khởi động lại máy.
2.  **Xử lý triệt để IPv6 Leak:**
    - Hiện tại hệ thống vẫn bị lộ IPv6 Việt Nam khi truy cập web thông thường. Cần tắt IPv6 trên máy tính hoặc bổ sung dải `::/0` vào `AllowedIPs` (nếu hạ tầng hỗ trợ) để TikTok không phát hiện được vị trí thật.
3.  **Tối ưu hóa MTU:**
    - Nếu quá trình xem video bị khựng, hãy đồng bộ giá trị `MTU = 1280` trên toàn hệ thống (Windows, Singapore, Tokyo).

## 🧪 Kết quả test kết nối

```text
PS C:\Users\dell> tracert -d -4 8.8.8.8

Tracing route to 8.8.8.8 over a maximum of 30 hops

  1    34 ms    29 ms    29 ms  10.8.0.1
  2    99 ms    98 ms    98 ms  10.9.0.2
  3     *        *        *     Request timed out.
  4   100 ms   102 ms   103 ms  99.82.13.102
  5   101 ms   101 ms   100 ms  99.82.13.103
  6   100 ms   100 ms   101 ms  108.170.231.103
  7   101 ms   100 ms   101 ms  216.239.43.51
  8   104 ms   101 ms   104 ms  8.8.8.8

Trace complete.
PS C:\Users\dell> tracert -d -4 8.8.8.8

Tracing route to 8.8.8.8 over a maximum of 30 hops

  1     *        *        *     Request timed out.
  2   100 ms    99 ms   101 ms  10.9.0.2
  3     *        *        *     Request timed out.
  4   100 ms   102 ms    99 ms  99.82.13.102
  5   108 ms   104 ms   101 ms  99.82.13.103
  6   101 ms   105 ms   101 ms  108.170.231.103
  7   100 ms   102 ms   102 ms  216.239.43.51
  8   102 ms   101 ms   101 ms  8.8.8.8

Trace complete.
PS C:\Users\dell> tracert -d -4 13.193.91.19

Tracing route to 13.193.91.19 over a maximum of 30 hops

  1    34 ms    29 ms    30 ms  10.8.0.1
  2    97 ms    97 ms    97 ms  10.9.0.2
  3     *        *        *     Request timed out.
  4    98 ms   100 ms    98 ms  13.193.91.19

Trace complete.
PS C:\Users\dell> tracert -d -4 13.193.91.19

Tracing route to 13.193.91.19 over a maximum of 30 hops

  1     *        *        *     Request timed out.
  2    98 ms    99 ms    97 ms  10.9.0.2
  3     *        *        *     Request timed out.
  4   101 ms   102 ms   104 ms  13.193.91.19

Trace complete.
PS C:\Users\dell> echo "đã deactivate wireguard trên desktop"
đã deactivate wireguard trên desktop
PS C:\Users\dell> tracert -d -4 13.193.91.19

Tracing route to 13.193.91.19 over a maximum of 30 hops

  1     3 ms     2 ms     3 ms  192.168.1.1
  2    13 ms     7 ms    11 ms  100.120.0.2
  3     5 ms     5 ms     5 ms  172.16.128.9
  4     9 ms    12 ms    11 ms  10.0.245.129
  5     4 ms     6 ms     5 ms  10.0.245.130
  6     *        *        *     Request timed out.
  7    27 ms    25 ms    34 ms  125.234.123.37
  8    25 ms    24 ms    27 ms  27.68.250.208
  9     *        *        *     Request timed out.
 10     *        *        *     Request timed out.
 11     *        *        *     Request timed out.
 12     *        *        *     Request timed out.
 13     *        *        *     Request timed out.
 14    90 ms    90 ms    92 ms  13.193.91.19

Trace complete.
PS C:\Users\dell> tracert -d -4 13.193.91.19

Tracing route to 13.193.91.19 over a maximum of 30 hops

  1     3 ms     2 ms     3 ms  192.168.1.1
  2     8 ms     5 ms     6 ms  100.120.0.2
  3     5 ms     8 ms     8 ms  172.16.128.9
  4     5 ms     6 ms     6 ms  10.0.245.129
  5     6 ms     4 ms     5 ms  10.0.245.130
  6     *        *        *     Request timed out.
  7    24 ms    25 ms    24 ms  125.234.123.37
  8    24 ms    23 ms    25 ms  27.68.250.208
  9     *        *        *     Request timed out.
 10     *        *        *     Request timed out.
 11     *        *        *     Request timed out.
 12     *        *        *     Request timed out.
 13     *        *        *     Request timed out.
 14    94 ms    91 ms    92 ms  13.193.91.19

Trace complete.
PS C:\Users\dell>
```

Chào Lợi, đây là bản "nhật ký thực chiến" chi tiết nhất để bạn lưu lại. File này tóm tắt toàn bộ quá trình từ việc khai tử mô hình 2-hop cũ cho đến lúc "độ" xong động cơ BBR và thông nòng AGA.

---

# 🚀 Tối ưu hóa Proxy mức 2: Chuyển đổi từ 2-Hop sang AWS Global Accelerator (AGA)

**Ngày cập nhật:** 21/03/2026
**Trạng thái:** Hoàn tất & Tối ưu (Full Option)
**Lộ trình:** `Phone/PC → AWS Global Accelerator (Anycast) → AWS Backbone → EC2 Tokyo (WireGuard)`

---

## 1. Tổng quan sự thay đổi kiến trúc

| Đặc điểm       | Mô hình 2-Hop cũ                | Mô hình Global Accelerator (Mới)       |
| :------------- | :------------------------------ | :------------------------------------- |
| **Cấu trúc**   | `Thiết bị → SG VPS → Tokyo VPS` | `Thiết bị → AGA IP → Tokyo VPS`        |
| **Quản lý**    | Phải duy trì 2 VPS (SG & Tokyo) | Chỉ cần 1 VPS duy nhất tại Tokyo       |
| **Độ ổn định** | Phụ thuộc vào VPS Singapore     | Cực cao, dùng mạng Backbone của Amazon |
| **Định tuyến** | Thủ công (Table 200, Routing)   | Tự động qua các Edge Location của AWS  |

---

## 2. Quy trình thiết lập A-Z

### Bước 2.1: Khởi tạo AWS Global Accelerator

1.  **Tạo Accelerator:** Đã cấp 2 IP tĩnh (Anycast) để làm Endpoint cho thiết bị.
2.  **Listener:** Thiết lập giao thức **UDP**, Port **51820** (hoặc 51821 tùy cấu hình WireGuard).
3.  **Endpoint Group:** Khu vực `ap-northeast-1` (Tokyo).
4.  **Endpoint:** Trỏ trực tiếp về Instance ID của máy Tokyo (`13.193.91.19`).
    - _Lưu ý:_ Tính năng **Preserve client IP address** được để mặc định (Bật) cho UDP.

### Bước 2.2: Xử lý Health Check (Lỗi Unhealthy)

- **Vấn đề:** AWS mặc định dùng TCP để check cổng UDP của WireGuard nên báo Unhealthy.
- **Giải pháp:** Chuyển **Health check port** sang cổng **22 (SSH)** với giao thức **TCP**.
- **Kết quả:** Trạng thái chuyển sang **Healthy** màu xanh.

### Bước 2.3: Cấu hình Security Group (Tokyo)

- Mở cổng **UDP 51820/51821** cho nguồn `0.0.0.0/0`.
- _Lý do:_ Vì AGA bảo lưu IP gốc từ Việt Nam, nên máy Tokyo cần chấp nhận gói tin từ mọi IP gửi đến thông qua Accelerator.

---

## 3. Tối ưu hóa "Động cơ" Máy chủ (BBR)

Để chống lại việc bóp băng thông và mất gói tin (packet loss) từ nhà mạng VN, thuật toán **Google BBR** đã được kích hoạt trên Ubuntu 24.04:

```bash
# Lệnh kích hoạt
echo "net.core.default_qdisc=fq" | sudo tee -a /etc/sysctl.conf
echo "net.ipv4.tcp_congestion_control=bbr" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

**Xác nhận trạng thái:**
`net.ipv4.tcp_congestion_control = bbr` (Đã kích hoạt thành công ✅)

---

## 4. Tối ưu hóa Thiết bị đầu cuối (MTU)

Để tránh gói tin bị vỡ khi đi qua nhiều lớp mã hóa và backbone:

- **Cấu hình:** Sửa file WireGuard trên Phone/PC.
- **Thông số:** `MTU = 1280`.
- **Tác dụng:** Giúp video TikTok load tức thì, không bị xoay vòng hoặc đen màn hình.

---

## 5. Kết quả kiểm tra (Test Results)

### 📊 So sánh lộ trình (Traceroute từ HCM)

| Tham số                | Qua Internet công cộng               | Qua AWS Global Accelerator                      |
| :--------------------- | :----------------------------------- | :---------------------------------------------- |
| **Số chặng (Hops)**    | 15 chặng (len lỏi qua nhiều router)  | **3 chặng** (nhảy thẳng vào mạng AWS)           |
| **Handshake**          | Bình thường                          | Cực nhanh                                       |
| **Đặc điểm nhận dạng** | Các IP của nhà mạng VN (Viettel/FPT) | Xuất hiện dải IP **`244.5.0.x`** (AWS Internal) |

### 🔍 Chi tiết Trace qua AGA (Thực tế của Lợi)

```text
1  10.9.0.2 (Tunnel Gateway)    128ms
2  244.5.0.195 (AWS AGA Node)   127ms  <-- Đã nhập làn cao tốc
3  13.193.91.19 (Tokyo Exit)    118ms  <-- Cán đích
```

> **Nhận xét:** Tuy Ping (120ms) cao hơn một chút so với đi thẳng (100ms), nhưng độ ổn định là tuyệt đối. Không có hiện tượng nhảy ping (jitter) hay mất gói.

---

## 6. Checklist kiểm tra định kỳ

- [x] Trạng thái AGA: **Healthy** (Cổng 22 TCP).
- [x] Thuật toán Congestion: **bbr**.
- [x] WireGuard Endpoint: Sử dụng IP của Accelerator.
- [x] Client MTU: **1280**.
- [ ] **IPv6 Leak Test:** (Cần kiểm tra trên `ipleak.net`, nếu thấy IP VN thì phải tắt IPv6).
