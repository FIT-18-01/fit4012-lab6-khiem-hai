# Report 1 page - Lab 6 AES-CBC Socket

## Thông tin nhóm

- Thành viên 1: Trần Đình Khiêm
- Thành viên 2: La Văn Hải

## Mục tiêu

Mục tiêu của bài lab là xây dựng một hệ thống truyền tin bảo mật cơ bản giữa Sender và Receiver thông qua giao thức TCP Socket. Trong đó, dữ liệu được mã hóa bằng thuật toán AES-CBC kết hợp với PKCS#7 padding để đảm bảo tính bí mật. Bài lab cũng hướng tới việc thực hành thiết kế kiến trúc tách biệt giữa kênh truyền khóa (Key Channel) và kênh truyền dữ liệu (Data Channel), đồng thời đánh giá các lỗ hổng bảo mật tiềm tàng thông qua mô hình Threat Model.

## Phân công thực hiện

Trần Đình Khiêm: Phụ trách lập trình sender.py, xây dựng module mã hóa aes_socket_utils.py và viết hệ thống tests/ để kiểm thử các trường hợp lỗi padding/sai key.

La Văn Hải: Phụ trách lập trình receiver.py, xử lý đa luồng socket, quản lý hệ thống logs và hoàn thiện báo cáo threat-model-1page.md.

Phần làm chung: Thiết kế cấu trúc giao thức (protocol header), thực hiện demo chạy thực tế và phản hồi peer-review.
## Cách làm

Hệ thống được triển khai trên nền tảng Python:

AES-CBC: Sử dụng thư viện pycryptodome, mã hóa dữ liệu theo khối 16 bytes.

Padding: Áp dụng chuẩn PKCS#7 để bù dữ liệu cho đủ kích thước khối trước khi mã hóa.

Giao thức truyền: Sử dụng Header 4 bytes (struct.pack('>I', length)) để báo trước độ dài dữ liệu, giúp Receiver biết chính xác số lượng bytes cần nhận từ socket buffer.

Kênh truyền: Sender gửi Key/IV qua KEY_PORT trước, sau đó mới gửi Ciphertext qua DATA_PORT để Receiver có đủ thông tin giải mã.

## Kết quả

Chạy demo: Hệ thống truyền tin thành công, file sample_output.txt trùng khớp 100% với nội dung sample_input.txt.

Minh chứng: Các file log trong thư mục logs/ ghi nhận chi tiết quá trình bắt tay (handshake), trao đổi khóa và các bước giải mã thành công.

Kiểm thử: Toàn bộ 6/6 test cases (bao gồm test sai key và test can thiệp dữ liệu - tampering) đều đạt trạng thái Passed trên hệ thống Pytest.

## Kết luận

Về kỹ thuật: Hiểu rõ cách hoạt động của chế độ CBC và tầm quan trọng của việc quản lý Vector khởi tạo (IV) cũng như Padding trong mã hóa khối.

Về bảo mật: Nhận thấy rằng dù có mã hóa AES mạnh, hệ thống vẫn không an toàn nếu kênh truyền khóa (Key Channel) không được bảo vệ. Việc gửi Key/IV ở dạng plaintext khiến hệ thống dễ bị tấn công Sniffing, cho thấy cần áp dụng thêm các phương thức như RSA hoặc Diffie-Hellman trong thực tế.
