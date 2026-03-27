# Quy Trình chuẩn A–Z Tạo Video 1 Phút Bằng Grok AI

> **Lưu ý quan trọng:** Grok hiện chỉ tạo được clip tối đa **6–10 giây/lần**. Quy trình này hướng dẫn bạn chia kịch bản thành nhiều cảnh ngắn, tạo từng cảnh, rồi ghép lại thành video hoàn chỉnh 1 phút — nhân vật nhất quán, chất lượng cinematic.

| Thông số          | Giá trị  |
| ----------------- | -------- |
| Số giai đoạn      | 5        |
| Số bước thực hiện | 10       |
| Tổng thời gian    | < 1 giờ  |
| Chi phí cơ bản    | Miễn phí |

⚠️ **Giới hạn:** Grok miễn phí tạo clip **6 giây, 480p**. Gói **SuperGrok** cho phép **10 giây, 720p HD**. Prompt nên viết **bằng tiếng Anh** để đạt chất lượng tốt nhất.

---

## Giai đoạn 1 — Chuẩn bị & Lên kịch bản

_Thực hiện trước khi mở Grok_

### Bước 1 — Xác định ý tưởng video

Trả lời 5 câu hỏi cốt lõi trước khi bắt đầu:

- **Chủ đề:** Quảng cáo, câu chuyện, giáo dục, hài hước…?
- **Phong cách:** Cinematic, anime, 3D Pixar, realistic, cyberpunk…?
- **Định dạng:** 9:16 (TikTok/Reels) hay 16:9 (YouTube)?
- **Nhân vật chính:** Mô tả chi tiết ngoại hình, trang phục
- **Thông điệp cuối:** Người xem nhớ điều gì sau 1 phút?

---

### Bước 2 — Viết kịch bản 8–10 cảnh ⭐

Dùng ChatGPT hoặc Claude với prompt mẫu sau:

```
Viết kịch bản video 1 phút về [chủ đề].
Chia thành 8 cảnh, mỗi cảnh 6 giây.
Mô tả chi tiết: hành động, góc máy, ánh sáng, chuyển động.
Nhân vật: [mô tả chi tiết nhân vật chính].
```

**Cấu trúc 1 phút gợi ý:**

| Cảnh     | Nội dung                              | Thời lượng |
| -------- | ------------------------------------- | ---------- |
| Cảnh 1   | Mở đầu — giới thiệu bối cảnh          | 6s         |
| Cảnh 2–6 | Nội dung chính — diễn biến câu chuyện | 35s        |
| Cảnh 7–8 | Cao trào + kết thúc / CTA             | 18s        |

---

### Bước 3 — Viết Character Anchor (mô tả nhân vật cố định)

Tạo 1 đoạn mô tả nhân vật **dùng xuyên suốt tất cả các cảnh** để giữ nhất quán. Copy đoạn này vào đầu mọi prompt.

```
# Ví dụ Character Anchor:
main character: Vietnamese girl, 25 years old,
long black hair, white shirt, round glasses,
cinematic modern style, consistent appearance
```

Character Anchor cần bao gồm: tóc + màu tóc, trang phục cụ thể, phong cách ánh sáng, màu mắt / chi tiết đặc trưng.

---

## Giai đoạn 2 — Thiết lập Grok

### Bước 4 — Truy cập Grok & cấu hình ban đầu

- **Máy tính:** mở `grok.com` → đăng nhập Gmail hoặc tài khoản X
- **Điện thoại:** tải app **Grok** (iOS / Android)
- Vào **Menu → Settings → Behavior** → tắt _"Auto-generate video"_ để kiểm soát từng cảnh thủ công
- Chọn tab **Imagine** (góc trên hoặc sidebar)

---

## Giai đoạn 3 — Tạo từng cảnh video

_Quy trình cốt lõi_

### Bước 5 — Tạo ảnh tham chiếu nhân vật

Trước khi tạo video, tạo 1 ảnh nhân vật chuẩn làm mốc nhất quán:

- Trong Grok Imagine, chọn chế độ **Image** (không phải Video)
- Dán Character Anchor + mô tả Cảnh 1
- Chọn tỉ lệ 16:9 hoặc 9:16 tuỳ định dạng
- Generate, chọn ảnh đẹp nhất → **lưu lại làm chuẩn**

---

### Bước 6 — Chuyển ảnh → Video Cảnh 1 (Image-to-Video) ⭐

Upload ảnh vừa tạo lên Grok, nhập prompt cảnh 1, nhấn **"Make Video"**.

**Template prompt chuẩn mỗi cảnh:**

```
[Character Anchor] + [hành động] + [bối cảnh] + [góc máy] + [style]

# Ví dụ Cảnh 1:
Vietnamese girl, 25yo, long black hair, white shirt,
sitting at café table, reading book, warm afternoon light,
cinematic medium shot, golden hour, smooth camera pan right,
ultra detailed, 4K quality
```

**Chọn phong cách video:** Custom (linh hoạt nhất), Normal (cân bằng), Fun (tươi sáng), Spicy (táo bạo).

Sau khi generate xong → tải clip về (**Download MP4**).

---

### Bước 7 — Kỹ thuật "khung hình cuối" để nối cảnh mượt ⭐

Đây là bí quyết quan trọng nhất để video có sự liên tục tự nhiên:

- Mở video Cảnh 1 vừa tải → dừng ở **khung hình cuối cùng**
- PC: Right-click → _"Save frame"_ / Điện thoại: chụp màn hình
- Cảnh tiếp theo: **upload ảnh frame cuối này** lên Grok
- Thêm prompt Cảnh 2 → Generate video mới
- **Lặp lại** cho đến đủ 8–10 cảnh

```
# Vòng lặp cho mỗi cảnh:
Cảnh N-1 (frame cuối) → upload → prompt Cảnh N → generate → download
                                                          ↓
                                         Cảnh N (frame cuối) → ...
```

---

### Bước 8 — Mẹo tối ưu chất lượng prompt

Luôn thêm các từ khoá sau vào cuối mỗi prompt:

- **Ánh sáng & chất lượng:** `cinematic lighting` · `ultra detailed` · `4K quality`
- **Góc máy:** `close-up` · `wide shot` · `drone shot` · `tracking shot`
- **Chuyển động camera:** `camera pan` · `camera zoom` · `camera tilt`
- **Chuyển động nhân vật:** `walking` · `flowing` · `turning head`
- **Âm thanh:** `natural audio` · `ambient sound`

---

## Giai đoạn 4 — Tạo giọng đọc & âm thanh

### Bước 9 — Tạo voice-over từ kịch bản

Copy toàn bộ lời thoại trong kịch bản (không dùng prompt từng cảnh) vào một trong các công cụ:

| Công cụ                        | Ưu điểm                     |
| ------------------------------ | --------------------------- |
| **Minimax.io** — Speech 2.6 HD | Khuyến nghị, chất lượng cao |
| **ElevenLabs**                 | Giọng tự nhiên nhất         |
| **CapCut TTS**                 | Nhanh, miễn phí             |
| **Google AI Studio**           | Đa ngôn ngữ                 |

Chọn chất lượng cao nhất → tải file audio (.MP3) về máy. Nếu cần giọng tiếng Việt: thêm `"with Vietnamese voiceover"` vào prompt Grok.

---

## Giai đoạn 5 — Dựng phim & Xuất bản

### Bước 10 — Ghép video trong CapCut

- Mở CapCut → **New Project** → Import tất cả clip theo thứ tự
- **Tắt tiếng (Mute)** tất cả clip gốc
- Kéo file voice-over vào timeline → **đồng bộ với hình**
- Thêm transition: _Black Fade, Zoom In/Out_ giữa các cảnh
- Thêm nhạc nền nhẹ từ thư viện CapCut (âm lượng thấp hơn voice)
- Thêm subtitle / text nếu cần
- Kiểm tra tổng thời lượng đúng ~60 giây
- Export: **1080p / 1080×1920 (9:16), 30fps**

---

## Tóm tắt quy trình

| Bước | Việc làm                                                   | Công cụ              | Thời gian   |
| ---- | ---------------------------------------------------------- | -------------------- | ----------- |
| 1–3  | Ý tưởng → Kịch bản → Character Anchor                      | ChatGPT / Claude     | ~10 phút    |
| 4    | Thiết lập Grok, tắt auto-generate                          | grok.com / App Grok  | ~5 phút     |
| 5–8  | Ảnh chuẩn → Image-to-Video từng cảnh → Frame cuối nối cảnh | Grok Imagine         | ~20–40 phút |
| 9    | Tạo voice-over từ kịch bản                                 | Minimax / ElevenLabs | ~5 phút     |
| 10   | Ghép clip + audio + transition → Export                    | CapCut / DaVinci     | ~10 phút    |

---

## Lưu ý & So sánh gói

|                        | Gói miễn phí | SuperGrok     |
| ---------------------- | ------------ | ------------- |
| Thời lượng clip        | 6 giây / lần | 10 giây / lần |
| Độ phân giải           | 480p         | 720p HD       |
| Số clip cần cho 1 phút | ~10 clip     | 6 clip        |
| Watermark              | Không        | Không         |

**Prompt tốt nhất khi:** viết bằng tiếng Anh · kèm góc máy + chuyển động · luôn có Character Anchor · kết thúc bằng `4K, cinematic lighting`.
