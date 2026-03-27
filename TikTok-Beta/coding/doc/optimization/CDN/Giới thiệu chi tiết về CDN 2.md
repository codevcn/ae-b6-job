CDN (Content Delivery Network) là mạng phân phối nội dung, giúp tăng tốc độ tải trang web và ứng dụng bằng cách phân tán nội dung đến các máy chủ gần người dùng hơn. [aws.amazon](https://aws.amazon.com/vi/what-is/cdn/)

## Giới thiệu chung

CDN là hệ thống gồm nhiều máy chủ được đặt tại các vị trí địa lý khác nhau trên toàn cầu, hoạt động phối hợp để cung cấp nội dung như hình ảnh, video, trang web nhanh chóng và ổn định. [viettelidc.com](https://viettelidc.com.vn/tin-tuc/cdn-la-gi-phan-tich-chuyen-sau-ve-mang-luoi-phan-phoi-noi-dung)
Nó giảm khoảng cách truyền dữ liệu giữa máy chủ gốc và người dùng, cải thiện trải nghiệm trực tuyến cho hàng tỷ người dùng hàng ngày. [vngcloud](https://vngcloud.vn/vi/blog/what-is-a-content-delivery-network-cdn)

## Các khái niệm chính

Origin Server (máy chủ gốc) lưu trữ nội dung chính thức, là nguồn dữ liệu gốc mà CDN lấy để sao chép. [kungfutech.edu](https://kungfutech.edu.vn/posts/huong-dan-su-dung-cdn-khai-niem-va-quy-trinh-hoat-dong)
Edge Server (máy chủ biên) nằm ở các PoP (Point of Presence), cache và phân phối nội dung gần người dùng nhất, giảm độ trễ. [viblo](https://viblo.asia/p/kham-pha-cdn-content-delivery-network-tu-khai-niem-den-thiet-ke-he-thong-gwd43MWQLX9)
Các khái niệm khác bao gồm caching (lưu tạm nội dung), routing (định tuyến yêu cầu) và peering (kết nối mạng tối ưu). [web](https://web.dev/articles/content-delivery-networks?hl=vi)

## Lý do ra đời, bối cảnh trước và sau

CDN ra đời cuối những năm 1990, tiên phong bởi Akamai Technologies năm 1998, để giải quyết "Flash Crowd" – tình trạng quá tải đột biến làm sập website do lưu lượng truy cập tăng vọt. [vnetwork](https://www.vnetwork.vn/news/cdn-la-gi-va-6-loi-ich-dac-biet-cua-cong-nghe-cdn/)
Trước CDN, nội dung chỉ từ một máy chủ trung tâm, gây độ trễ cao, quá tải và gián đoạn khi người dùng xa xôi hoặc đông đúc. [aws.amazon](https://aws.amazon.com/vi/what-is/cdn/)
Sau CDN, tốc độ tải tăng, tính sẵn sàng cao hơn, xử lý lưu lượng lớn toàn cầu mà không sập, như phục vụ 30% lưu lượng web thế giới. [via.org](https://via.org.vn/cmc-cdn-cmc-akamai-cdn)

## Mục tiêu thiết kế & Triết lý

Mục tiêu chính là giảm độ trễ bằng cách đưa nội dung gần người dùng, tăng hiệu suất, khả dụng và bảo mật (chống DDoS, SSL). [viblo](https://viblo.asia/p/kham-pha-cdn-content-delivery-network-tu-khai-niem-den-thiet-ke-he-thong-gwd43MWQLX9)
Triết lý đằng sau tập trung vào phân tán (edge servers), quản lý cache thông minh và định tuyến động để tối ưu toàn cầu, đảm bảo nội dung nhanh, ổn định bất kể vị trí. [web](https://web.dev/articles/content-delivery-networks?hl=vi)
Thiết kế nhấn mạnh scalability (mở rộng), peering mạng và bảo mật để xử lý lưu lượng lớn mà không phụ thuộc máy chủ gốc. [bizflycloud](https://bizflycloud.vn/tin-tuc/pop-cdn-la-gi-20260305155922373.htm)

## Các trường hợp sử dụng phổ biến

CDN phổ biến cho website thương mại điện tử để tải nhanh sản phẩm, hình ảnh; streaming video như Netflix giảm buffer. [vnptai](https://vnptai.io/vi/blog/detail/cdn-la-gi)
Nó dùng cho game online giảm lag, y tế truy cập hồ sơ nhanh, và sự kiện lớn chống quá tải. [tuhoclaptrinh.edu](https://tuhoclaptrinh.edu.vn/cdn-la-gi-va-khi-nao-nen-dung-cdn-cho-website-1097.html)
Các nền tảng như AWS CloudFront, Cloudflare hỗ trợ hàng triệu site với nội dung tĩnh/động toàn cầu. [aws.amazon](https://aws.amazon.com/what-is/cdn/)
