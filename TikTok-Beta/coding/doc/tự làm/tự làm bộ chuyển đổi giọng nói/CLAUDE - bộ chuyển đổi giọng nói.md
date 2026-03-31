# Ý tưởng về Bộ chuyển đổi giọng nói

Tôi muốn thực hiện kỹ thuật chuyển đổi giọng nói từ tiếng Việt sang tiếng Việt (speech to speech), ý tưởng cốt lõi là thay đổi vocal trong 1 file audio thành 1 vocal hoàn toàn khác, file audio thì chỉ bao gồm vocal + instrument, sơ đồ tóm tắt quy trình của tôi:
[original audio (chỉ có vocal + instrument, chỉ có tiếng Việt)]
-->
[vocal separation]
-->
[pre-process vocal]
-->
[vocal conversion]
-->
[post-process vocal]
-->
[mix vocal + stem]
-->
[converted audio (chỉ có vocal + instrument, chỉ có tiếng Việt)]

# Stem là gì?

**Stem** là file audio chứa **một thành phần riêng biệt** đã được tách ra khỏi bản nhạc gốc.

Ví dụ khi tách một bài hát:

| Stem         | Nội dung            |
| ------------ | ------------------- |
| `vocals.wav` | chỉ có giọng hát    |
| `drums.wav`  | chỉ có trống        |
| `bass.wav`   | chỉ có bass         |
| `other.wav`  | guitar, piano, v.v. |

# Đề xuất stack & roadmap

Q: Target voice (giọng đích) là gì?
A: Giọng tự mình clone (người thật)

Q: Bạn ưu tiên điều gì nhất?
A: Chất lượng output cao nhất có thể

Q: Bạn có data giọng nói tiếng Việt để train không?
A: Chưa có, cần tìm hoặc thu thập

> Với mục tiêu **clone giọng người thật, tiếng Việt, chất lượng cao**, đây là toàn bộ kế hoạch:

---

## Stack đề xuất cho từng bước

[Full pipeline đề xuất](./full_pipeline_with_tools.svg)

---

## Vấn đề cốt lõi cần giải quyết trước: Data

Vì bạn chưa có data, đây là phần quan trọng nhất. Chất lượng data quyết định ~80% chất lượng giọng sau khi convert.

**Yêu cầu tối thiểu cho RVC v2:**

| Tiêu chí   | Mức tối thiểu       | Lý tưởng                   |
| ---------- | ------------------- | -------------------------- |
| Thời lượng | 30 phút             | 1–2 giờ                    |
| Môi trường | Phòng yên tĩnh      | Phòng cách âm              |
| Thiết bị   | Micro condenser     | Studio mic                 |
| Nội dung   | Đọc văn bản đa dạng | Đủ 6 thanh điệu, nhiều vần |
| Format     | WAV 44.1kHz         | WAV 48kHz/24-bit           |

**Nội dung nên đọc:** đoạn văn xuôi, thơ, bài báo — để cover đủ phoneme tiếng Việt (đặc biệt các âm khó như "ươi", "oăn", "iêu", "uân").

---

## Roadmap gợi ý

Có 3 giai đoạn rõ ràng theo thứ tự ưu tiên:

**Giai đoạn 1 — Thu thập & chuẩn bị data** (làm ngay, song song với các bước khác): thu âm 30–60 phút, xử lý noise, cắt thành đoạn 3–10 giây.

**Giai đoạn 2 — Dựng pipeline kỹ thuật**: cài UVR5 để test vocal separation, cài RVC v2, test toàn bộ pipeline với một bài nhạc mẫu.

**Giai đoạn 3 — Train & iterate**: train model RVC với data đã thu, evaluate chất lượng, thu thêm data nếu cần.
