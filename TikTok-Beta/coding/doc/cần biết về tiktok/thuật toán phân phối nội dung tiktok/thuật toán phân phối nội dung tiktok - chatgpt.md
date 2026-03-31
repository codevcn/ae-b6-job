## 🧠 Tổng quan nhanh: Thuật toán của TikTok hoạt động như thế nào?

![Image](https://images.openai.com/static-rsc-4/UVqRhderQnFUTl7OVj-yK6YDAO0X35MWPHKjyWEX-jGhDm4ai7BzUF6b7JQ2jcnd7CeuVh1987bjWZt8gQNPCIZd7ZNZPMm-qfEyMxi-tunz5xJdg1LOMl_TMRQ33fbmIqR4u2JvAcpUL2CG0semVdi99fmn7-XirOqsPrFadydVfqmER2-cMoWl149T4dHl?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/W538Trmb8BO_7Q-sASrvmK4CWTcn4R_-QGd314-WqdtpLBeMe6Ntxm-NgXY3jnf8D7uJW1ycayNi-46bwxrfK2KF6T9LwFPmMSc5SuDZSTbyqqTHBjUNjnGDJrenPN4VJ5mbEpfT4yv41kW9Zyfcg3RAjMRfhQwN_dhN-zVtoQ-dQ-xbzVo4yj25rJBXZVaZ?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/pUTpa87FVJyS9DnlmDX7Wo7MCsNFT0SpDxomY0iJH8-iG8gk4d-2Gp0JHIFQSkJ9P5NaEuGEuVLAIdhJmxrKbcI2sO3SH8Jv0Ru9KAqW0pYSufbLAMi-PrTU0FaHkgD1u76YhaX6qWAjH1KrTjTMVrI8CeEtu7O7klLmHt6IMBGDPsKl5UfLimyhx65yWEGP?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/Twr6974yDT-wla-YSh__6Ufpy5VfUPlOJuJbJW5euPs6p8-yZJ5QFY8BcPGJFsySQVqHJjZxcGo0OKBg7y4-k8bD1Z6LFegweUeDlwvI8OtRDvPvEUUhWYIYJCVAtWDFKcvCyHE8dlLMsVDich2Ij6IWgYV9pagsolm3nJHLZ86IGlcE5tmVZDxJ0RPLe0J6?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/ircAIX15mq-x-Xo5B41kFeyCQcqVNiMZ-M4DaF80J2r5RTh2PxLufoS67ZMY2M1-5xaQd2IyLCsq1tXH67UOeUFnZpR3rMKhZVYgFyb3zPlRT_SUu3cPQUqCkbPNe4YW_xs5tHCaZcmcTxbY_psokYdMjbYqMo9MKHzOQMyl-mv5e9kxJibUCOGhWSaw8EwS?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/yNjYHMUUBum0ynknTDHNqq68OJjQU-4zIPUU3A5Dgnoy0RliJSA_cGfaER4PJRwPMqeBBJC4JsEBcCRpix_iHt3i8P2x2rziY3r7PQmif2E6jdIYDN9F1CFwEEsfvfu2BuWjwNoBUTKpdLpI-pdS8fTtXXzcuOfRp8BYcctIGu907CmfXftFgIzNp054555K?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/XG_R7F6jsfAsKq2EPRJWa58tmXvLr1pkVB_o3OdJXA0hoc4YQ6b7WIAUz-I6kAJEoLSmtVNbNRAs6iTCUe_wDWZTvu6ndTLJt48JPPs1vbgIloDQmO-IO1Q0kT7I6QeSO9GtEVM42x07U2yBb5rIZ9k49WI72h6aKeKiD5yo9IsqGhjdRHq5A5Bfu3SCLuD6?purpose=fullsize)

TikTok KHÔNG phân phối nội dung theo kiểu “follow-based” như Facebook hay Instagram. Thay vào đó:

> 👉 Mỗi video là một “thử nghiệm độc lập” với một nhóm user nhỏ → nếu hiệu suất tốt → mở rộng phân phối theo từng tầng.

---

# ⚙️ Cơ chế cốt lõi (Core Loop)

## 1. Giai đoạn test ban đầu (Initial Distribution)

- Video mới đăng sẽ được đẩy đến:
  - ~200–500 người dùng đầu tiên (không cần follower)

- Đây là “vòng loại”

👉 TikTok đang hỏi:

> “Video này có đáng để lan rộng không?”

---

## 2. Các chỉ số quyết định sống còn (Ranking Signals)

### 🎯 Nhóm quan trọng nhất:

#### 📌 1. Watch Time (thời gian xem)

- % xem hết video (completion rate)
- Xem lại (rewatch)

👉 **Đây là yếu tố mạnh nhất**

---

#### 📌 2. Engagement (tương tác)

- Like ❤️
- Comment 💬
- Share 📤
- Save 📌

👉 Share + Comment có trọng số cao hơn Like

---

#### 📌 3. Hook rate (giữ chân 3 giây đầu)

- Bao nhiêu % user KHÔNG lướt qua trong 1–3 giây đầu

👉 Fail ở đây = chết từ vòng gửi xe

---

#### 📌 4. Video info

- Caption
- Hashtag
- Âm thanh (sound)
- Chủ đề nội dung

👉 Giúp TikTok hiểu “video thuộc cluster nào”

---

#### 📌 5. User behavior matching

- Người dùng từng xem gì
- Từng tương tác với dạng content nào

👉 TikTok match video với “tệp phù hợp nhất”

---

## 3. Vòng lặp mở rộng (Scaling Loop)

Nếu video vượt ngưỡng:

| Vòng   | Số user tiếp cận  |
| ------ | ----------------- |
| Test 1 | 200–500           |
| Test 2 | 1k–5k             |
| Test 3 | 10k–50k           |
| Viral  | 100k → hàng triệu |

👉 Mỗi vòng đều có “điểm chuẩn” riêng
👉 Fail ở vòng nào → dừng ở đó

---

# 🧬 Insight cực quan trọng (ít người hiểu đúng)

## ❗ 1. TikTok KHÔNG quan tâm bạn là ai

- Acc mới vẫn có thể viral
- Acc lớn vẫn flop như thường

👉 “Content > Creator”

---

## ❗ 2. Mỗi video là một cuộc thi riêng

- Video trước viral ≠ video sau viral

---

## ❗ 3. TikTok phân phối theo “interest graph”

Khác với:

- Facebook: social graph (bạn bè)
- TikTok: **interest graph (sở thích)**

---

## ❗ 4. Video không chết ngay

- Có thể viral lại sau vài ngày / vài tuần

---

# 🧪 Reverse Engineering (góc nhìn dev / growth)

## TikTok thực chất đang optimize:

> **Expected Watch Time per Impression**

Tức là:

```
Score ≈ (Avg Watch Time × Completion Rate × Rewatch Rate)
       + (Weighted Engagement)
```

---

# 📊 Công thức thực chiến (ước lượng)

Một video dễ viral khi:

- Completion rate > 70%
- Avg watch time ≈ 90–120% video length (có rewatch)
- Share rate > 1–3%
- Comment rate > 0.5%

---

# 🔥 Tại sao nhiều video “nhảm” vẫn viral?

Vì chúng:

- Hook cực mạnh trong 1–2 giây đầu
- Dễ xem hết (ngắn, gây tò mò)
- Kích thích rewatch (twist, loop)

---

# 🧩 Cách TikTok hiểu nội dung của bạn

## Dựa trên:

- Speech-to-text (AI đọc nội dung nói)
- Computer Vision (nhận diện hình ảnh)
- Caption + hashtag
- Âm thanh đang trend

👉 Nó build thành **content cluster**

---

# 🚀 Áp dụng cho bạn (game dev / push content)

Dựa vào bối cảnh bạn đang:

> [ra mắt game] → [push content] → [lấy user]

👉 TikTok chính là kênh mạnh nhất nếu hiểu thuật toán:

## 🎯 Chiến lược phù hợp:

### 1. Làm video NGẮN (5–15s)

- Tăng completion rate

### 2. Hook cực mạnh trong 2 giây đầu

Ví dụ:

- “99% người chơi fail level này”
- “Bạn có giải được trong 5 giây không?”

---

### 3. Loop video

- Kết thúc quay lại đầu tự nhiên
- Người xem xem lại mà không nhận ra

---

### 4. Content dạng:

- Puzzle / thử thách (rất hợp game 2048 của bạn)
- Fail / rage
- Trick / hack game

---

### 5. Spam test nhiều video

- 1 video = 1 thử nghiệm
- Không cần hoàn hảo

---

# 🧠 Tóm lại (ngắn gọn nhất có thể)

👉 Thuật toán TikTok =
**Test nhỏ → đo retention + engagement → scale dần**

👉 Muốn win:

- Hook mạnh
- Giữ chân lâu
- Kích thích tương tác
- Test liên tục
