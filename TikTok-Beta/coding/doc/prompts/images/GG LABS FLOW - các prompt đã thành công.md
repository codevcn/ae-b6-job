# Các prompt đã thành công khi tạo ảnh với Grok Imagine

## 1. Góc máy camera (Camera Angles)

- **Ảnh** `images/model-29.png` --> `images/model-48.png`:
  A fashion-forward female model crouching low to the ground in a confident pose, one knee bent forward and the other leg folded beneath her body. Her upper body is slightly leaning forward, with one hand resting casually near her knee. She looks down toward the camera with a calm, confident expression. Captured from a dramatic low-angle shot, making the model appear dominant and powerful. Emphasize long legs and perspective distortion from the low viewpoint. The pose should feel natural, stylish, and editorial, commonly seen in street fashion photography. Outfit includes a casual oversized t-shirt, denim shorts, and chunky sneakers. Urban city environment with tall glass skyscrapers, bright blue sky, and modern street elements. Strong daylight, sharp shadows, cinematic composition, commercial fashion photography style, ultra-realistic.

- **Ảnh** `images/model-29.png` --> `images/model-22.png`:
  Transform the provided image into a Profile Shot photograph showing the left-side facial profile of the model, while preserving the exact same street environment and the exact same pose of the model.
  Camera angle: Profile Shot (left profile) — position the camera on the left side of the model, capturing her from a perfect 90-degree side angle so that the left-side facial profile (nose line, lips, chin, and jawline) is clearly visible. The camera should be aligned with the left side of her face, not angled from the front-left or rotating across the scene.
  The model should be looking in the same direction her body is facing, not toward the camera.
  Important requirements:
  Keep the background exactly the same, preserving every object in its original position, shape, and structure without any alteration. Maintain the same street background unchanged, including surrounding buildings, road, and city environment.
  Keep the body pose and posture of the person exactly the same (same leg placement, arm placement, and body orientation).
  Keep the same clothing, hairstyle, and overall composition.
  Only the camera position changes to the left-side profile view.
  Style: photorealistic street fashion photography, professional DSLR quality, natural daylight, realistic shadows, sharp focus, natural skin texture, detailed fabric textures, cinematic color grading, realistic depth of field.

## 2. Cho người mẫu cầm trang phục

Cho cô gái @[cô gái] cầm và giơ sản phẩm @[trang phục] sang bên phải (cho sản phẩm vào 1 cái móc treo), miệng mỉm cười nhẹ.

## 3. Cho người mẫu mặc trang phục

Hãy cho cô gái @[cô gái] mặc trang phục @[trang phục] và cô ấy đứng thẳng tạo dáng chuẩn như người mẫu, biểu cảm vui vẻ, miệng mỉm cười nhẹ (không hé môi), 2 tay cô gái thả lỏng dọc theo cơ thể, background phía sau cô gái là tông nền màu xám.

## 4. Tách trang phục ra một nền riêng

Remove the model and isolate the clothing from the reference image. Also remove any jewelry and accessories from the item and the image. Reconstruct the garment as a standalone fashion product while preserving the exact design, shape, fabric texture, stitching, patterns, colors, and details. The clothing should appear naturally shaped as if worn by an invisible mannequin. Centered front view, symmetrical composition, solid gray background, clean studio setup, soft studio lighting, high detail, professional fashion e-commerce product photography.

## 5. Làm nét ảnh chân dung người

Transform this image into highly photorealistic quality as if captured by a professional DSLR camera with a prime lens. Apply natural lighting with accurate shadows and highlights. Add authentic real-world details including natural skin texture with visible pores, organic surface imperfections, realistic fabric and material properties, and proper depth of field with natural bokeh. Enhance with volumetric lighting, realistic color grading, sharp focus, and physical accuracy. Turn any blurry details into physical, meaningful details. Make the picture 10–20% brighter and more vibrant. Preserve the original facial structure, proportions, identity, and all fine facial details of the person in the image. Preserve the original background exactly as it is, without altering, replacing, or reimagining any background elements. Output should appear indistinguishable from real professional photography, with all elements following real-world physics and a natural appearance at maximum resolution.

## 6. Tạo ảnh tạo dáng cho người mẫu (sau khi đã có ảnh sản phẩm & ảnh người mẫu)

### Trong 1 cửa hàng thời trang

> Input là [ảnh người mẫu (mang giày)] và [ảnh trang phục], sau đó dùng câu prompt bên dưới.
> Xem xét chỉnh lại prompt thay kiểu giày.

Create an image using the face and body from @[model image], keeping the face 100% unchanged and without altering or modifying any facial features in any way. The model must wear the exact outfit shown in @[outfit image], accurately reproducing the design, material, colors, patterns, and overall fit of the clothing.

Fashion photo inside a high-end, modern, minimalist fashion store, with a clean and luxurious space, very bright indoor lighting.
Medium camera angle, at eye level / body level with the model, creating the feeling that the viewer is standing directly in front of the girl, with a natural perspective, not a low angle, not a high angle. Shot in 3/4 subject body to near full body, vertical composition, with the subject standing in the center of the frame.

The model wears an outfit similar to the reference image and a pair of white ankle boots, standing straight with balanced weight, with a slight natural shift in the hips. One hand is placed on the hip, while the other hangs naturally along the body. Her face is relaxed, with a gentle closed-mouth smile, and her eyes are looking at the phone.

The lighting is very bright and evenly spread throughout the entire room, making the subject stand out, with clear clothing details. The background is a high-end fashion store with softly blurred clothing racks behind her, clean, neat, and not visually cluttered.

Super realistic style, high-end fashion photography, realistic skin texture, natural body proportions, eye-level perspective, clean composition, sharp focus on subject, soft background blur, premium indoor lighting.

- **Nếu muốn loại bỏ chi tiết về điện thoại thì thêm câu sau**:
  Remove any phone detail from the image, the model is not holding a phone.

### Cầm điện thoại trước gương

> Input là [ảnh người mẫu] và [ảnh trang phục], sau đó dùng câu prompt bên dưới.

Tạo một hình ảnh sử dụng khuôn mặt cơ thể như hình @[hình người mẫu] và giữ nguyên 100% khuôn mặt, tuyệt đối không chỉnh sửa hay thay đổi bất kỳ đặc điểm nào. Dáng người thon gọn, da trắng hồng tự nhiên, chất lượng cao, chi tiết sắc nét và mặc trang phục như hình @[hình trang phục].
Tư thế: Selfie trước gương, tay phải cầm điện thoại, điện thoại che một phần má và mắt phải.

- Cơ thể:
  - Xoay nhẹ góc 3/4
  - Nhấn đường cong cơ thể và vòng eo.

- Đầu & ánh mắt:
  - Nhìn vào màn hình điện thoại iphone 16
  - Ốp màu hồng bụi (dusty pink) hoặc ảnh phản chiếu
  - Biểu cảm trung tính nhưng cuốn hút.

- Bối cảnh & Không gian:
  - Trong phòng ngủ.

- Phông nền:
  - Tối giản
  - Tường màu sáng (trắng ngà, xám nhạt hoặc kem)
  - Không có vật thể gây phân tán.

- Ánh sáng & Bóng:
  - Ánh sáng tự nhiên từ bên trái ảnh (bên phải cơ thể)

- Hiệu ứng:
  - Highlight rõ ở sống mũi, môi, xương quai xanh, tay áo phải
  - Da sáng, glow hồng trắng.

- Bóng:
  - Bóng mềm ở bên trái khuôn mặt và eo
  - Tạo chiều sâu, không bị phẳng.

- Tông màu & không khí:
  - Ấm
  - Độ tương phản thấp
  - Cảm giác film nhẹ / vintage.

- Mood:
  - Riêng tư, thư giãn
  - Sexy nhẹ, hiện đại, thời trang.

- Góc máy:
  - Ngang tầm mắt, hơi chúc xuống nhẹ.

- Khung hình:
  - Medium shot (nửa người)
  - Tập trung phần thân trên và eo.

- Tỉ lệ khung hình 9:16.

## 7. Cho người mẫu mang túi xách

> Xem xét prompt nên cho người mẫu cầm túi xách bên tay trái hay phải để khi làm video ko bị bất tiện.

### 7.1. Đã có ảnh túi xách

> Input là [ảnh người mẫu với 1 background cụ thể] và [ảnh túi xách với tông nền xám], rồi dùng câu prompt bên dưới.

- **Tiếng Việt**:
  Cho người mẫu @[người mẫu] mang túi xách @[túi xách], miệng người mẫu mỉm cười nhẹ, mắt nhìn về phía trước, đứng thẳng tạo dáng chuẩn như người mẫu, giữ nguyên chi tiết background phía sau.
- **Tiếng Anh**:
  Have the model @[người mẫu] carry the handbag @[túi xách], with a slight smile, eyes looking forward, standing straight in a standard model pose, while keeping all background details unchanged.

### 7.2. Chưa có ảnh túi xách nhưng có ảnh người mẫu

> Input là [ảnh người mẫu với 1 background cụ thể], rồi dùng câu prompt bên dưới.

Make the model in the image carry a modern women's handbag that matches the outfit she is wearing.

## 8. Cho người mẫu mặc trang phục và mang giày

cho người mẫu @[người mẫu] mặc trang phục @[trang phục] và mang giày @[giày], giữ nguyên background phía sau người mẫu và giữ nguyên tư thế của người mẫu.

## 9. Cho người mẫu đi trên máy đi bộ mini

> Input là [ảnh người mẫu của minh] và [ảnh người mẫu khác đang đi trên máy đi bộ mini].

Tạo ảnh người mẫu với vóc dáng cơ thể, chi tiết khuôn mặt, chiều cao và trang phục như hình @[hình người mẫu] đang sải bước đầy tự tin trên chiếc máy đi bộ mini đặt giữa không gian bối cảnh tại phòng khách, bối cảnh phòng khách đơn giản và ngẫu nhiên. Góc và hướng của chiếc máy đi bộ mini, tư thế hướng người của người mẫu giống như hình @[hình người mẫu khác đang đi trên máy đi bộ]. Trọng tâm bức hình dồn vào tư thế sải chân dứt khoát như đang sải bước trên sàn catwalk của người mẫu, người mẫu với 2 tay buông thõng tự nhiên, kết hợp cùng khuôn mặt hướng thẳng vào ống kính tạo nên phong thái cực kỳ năng động và cuốn hút. Tổng thể bức ảnh mang đến một sự tương phản thú vị và thời thượng. Chất lượng hình ảnh 4K.
