# Threat Model - Lab 6 AES-CBC Socket

## Thông tin nhóm

- Thành viên 1: Trần Đình Khiêm
- Thành viên 2: La Văn Hải

## Assets

Để hoàn thiện file Threat Model này một cách chuyên nghiệp và giúp Khiêm "xanh" luôn phần nội dung báo cáo, bạn có thể điền theo gợi ý sát với thực tế bài Lab như sau:

Threat Model - Lab 6 AES-CBC Socket
Thông tin nhóm
Thành viên 1: Trần Đình Khiêm

Thành viên 2: La Văn Hải

Assets
Các tài sản (Assets) quan trọng cần được bảo vệ trong hệ thống bao gồm:

Plaintext (Nội dung gốc): Thông tin nhạy cảm từ sample_input.txt cần được giữ bí mật.

AES Key & IV: Thành phần cốt lõi để mã hóa và giải mã dữ liệu. Nếu mất Key, tính bí mật của toàn bộ hệ thống sẽ bị phá vỡ.

Ciphertext: Dữ liệu đã mã hóa đang truyền trên kênh DATA_PORT, cần đảm bảo tính toàn vẹn (không bị sửa đổi).

Logs: Các file nhật ký trong thư mục logs/ chứa vết chạy của hệ thống, không nên lộ các thông tin nhạy cảm như Key thật.

## Attacker model

TĐối tượng tấn công (Attacker) trong kịch bản này được giả định là:

Network Sniffer: Kẻ tấn công cùng mạng LAN, có khả năng sử dụng các công cụ như Wireshark để bắt gói tin trên cả KEY_PORT và DATA_PORT.

Man-in-the-Middle (MitM): Kẻ đứng giữa có khả năng chặn bắt và chỉnh sửa (Tamper) các byte trong ciphertext trước khi nó tới được Receiver.

Local Adversary: Kẻ có quyền truy cập trái phép vào máy tính để đọc các file log hoặc file output tạm thời.

## Threats

Hệ thống hiện tại đối mặt với các mối đe dọa cụ thể:

Key Disclosure (Lộ khóa): Do Key và IV được gửi dưới dạng plaintext qua KEY_PORT. Kẻ tấn công chỉ cần bắt gói tin ở cổng này là có thể giải mã toàn bộ dữ liệu ở cổng data.

Ciphertext Tampering (Chỉnh sửa dữ liệu): Chế độ AES-CBC không có cơ chế kiểm tra tính toàn vẹn (Integrity). Kẻ tấn công có thể thay đổi một vài byte trong ciphertext, dẫn đến việc Receiver giải mã ra dữ liệu sai lệch hoặc gây lỗi hệ thống.

No Authentication (Thiếu xác thực): Receiver không có cơ chế xác minh danh tính của Sender. Bất kỳ ai cũng có thể kết nối tới KEY_PORT và DATA_PORT để gửi dữ liệu giả mạo.

Log Leakage: Việc ghi lại toàn bộ quá trình mã hóa vào file log có thể vô tình làm lộ khóa đối xứng nếu không được phân quyền truy cập file chặt chẽ.

## Mitigations

Các biện pháp giảm thiểu rủi ro cần áp dụng:

Bảo vệ kênh khóa: Trong thực tế, không bao giờ gửi Key/IV plaintext. Cần sử dụng các giao thức trao đổi khóa an toàn như Diffie-Hellman hoặc mã hóa khóa bằng RSA (Asymmetric Encryption).

Sử dụng Mã hóa xác thực (Authenticated Encryption): Thay thế AES-CBC bằng AES-GCM để vừa mã hóa vừa đảm bảo tính toàn vẹn của dữ liệu (chống Tampering).

Thiết lập TLS/SSL: Sử dụng thư viện ssl của Python để bọc các socket lại, tạo ra một đường truyền mã hóa an toàn cho cả Key và Data.

Cơ chế chống Replay: Thêm Timestamp hoặc Nonce vào gói tin để Receiver có thể từ chối các gói tin cũ bị gửi lại.

An toàn log: Cần loại bỏ việc in Key/IV ra log trong môi trường production và thực hiện phân quyền (Permission) cho thư mục logs/.
## Residual risks

Rủi ro còn lại lớn nhất là hệ thống này hiện tại chỉ mang tính chất mô phỏng học tập. Ngay cả khi code chạy đúng logic AES, việc tách kênh mà không có mã hóa lớp dưới (Transport Layer Security) và thiếu cơ chế xác thực hai chiều vẫn khiến hệ thống dễ bị tổn thương trước các cuộc tấn công bắt gói tin và giả mạo danh tính trong môi trường mạng thực tế.