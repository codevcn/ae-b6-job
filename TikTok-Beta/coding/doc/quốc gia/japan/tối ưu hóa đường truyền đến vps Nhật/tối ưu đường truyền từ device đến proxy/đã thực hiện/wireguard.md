Chào Lợi, để xây dựng một quy trình chuẩn từ A-Z cho một hệ thống Proxy sử dụng WireGuard, chúng ta cần nhìn nhận sự phối hợp chặt chẽ giữa hai thực thể: **Thiết bị khách (Client Device)** và **Máy chủ Proxy (Ubuntu VPS)**.

Dưới đây là sơ đồ và các bước thiết lập chi tiết để đảm bảo hệ thống vận hành ổn định, có tính kế thừa từ cấu hình "Double Hop" mà bạn đã thực hiện thành công giữa Singapore và Tokyo.

---

## 🏗️ Tổng quan kiến trúc Proxy WireGuard

```text
[Client Device: Phone/PC] <--- (Tunnel WireGuard) ---> [Proxy Server: Ubuntu VPS] <---> [Internet/TikTok]
      (IP: 10.8.0.2)                                       (IP: 10.8.0.1)               (Exit IP: Tokyo/SG)
```

---

## Bước 1: Chuẩn bị trên Proxy Server (Ubuntu VPS)

Đầu tiên, bạn cần chuẩn bị "nội lực" cho máy chủ để nó có thể tiếp nhận và chuyển tiếp dữ liệu.

### 1.1 Cài đặt thành phần cốt lõi

Cài đặt WireGuard và công cụ tạo mã QR để thuận tiện cho việc thiết lập trên điện thoại sau này.

```bash
sudo apt update && sudo apt install wireguard qrencode -y
```

### 1.2 Kích hoạt chuyển tiếp gói tin (IP Forwarding)

Đây là bước bắt buộc để VPS không chỉ nhận gói tin mà còn biết cách "đẩy" nó ra internet.

- **Thực hiện:** Mở file `/etc/sysctl.conf` và bỏ dấu `#` trước dòng `net.ipv4.ip_forward=1`.
- **Áp dụng:** Chạy lệnh `sudo sysctl -p` để thay đổi có hiệu lực vĩnh viễn.

---

## Bước 2: Thiết lập cặp khóa (Security Keys)

Mối quan hệ giữa Client và Proxy dựa trên sự tin tưởng thông qua cặp khóa Public/Private.

1.  **Khóa cho Proxy:** Tạo file `server_private.key` và `server_public.key`.
2.  **Khóa cho Client:** Tạo file `client_private.key` và `client_public.key`.
    - _Lưu ý:_ Khóa Private của bên nào thì bên đó giữ kín, chỉ trao đổi Public Key cho nhau.

---

## Bước 3: Cấu hình chi tiết cho Proxy Server (`wg0.conf`)

Bạn cần cấu hình để VPS đóng vai trò là điểm tập trung (Hub). Điểm quan trọng nhất ở đây là sử dụng `PostUp` để lưu định tuyến vĩnh viễn, tránh việc bị mất cấu hình khi khởi động lại máy.

**File cấu hình tại `/etc/wireguard/wg0.conf`:**

```ini
[Interface]
Address = 10.8.0.1/24
ListenPort = 51820
PrivateKey = <PROXY_SERVER_PRIVATE_KEY>

# Định tuyến và NAT: Thay 'ens5' bằng tên card mạng thực tế của bạn (như trên VPS Tokyo)
PostUp = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o ens5 -j MASQUERADE
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o ens5 -j MASQUERADE

# Định nghĩa thiết bị khách (Client)
[Peer]
PublicKey = <CLIENT_DEVICE_PUBLIC_KEY>
AllowedIPs = 10.8.0.2/32
```

- _Lưu ý:_ Tên card mạng trên các Instance AWS mới thường là `ens5` thay vì `eth0` truyền thống.

---

## Bước 4: Cấu hình trên Client Device (Phone/PC)

Để tối ưu cho việc dùng TikTok và tránh các lỗi về rò rỉ thông tin, cấu hình thiết bị khách cần đặc biệt lưu ý đến IPv6 và MTU.

**File cấu hình `client.conf`:**

```ini
[Interface]
PrivateKey = <CLIENT_DEVICE_PRIVATE_KEY>
Address = 10.8.0.2/32
DNS = 1.1.1.1
MTU = 1280  # Tối ưu để gói tin không bị phân mảnh khi đi qua nhiều hop

[Peer]
PublicKey = <PROXY_SERVER_PUBLIC_KEY>
Endpoint = <PUBLIC_IP_CỦA_VPS>:51820
AllowedIPs = 0.0.0.0/0, ::/0  # Ép cả traffic IPv4 và IPv6 đi vào tunnel để tránh rò rỉ vị trí thật
PersistentKeepalive = 25
```

- Việc thêm `::/0` vào `AllowedIPs` sẽ giúp xử lý triệt để vấn đề IPv6 Leak mà bạn đã ghi nhận trong quá trình kiểm tra.

---

## Bước 5: Kích hoạt và Kiểm tra

1.  **Trên VPS:** Chạy `sudo systemctl enable wg-quick@wg0` để dịch vụ tự khởi động cùng hệ thống.
2.  **Tạo mã QR:** Dùng lệnh `qrencode -t ansiutf8 < client.conf` để hiển thị mã quét cho điện thoại.
3.  **Mở cổng Firewall:** Đảm bảo Security Group trên AWS đã mở cổng **UDP 51820** cho nguồn từ `0.0.0.0/0`.

---

## Bảng kiểm tra kết quả cuối cùng

| Thành phần  | Trạng thái cần đạt    | Cách kiểm tra                                               |
| :---------- | :-------------------- | :---------------------------------------------------------- |
| **Tunnel**  | Đã Handshake          | Chạy `sudo wg show` trên VPS                                |
| **Exit IP** | Đúng IP Proxy (Tokyo) | Truy cập `ifconfig.me` trên điện thoại                      |
| **Route**   | Đi qua Gateway nội bộ | Dùng **Network Analyzer** check Hop 1 là `10.8.0.1`         |
| **IPv6**    | Không bị rò rỉ        | Kiểm tra tại `ipv6-test.com` (phải hiện IP Proxy hoặc None) |

Quy trình này không chỉ giúp bạn có một Proxy đơn lẻ mà còn là nền tảng vững chắc để tích hợp vào chuỗi Relay Singapore - Tokyo mà bạn đang vận hành.

**Lợi có muốn tôi hướng dẫn cách lồng ghép cấu hình PostUp/PostDown này vào máy chủ Singapore để nó tự động chuyển tiếp traffic sang Tokyo một cách mượt mà nhất không?**
