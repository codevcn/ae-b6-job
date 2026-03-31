# Tài liệu: Setup & Khôi phục Dante SOCKS5 Proxy + Clash Verge

**Ngày thực hiện:** 2026-03-28  
**Server:** `ip-172-31-40-206` (AWS EC2 — ap-northeast-1 Tokyo)  
**Mục đích:** Khôi phục Dante proxy bị crash, thêm swap, cấu hình Clash Verge trên Windows 11

---

## 1. Kiểm tra trạng thái Dante

### Lệnh kiểm tra

```bash
systemctl status danted
ps aux | grep danted
dpkg -l | grep dante
ss -tlnp | grep 1080
```

### Kết quả phát hiện

- Trên VPS `b6-tokyo-proxy`: **không có Dante** (unit not found, không có package)
- Trên VPS `ip-172-31-40-206`: **Dante đã cài nhưng bị crash**

```
Active: failed (Result: oom-kill) since Sat 2026-03-21 13:41:27 UTC; 6 days ago
```

**Nguyên nhân:** OOM Kill — kernel tắt process Dante do hết RAM.

---

## 2. Kiểm tra RAM & Process

```bash
free -h
ps aux --sort=-%mem | head -15
```

### Kết quả

|      | Tổng  | Đã dùng | Còn trống | Available |
| ---- | ----- | ------- | --------- | --------- |
| RAM  | 911Mi | 357Mi   | 86Mi      | 553Mi     |
| Swap | 0     | 0       | 0         | 0         |

**Nhận xét:** RAM hiện tại còn đủ (~553Mi available). Không có swap → khi RAM spike, kernel lập tức OOM kill process thay vì dùng swap làm buffer.

---

## 3. Thêm Swap 1GB (phòng OOM)

```bash
sudo fallocate -l 1G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

- `/etc/fstab` được cập nhật để swap tự mount sau khi reboot.

---

## 4. Khởi động lại Dante

```bash
sudo systemctl restart danted
sudo systemctl status danted
```

### Kết quả sau khi restart

```
Active: active (running) since Sat 2026-03-28 06:10:54 UTC
Memory: 8.2M (peak: 8.2M)
Tasks: 20
```

Dante chạy ổn định với 20 worker processes, memory chỉ ~8MB.

---

## 5. Thông tin Proxy

| Thông số       | Giá trị                        |
| -------------- | ------------------------------ |
| Protocol       | SOCKS5                         |
| Port           | 1080                           |
| Authentication | Không (open)                   |
| Frontend       | AWS Global Accelerator         |
| Backend        | EC2 Tokyo (`ip-172-31-40-206`) |

> **Lưu ý:** Kết nối từ client nên dùng **IP của AWS Global Accelerator** (không dùng IP EC2 trực tiếp) để tận dụng backbone AWS, giảm latency và packet loss.

---

## 6. Cấu hình Clash Verge trên Windows 11

### Phần mềm

- **Clash Verge Rev** — https://github.com/clash-verge-rev/clash-verge-rev/releases
- Version sử dụng: v2.4.7 (Mihomo core v1.19.21)

### File config (`proxy.yaml`)

```yaml
mixed-port: 7890
allow-lan: false
mode: global
log-level: info
ipv6: false

proxies:
  - name: "Tokyo VPS"
    type: socks5
    server: <IP_GLOBAL_ACCELERATOR>
    port: 1080
    udp: true

proxy-groups:
  - name: "PROXY"
    type: select
    proxies:
      - "Tokyo VPS"

rules:
  - MATCH,PROXY
```

### Các bước import & kích hoạt

1. Mở Clash Verge → tab **Profiles**
2. Click **NEW** → chọn Type: **Local** → đặt tên → Save
3. Click icon **Edit** trên profile → dán nội dung yaml → Save
4. Click profile để **activate** (viền xanh)

### Bật proxy toàn hệ thống

| Cài đặt      | Trạng thái       |
| ------------ | ---------------- |
| System Proxy | ON (chấm xanh)   |
| TUN Mode     | ON (toggle xanh) |
| Proxy Mode   | **Global**       |
| Running Mode | Service Mode     |

> **TUN Mode** bắt buộc để route **toàn bộ traffic** kể cả các app không hỗ trợ proxy trực tiếp.  
> Lần đầu bật TUN Mode cần cài service → click Install khi được hỏi (yêu cầu quyền Admin).

### Lỗi gặp phải & cách fix

| Lỗi                                    | Nguyên nhân            | Fix                               |
| -------------------------------------- | ---------------------- | --------------------------------- |
| `TUN Mode Service Required`            | Service chưa được cài  | Click bánh răng → Install Service |
| IP vẫn hiện Vietnam                    | Current Node để DIRECT | Vào Proxies → chọn **Tokyo VPS**  |
| Proxy Mode = Rule nhưng không có rules | Config chỉ có `MATCH`  | Đổi Proxy Mode sang **Global**    |

---

## 7. Kiểm tra kết nối

Truy cập https://whatismyipaddress.com — IP phải hiện **địa chỉ EC2 Tokyo** (không phải IP nhà, không phải IP Global Accelerator).

---

## 8. Lưu ý vận hành

- **Swap đã được thêm** — nếu RAM spike, hệ thống dùng swap thay vì kill Dante
- Dante được set **enabled** → tự khởi động sau reboot
- Theo dõi log Dante nếu có vấn đề: `sudo journalctl -u danted -f`
- Kiểm tra RAM định kỳ: `free -h`
- Nếu Dante crash lại: `sudo systemctl restart danted`
