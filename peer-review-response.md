# Peer Review Response - Lab 6

## Thông tin
- Nhóm: 18 (Khiêm - Hải)
- Đối tượng review: Lab 6 - AES Socket

## Phản hồi các góp ý
1. **Góp ý về lỗi Encoding**: Nhóm đã ghi nhận lỗi `UnicodeEncodeError` trên Windows và đã khắc phục bằng cách thiết lập `PYTHONIOENCODING=utf-8`.
2. **Góp ý về bảo mật**: Nhóm đồng ý rằng việc truyền Key/IV plaintext là nguy hiểm. Chúng em đã cập nhật phần Threat Model để phân tích sâu hơn về vấn đề này.
3. **Góp ý về Code**: Đã kiểm tra lại hàm `unpad` để đảm bảo không bị lỗi khi dữ liệu nhận được bị trống hoặc sai định dạng.

## Kết luận
Các góp ý đã giúp nhóm hoàn thiện hệ thống truyền tin an toàn hơn và hiểu rõ hơn về các kịch bản tấn công thực tế.