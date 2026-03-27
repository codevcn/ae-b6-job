**Đúng rồi!** Đây là câu hỏi rất hay để làm rõ sự khác biệt giữa các mô hình kiếm tiền.

**Quảng cáo trong game (in-game ads)** chủ yếu xuất hiện ở **phân khúc mobile free-to-play**, đặc biệt là những game **cần volume người chơi cực lớn** và **không muốn người chơi trả tiền upfront**. Chúng không phổ biến (và thường bị ghét) ở game indie/AA trên Steam hay console vì làm giảm trải nghiệm và khó viral.

Dưới đây là **các dòng game thường xuyên chèn quảng cáo nhất** (dựa trên dữ liệu 2025–2026 từ Sensor Tower, GameAnalytics, Moloco và các báo cáo ngành):

### 1. **Hyper-casual** (Thể loại “siêu casual” – chiếm tỷ lệ lớn nhất về quảng cáo)

- Đặc điểm: Game siêu đơn giản, chơi trong 30 giây – 2 phút, không cần tutorial dài.
- Loại quảng cáo: Interstitial (toàn màn hình), Rewarded (xem để nhận thưởng), Banner.
- Tại sao nhiều ads? Doanh thu gần như 100% từ ads, retention thấp nên phải “vắt” liên tục.
- Ví dụ: Stack Ball, Color Fill 3D, Join Clash, Bridge Race, Aquapark.io, Hole.io.

### 2. **Puzzle / Match-3**

- Đặc điểm: Ghép 3, giải đố, level-based.
- Loại quảng cáo: Rewarded ads để nhận lives, booster, skip level.
- Ví dụ: Candy Crush Saga, Gardenscapes, Homescapes, Royal Match.

### 3. **Merge & Idle / Incremental**

- Đặc điểm: Merge vật phẩm, clicker, game “ngồi chơi cũng lên level”.
- Loại quảng cáo: Rewarded cho tài nguyên, speed-up, offline progress.
- Ví dụ: Merge Mansion, Merge Dragons, AFK Arena (một phần), Idle Miner Tycoon.

### 4. **Arcade / Endless Runner / Simple Action**

- Đặc điểm: Chạy vô tận, tránh chướng ngại vật.
- Ví dụ: Temple Run, Subway Surfers, Talking Tom series, Stack Runner.

### 5. **Casual Simulation / Tycoon / Board / Solitaire / Word Games**

- Đặc điểm: Xây dựng nhẹ, quản lý nhỏ, trò chơi trí tuệ đơn giản.
- Ví dụ: Monopoly Go!, Solitaire Grand Harvest, Wordle-style games, FarmVille-style.

### Bảng tóm tắt nhanh (để dễ hình dung)

| Thể loại         | Mức độ dùng ads | Nền tảng chính    | Doanh thu chính  | Retention (giữ chân) |
| ---------------- | --------------- | ----------------- | ---------------- | -------------------- |
| Hyper-casual     | Rất cao         | Mobile            | 90–100% từ ads   | Thấp                 |
| Puzzle / Match-3 | Cao             | Mobile            | Ads + IAP        | Trung bình           |
| Merge / Idle     | Cao             | Mobile            | Ads + IAP        | Trung bình cao       |
| Arcade / Runner  | Cao             | Mobile            | Ads              | Thấp                 |
| Strategy / RPG   | Thấp–trung bình | Mobile (một phần) | Chủ yếu IAP      | Cao                  |
| Indie/AA Premium | Gần như không   | PC/Steam/Console  | Bán game một lần | Rất cao              |

**Kết luận quan trọng:**  
Các game dùng quảng cáo nhiều nhất đều thuộc **phân khúc casual → hyper-casual trên mobile**. Chúng kiếm tiền bằng **số lượng người chơi khổng lồ + xem ads liên tục**, chứ không phải chất lượng trải nghiệm hay lòng trung thành lâu dài (điều mà Balatro, Lethal Company… đang làm rất tốt).

Nếu bạn muốn **thêm phần này vào file HTML** trực quan (để so sánh rõ ràng với các mô hình “tử tế” trước đó), tôi đã cập nhật ngay cho bạn. Chỉ cần copy toàn bộ code dưới đây (đã thêm section mới ngay sau phần Quảng cáo):

```html
<!-- Thêm phần này vào file HTML cũ, ngay sau section id="ads" -->

<!-- PHẦN MỚI: CÁC DÒNG GAME THƯỜNG CHÈN QUẢNG CÁO -->
<section id="genres" class="max-w-screen-2xl mx-auto px-8 py-16 bg-slate-900">
  <div class="flex items-end justify-between mb-8">
    <div>
      <span class="text-orange-400 text-sm font-mono flex items-center gap-x-2">
        <i class="fa-solid fa-mobile-screen"></i>
        MOBILE FREE-TO-PLAY
      </span>
      <h2
        class="section-header text-4xl heading-font font-semibold tracking-tighter text-orange-300"
      >
        Các dòng game thường xuất hiện quảng cáo trong game
      </h2>
    </div>
    <p class="max-w-md text-slate-400">
      Phân khúc hay “vắt chanh” người chơi nhất – hoàn toàn trái ngược với Value-based Monetization.
    </p>
  </div>

  <div class="grid md:grid-cols-3 gap-6">
    <div class="bg-white/5 backdrop-blur rounded-3xl p-6 border border-orange-400/30">
      <div class="text-4xl mb-4">⚡</div>
      <h3 class="text-xl font-semibold">Hyper-casual</h3>
      <p class="text-sm text-slate-400 mt-2">
        Stack, run, fill, merge… Chơi 1 phút là chán → chèn ads liên tục.
      </p>
      <div class="mt-6 text-xs flex flex-wrap gap-2">
        <span class="px-3 py-1 bg-orange-400/10 text-orange-400 rounded-3xl">Stack Ball</span>
        <span class="px-3 py-1 bg-orange-400/10 text-orange-400 rounded-3xl">Color Fill</span>
        <span class="px-3 py-1 bg-orange-400/10 text-orange-400 rounded-3xl">Bridge Race</span>
      </div>
    </div>

    <div class="bg-white/5 backdrop-blur rounded-3xl p-6 border border-orange-400/30">
      <div class="text-4xl mb-4">🧩</div>
      <h3 class="text-xl font-semibold">Puzzle / Match-3</h3>
      <p class="text-sm text-slate-400 mt-2">Rewarded ads để nhận lives, booster, skip level.</p>
      <div class="mt-6 text-xs flex flex-wrap gap-2">
        <span class="px-3 py-1 bg-orange-400/10 text-orange-400 rounded-3xl">Candy Crush</span>
        <span class="px-3 py-1 bg-orange-400/10 text-orange-400 rounded-3xl">Gardenscapes</span>
        <span class="px-3 py-1 bg-orange-400/10 text-orange-400 rounded-3xl">Royal Match</span>
      </div>
    </div>

    <div class="bg-white/5 backdrop-blur rounded-3xl p-6 border border-orange-400/30">
      <div class="text-4xl mb-4">🔄</div>
      <h3 class="text-xl font-semibold">Idle / Merge / Arcade</h3>
      <p class="text-sm text-slate-400 mt-2">
        Idle Miner, Merge Mansion, Endless Runner… Ads để speed-up, offline reward.
      </p>
      <div class="mt-6 text-xs flex flex-wrap gap-2">
        <span class="px-3 py-1 bg-orange-400/10 text-orange-400 rounded-3xl">Merge Mansion</span>
        <span class="px-3 py-1 bg-orange-400/10 text-orange-400 rounded-3xl">Subway Surfers</span>
        <span class="px-3 py-1 bg-orange-400/10 text-orange-400 rounded-3xl">Idle Tycoon</span>
      </div>
    </div>
  </div>

  <div class="mt-10 text-center text-xs text-slate-500">
    💡 Lưu ý: Hầu hết các game này đều là mobile. Trên Steam/PC, quảng cáo trong game gần như bị
    Valve hạn chế nghiêm ngặt từ 2025.
  </div>
</section>
```

Bạn chỉ cần dán phần trên vào file cũ là có ngay bảng so sánh trực quan.

# Các game tiêu biểu mà thành công trong mảng quảng cáo

**Dưới đây là danh sách các game tiêu biểu thành công nhất trong mảng “quảng cáo trong game” (ad-based / hybrid monetization)** những năm gần đây (2024–2026).

Tôi tập trung vào các tựa **mobile free-to-play** thuộc phân khúc **hyper-casual, hybrid-casual, puzzle/match-3, merge/idle, arcade** – những thể loại mà quảng cáo (rewarded video, interstitial, banner) chiếm tỷ lệ doanh thu rất lớn (thường 50–90%). Dữ liệu dựa trên báo cáo Sensor Tower, AppMagic, Liftoff & Singular năm 2025–2026.

### 1. **Puzzle / Match-3 & Block Puzzle** (Thể loại thống trị ad revenue)

| Game                 | Nhà phát triển | Doanh thu nổi bật (2025) | Loại quảng cáo chính       | Ghi chú                         |
| -------------------- | -------------- | ------------------------ | -------------------------- | ------------------------------- |
| **Royal Match**      | Dream Games    | ~1.37 tỷ USD             | Rewarded (lives, boosters) | Top 1 casual game toàn cầu 2025 |
| **Candy Crush Saga** | King           | ~1.01 tỷ USD             | Rewarded + interstitial    | Classic vẫn cực mạnh            |
| **Block Blast!**     | -              | Top downloads + revenue  | Rewarded video             | Hybrid-casual block puzzle hot  |
| **Gardenscapes**     | Playrix        | ~396 triệu USD           | Rewarded (energy, stars)   | Narrative + puzzle              |
| **Homescapes**       | Playrix        | Top 20 casual            | Rewarded                   | Cùng series Gardenscapes        |

### 2. **Board / Casual Simulation**

| Game             | Nhà phát triển | Doanh thu nổi bật (2025)      | Loại quảng cáo chính    | Ghi chú                                |
| ---------------- | -------------- | ----------------------------- | ----------------------- | -------------------------------------- |
| **MONOPOLY GO!** | Scopely        | ~1.36 tỷ USD (lifetime >6 tỷ) | Rewarded + interstitial | Một trong những hit lớn nhất 2024-2025 |
| **Coin Master**  | Moon Active    | ~650 triệu USD                | Rewarded video          | Slot machine + village building        |

### 3. **Merge / Idle**

| Game                             | Nhà phát triển | Doanh thu nổi bật (2025) | Loại quảng cáo chính           | Ghi chú                                 |
| -------------------------------- | -------------- | ------------------------ | ------------------------------ | --------------------------------------- |
| **Gossip Harbor: Merge & Story** | Microfun       | ~550 triệu USD           | Rewarded (energy, merge items) | Merge-2 với story, tăng trưởng cực mạnh |
| **Merge Mansion**                | -              | Top merge category       | Rewarded                       | Vẫn ổn định                             |

### 4. **Hybrid-Casual & Hyper-Casual thuần** (Top hybridcasual 2025)

Những game này kết hợp cơ chế hyper-casual đơn giản + rewarded ads + một ít IAP:

- **Color Block Jam** (Rollic Games) → Top 1 hybrid-casual, ~33–42 triệu USD/quý
- **Screwdom** (iKame Games / Zego) → Screw puzzle, doanh thu cao
- **All in Hole** (Homa Games)
- **Hole People** (Rollic)
- **Magic Sort!**, **Goods Puzzle: Sort Challenge**
- **Pocket Champs** (Madbox)

**Hyper-casual thuần (downloads khổng lồ, ads chiếm gần 100%):**

- **Subway Surfers** (SYBO Games) → Vẫn top 2–3 most downloaded mobile game 2025
- **Paper.io 2** → Top DAU hyper-casual Android
- **Stack Ball**, **Bridge Race**, **Color Fill 3D** (cũ nhưng vẫn chạy ads mạnh)

### Tóm tắt xu hướng 2025–2026

- **Không còn hyper-casual thuần 100% ads** nữa → hầu hết chuyển sang **hybrid-casual** (ads + IAP + LiveOps) để tăng retention.
- **Puzzle & Merge** là 2 sub-genre kiếm tiền từ quảng cáo tốt nhất (puzzle >8 tỷ USD toàn ngành 2025).
- **Royal Match** và **MONOPOLY GO!** là 2 “ông lớn” điển hình: dùng rewarded ads cực kỳ khéo léo, người chơi **chủ động xem** để nhận thưởng thay vì bị ép.

# Phân tích lý do thành công của các game mảng quảng cáo ở trên

**Phân tích chi tiết lý do thành công của các tựa game mảng quảng cáo (ad-based / hybrid monetization) 2024–2026**

Dựa trên dữ liệu mới nhất từ **Sensor Tower, AppMagic, Naavik, Udonis, Business of Apps** (cập nhật đến tháng 3/2026), tôi phân tích **top game tiêu biểu** bạn đã hỏi.

**Điểm chung quan trọng:**  
Hầu hết các game này **không còn là hyper-casual thuần 100% ads** nữa. Chúng chuyển sang **mô hình hybrid** (40–60% revenue từ rewarded ads + 40–60% từ IAP). Rewarded ads được thiết kế **voluntary** (người chơi chủ động xem để nhận thưởng), không ép buộc → retention cao hơn, churn thấp hơn. Thành công đến từ **kết hợp gameplay addictive + LiveOps liên tục + UA thông minh**.

Dưới đây là phân tích từng game/group:

### 1. **Royal Match (Dream Games) – Match-3 Puzzle**

- **Doanh thu**: ~1.4 tỷ USD (2024) → vẫn top 3–5 toàn cầu 2025, lifetime >3 tỷ USD.
- **Lý do thành công chính**:
  - **Gameplay “ultimate casual”**: Dễ tiếp cận nhưng có chiều sâu (near-miss levels tạo FOMO), visuals đẹp, nhân vật dễ thương (King Robert, Winston, Duke).
  - **LiveOps cực mạnh**: Mini-games, weekend tournaments (Propeller Rush tăng **14.6% revenue** chỉ trong 3 ngày), seasonal events → giữ người chơi quay lại hàng ngày.
  - **Monetization thông minh**: **Chủ yếu IAP** (không ads ép buộc), tập trung “whales” (ARPDAU ~0.17 USD – cao nhất phân khúc). Rewarded ads chỉ show cho non-payers → ads bổ trợ chứ không phải nguồn chính.
  - **User Acquisition xuất sắc**: Playable ads + paid UA lớn + celebrity campaigns (tương tự Royal Kingdom).
  - **Iteration data-driven**: A/B test liên tục (ví dụ: “Super Light Ball” tăng revenue 1.5×).

### 2. **MONOPOLY GO! (Scopely) – Board / Casual Simulation**

- **Doanh thu**: >6 tỷ USD lifetime (nhanh nhất lịch sử mobile game, đạt mốc này chỉ trong ~1.275 ngày), ~200 triệu USD/tháng.
- **Lý do thành công chính**:
  - **Social & virality mạnh**: Multiplayer events, gifting, trading, friend interactions → người chơi kéo bạn bè vào (social flywheel).
  - **Fast reward loops + board progression**: Cảm giác “tiến bộ nhanh” như board game thật, tạo nghiện.
  - **Event-Driven LiveOps quy mô lớn**: Limited-time competitions, daily events → lý do quay lại liên tục.
  - **Retention curve cực tốt**: Dài hạn cao nhất Scopely từng có → LTV cao.
  - **Marketing khổng lồ**: >1 tỷ USD UA (celebrity ads với Will Ferrell, Chris Pratt…).

### 3. **Candy Crush Saga (King) – Match-3 Classic**

- **Doanh thu**: ~1 tỷ USD/năm (vẫn top 10), lifetime >20 tỷ USD.
- **Lý do thành công chính**:
  - **Universal appeal + longevity**: 10+ năm tuổi nhưng vẫn giữ 26 triệu DAU toàn cầu nhờ level-based dễ chơi mọi lứa tuổi.
  - **Rewarded ads khéo léo nhất ngành**: Chỉ show cho người **không bao giờ mua IAP** (segmentation tinh tế). Người chơi **chủ động xem** để lấy lives/boosters → ads bổ trợ economy chứ không phá gameplay.
  - **Non-intrusive monetization**: IAP + rewarded ads hòa quyện, không gây khó chịu.
  - **Events lớn**: All Stars tournament (15 triệu người tham gia, +108 triệu USD IAP chỉ trong 1 tháng).

### 4. **Block Blast! (Hungry Studio) – Block Puzzle / Hybrid-Casual**

- **Doanh thu**: Top downloads toàn cầu 2025–2026, 70 triệu DAU, 300 triệu MAU.
- **Lý do**: Cơ chế siêu đơn giản + relaxing, high-frequency play (chơi ngắn nhưng chơi nhiều lần/ngày). Hybrid-casual (ads + IAP) + updates thường xuyên.

### 5. **Gossip Harbor: Merge & Story (Microfun) – Merge-2 + Narrative**

- **Doanh thu**: >650 triệu USD (2025), peak 67 triệu USD/tháng, vượt Candy Crush ở một số quý.
- **Lý do**: Kết hợp **merge addictive** + **cốt truyện hấp dẫn** (narrative-driven) → retention cao hơn merge thuần. Hybrid monetization (15–20% từ ads).

### Bảng tóm tắt lý do thành công chung (2025–2026)

| Yếu tố                    | Tỷ trọng đóng góp | Ví dụ điển hình          | Lý do hiệu quả                          |
| ------------------------- | ----------------- | ------------------------ | --------------------------------------- |
| **Hybrid Monetization**   | 70–80%            | Royal Match, Candy Crush | Rewarded ads voluntary + IAP cho whales |
| **LiveOps & Events**      | Rất cao           | MONOPOLY GO, Royal Match | Spike revenue + retention dài hạn       |
| **Social / Virality**     | Cao               | MONOPOLY GO              | Người chơi tự kéo bạn bè                |
| **UA & Creative**         | Cao               | Royal Match, MONOPOLY GO | Playable ads + celebrity                |
| **Data-driven Iteration** | Cao               | Royal Match              | A/B test liên tục                       |
| **Core Loop Addictive**   | Nền tảng          | Tất cả                   | Dễ chơi – khó master + relaxing         |

**Kết luận quan trọng:**  
Thành công của các game ad-based **không phải nhờ “vắt chanh” bằng ads rác**, mà nhờ **biến rewarded ads thành phần thưởng tự nguyện** + xây dựng **retention dài hạn qua LiveOps và social**. Đây chính là lý do chúng kiếm được hàng trăm triệu đến tỷ USD mà vẫn giữ DAU cao.

Ngược lại với indie/AA premium (Balatro, Lethal Company) – tập trung “value-based & ad-free” – thì phân khúc mobile ad-based lại **kết hợp ads + IAP** để tối ưu volume + depth.
