# Google Labs Flow × Veo 3.1 — Quy Trình Chuẩn A–Z

> **Cập nhật 2026 · Google DeepMind**
> Quy trình tạo video cinematic theo đúng ý muốn — từ concept đến thành phẩm xuất kho.

| Thống kê   |                         |
| ---------- | ----------------------- |
| 🔢 Số bước | 9 bước thực hiện        |
| 🎬 Model   | Veo 3.1 (mạnh nhất)     |
| ⚡ Credits | ~20 credits/clip (Fast) |
| 🇻🇳 Khu vực | Việt Nam hỗ trợ đầy đủ  |

---

## ⚙️ Điều kiện cần thiết

Trước khi bắt đầu, bạn cần chuẩn bị đủ 4 thứ:

**🔑 Google AI Pro hoặc Ultra**
Đăng ký tại `one.google.com/ai`. Gói Pro ~$20/tháng, có credits dùng Veo 3.1. Gói Ultra mạnh hơn với nhiều credits hơn và truy cập tính năng mới sớm. Hỗ trợ thanh toán VNPAY hoặc thẻ ngân hàng Việt Nam.

**🔞 Đủ 18 tuổi & đã xác minh**
Tài khoản Google phải đã xác thực tuổi. Việt Nam được hỗ trợ đầy đủ.

**💻 Máy tính + Chrome**
Dùng trình duyệt Chromium (Chrome) trên máy tính để có trải nghiệm tối ưu. Mobile chưa được tối ưu hóa đầy đủ.

**⚡ Credits đủ dùng**
Veo 3.1 Fast tốn ~20 credits/clip. Quality tốn nhiều hơn. Ảnh Nano Banana Pro thường miễn phí hoặc rất ít credits.

> ⚠️ **Lưu ý:** Nếu credits hết giữa chừng, bạn có thể mua thêm top-up hoặc nâng cấp lên gói Ultra. Tất cả video xuất ra đều có **watermark SynthID ẩn** — không thể xóa nhưng không nhìn thấy bằng mắt thường.

---

## 🎬 9 Bước từ A đến Z

### Giai đoạn 1 — Chuẩn bị & Thiết lập

#### Bước 01 — Đăng ký & Truy cập Flow

Đăng nhập gói Google AI Pro/Ultra, sau đó vào trực tiếp Flow.

- Truy cập `labs.google/fx/tools/flow` (thêm `/vi/` để dùng giao diện tiếng Việt)
- Đăng nhập bằng Gmail → Chấp nhận điều khoản sử dụng
- Nhấn **New Project** → Đặt tên dự án rõ ràng (ví dụ: "Quảng cáo sản phẩm tháng 7")

---

#### Bước 02 — Lên Concept & Storyboard ⭐ Quan trọng

Đừng vội nhập prompt. Hãy xác định rõ kịch bản trước — đây là bước tiết kiệm credits nhất.

- Xác định: Video có bao nhiêu cảnh? Mỗi cảnh kéo dài bao lâu? Nhân vật trông như thế nào?
- Chuẩn bị **1–2 ảnh tham chiếu** (nền trắng/đơn giản, không có chữ) cho nhân vật hoặc sản phẩm
- Dùng **Gemini** để brainstorm ý tưởng: "Viết prompt Veo 3.1 cho cảnh này" + đính kèm ảnh

---

#### Bước 03 — Thiết lập thông số kỹ thuật

Cấu hình đúng từ đầu giúp tránh lãng phí credits vào các clip không đạt yêu cầu.

- **Model:** Chọn `Veo 3.1 Fast` khi thử nghiệm, `Veo 3.1 Quality` khi muốn xuất bản
- **Aspect Ratio:** 16:9 cho YouTube/phim · 9:16 cho TikTok/Reels/Shorts
- **Duration (hệ số x):** Dùng x1 để thử nghiệm hướng đi, x2/x4 khi đã ưng kết quả
- **Output count:** Tạo 2–4 phiên bản cùng lúc để có nhiều lựa chọn

---

### Giai đoạn 2 — Tạo nội dung

#### Bước 04 — Viết Prompt theo công thức "Vàng" 🎬

Veo 3.1 rất nhạy bén với thuật ngữ điện ảnh. Prompt chi tiết = kết quả chính xác hơn đáng kể.

**Công thức Prompt chuẩn:**

```
[Chủ thể] + [Hành động] + [Bối cảnh] + [Góc máy & Chuyển động] + [Ánh sáng & Màu sắc] + [Âm thanh]
```

**Ví dụ thực tế:**

> _"A young Vietnamese woman wearing a white áo dài, walking slowly along a misty Saigon street at sunset. Low angle tracking shot, gentle slow zoom in. Warm golden hour lighting, soft bokeh background. Native audio: distant motorbike sounds, light wind. Cinematic, 8K, photorealistic."_

**Lưu ý khi viết prompt:**

- Viết bằng tiếng Anh để có kết quả tốt hơn (tiếng Việt vẫn được nhưng kém chính xác hơn)
- Sử dụng các từ khóa: `cinematic`, `8K`, `photorealistic`, `golden hour`, `tracking shot`
- Nếu nhân vật bị méo dạng: thêm `natural movement`, `high anatomical accuracy`

---

#### Bước 05 — Thêm Ingredients — ảnh tham chiếu ⭐ Bí quyết nhất quán

Đây là tính năng quan trọng nhất để nhân vật/sản phẩm trông giống nhau xuyên suốt nhiều clip.

- Click **Video Ingredients** → Kéo thả ảnh tham chiếu vào
- Gõ `@` trong ô prompt để chọn ảnh từ thư viện đã upload
- Chọn **Character Reference** (giữ mặt nhân vật) hoặc **Style Reference** (giữ tông màu/phong cách)
- Chỉnh **Weight 0.6–0.8** để cân bằng giữa tham chiếu và sự sáng tạo của AI
- Tránh ảnh có chữ hoặc nền phức tạp — dễ gây lỗi font hoặc xuất hiện nội dung lạ

---

#### Bước 06 — Tạo chuyển cảnh — Start & End Frames

Dùng hai ảnh đầu/cuối để AI tự động tạo chuyển cảnh mượt mà giữa hai trạng thái.

- Click **Video Frames** → Thêm ảnh vào ô "Start frame" và "End frame"
- Viết prompt mô tả hành động xảy ra ở giữa (hoặc để trống để AI tự sáng tạo)
- Rất hiệu quả cho: morphing, zoom in/out, chuyển cảnh ngày/đêm, trước/sau

---

### Giai đoạn 3 — Tinh chỉnh & Dựng cảnh

#### Bước 07 — Iteration — Xem lại & chỉnh sửa clip

Không ai ra đúng ý 100% ngay lần đầu. Biết cách iterate đúng giúp tiết kiệm tối đa credits.

- **Kết quả gần đúng?** Đừng xóa prompt — chỉnh nhẹ tính từ, điều chỉnh Seed để biến tấu
- **Muốn kéo dài?** Dùng `Extend` → Gõ hành động tiếp theo, AI viết tiếp 5–10 giây
- **Thêm/xóa vật thể?** Dùng `Insert object` / `Remove object` → Kéo khung vị trí rồi mô tả
- **Đổi góc máy?** Dùng `Camera` → Chọn pan / zoom / dolly / aerial
- **Vẽ doodle?** Vẽ trực tiếp lên frame để chỉ AI vị trí hoặc hướng chuyển động cần thiết
- Phiên bản cũ vẫn giữ trong **History panel** — có thể quay lại bất kỳ lúc nào

---

#### Bước 08 — Dựng thành phim — Scenebuilder

Ghép các clip riêng lẻ thành một câu chuyện liền mạch có đầu có cuối.

- Hover lên clip → More → **Add to Scene**
- Vào tab **Scenebuilder** (góc trên cùng) → Kéo thả để sắp xếp thứ tự
- Cắt đầu/cuối từng clip để ghép khớp nhau
- Preview toàn bộ để kiểm tra âm thanh, nhịp độ, tính liền mạch
- ⚠️ Timeline reset khi rời dự án — nhưng clip riêng lẻ vẫn được lưu

---

### Giai đoạn 4 — Upscale & Xuất video

#### Bước 09 — Upscale & Tải video về

Bước cuối — nâng chất lượng và xuất file về máy.

- Hover vào clip → More → **Download**
- Bản miễn phí: tải về 720p · Gói Pro/Ultra: 1080p hoặc 4K
- Có thể tải dạng **GIF 270p** để preview hoặc share nhanh
- Nếu cần thêm chữ/phụ đề/nhạc: dùng **CapCut** hoặc DaVinci Resolve sau khi tải về
- Xem mẫu video hay tại `labs.google/flow/tv` (Flow TV)

**Bảng so sánh chế độ:**

| Chế độ          | Tốc độ            | Chất lượng | Khi nào dùng                       |
| --------------- | ----------------- | ---------- | ---------------------------------- |
| Veo 3.1 Fast    | ⚡ Nhanh (~20 cr) | Tốt        | Thử nghiệm, draft                  |
| Veo 3.1 Quality | 🎬 Chậm hơn       | Tốt nhất   | Xuất bản, thành phẩm               |
| 720p Download   | —                 | Tiêu chuẩn | Bản thường, share mạng             |
| 4K Download     | —                 | Cao nhất   | Xuất bản chuyên nghiệp (Pro/Ultra) |

---

## 💡 Mẹo PRO để video đúng 100% ý

**✍️ Prompt cực chi tiết**
Mô tả đủ 6 yếu tố: subject + action + environment + lighting + camera + audio. Càng cụ thể, AI càng ít "tự sáng tác".

**🤖 Dùng Gemini viết prompt**
Mô tả ý tưởng bằng tiếng Việt cho Gemini, nó sẽ dịch và viết lại thành prompt điện ảnh chuẩn cho Veo 3.1.

**🎞️ Clip ngắn, ghép nhiều**
Tạo nhiều clip 8 giây rồi ghép trong Scenebuilder thay vì cố tạo 1 clip dài — tiết kiệm credits và dễ kiểm soát hơn.

**🖼️ Luôn dùng Ingredients**
Mỗi dự án có nhân vật/sản phẩm → upload ảnh reference ngay từ đầu. Ingredients giữ tính nhất quán mà không cần describe lại mỗi lần.

**🔄 Lặp lại nhiều phiên bản**
Generate 4–8 phiên bản cùng một prompt rồi chọn cái tốt nhất. Thậm chí kết quả "lỗi" đôi khi cho ra góc nhìn sáng tạo bất ngờ.

**❌ Tránh chữ trong ảnh tham chiếu**
Ảnh có logo, chữ, hoặc watermark thường gây lỗi font trong video. Dùng ảnh nền trắng thuần túy cho nhân vật hoặc sản phẩm.

---

## 🔗 Link nhanh

|                          |                             |
| ------------------------ | --------------------------- |
| 🎬 Mở Flow               | `labs.google/fx/tools/flow` |
| 🔑 Đăng ký Google AI Pro | `one.google.com/ai`         |
| 📺 Flow TV (xem mẫu)     | `labs.google/flow/tv`       |
| 🤖 Gemini (viết prompt)  | `gemini.google.com`         |

---

> _Google Labs Flow và Veo 3.1 là sản phẩm của Google DeepMind. SynthID watermark có trong tất cả video xuất ra._
