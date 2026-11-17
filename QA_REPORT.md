# Báo cáo kiểm tra notebook tuần 09–15

ThS. Hoàng Hữu Bách — BM. Khoa học & Kỹ thuật tính toán - Khoa Công nghệ Thông tin, VNU-UET

Ngày bàn giao: 17/11/2026. Kết quả: **PASS, 14/14 notebook**.

| Tuần | Tổng ô MP/PN | Ô code MP/PN | Ví dụ/câu hỏi/bài tập mỗi bản | PNG MP/PN | Chạy từ đầu |
|---|---:|---:|---:|---:|---|
| 09 | 68/67 | 17/16 | 22 | 5/5 | PASS |
| 10 | 64/64 | 19/19 | 14 | 7/7 | PASS |
| 11 | 62/62 | 18/18 | 13 | 6/6 | PASS |
| 12 | 50/50 | 15/15 | 9 | 5/5 | PASS |
| 13 | 70/70 | 21/21 | 12 | 10/10 | PASS |
| 14 | 64/63 | 20/19 | 12 | 7/7 | PASS |
| 15 | 51/50 | 16/15 | 7 | 6/6 | PASS |

Tổng cộng **249 ô code**, **92 kết quả PNG**, **3 đồ thị Plotly** và **89 mục ví dụ/câu hỏi/bài tập nguồn trên mỗi bản**. Bảy PDF nguồn có 536 trang; bảng đối chiếu ghi nhận trang nguồn ở từng phần. Số lượng mục là theo danh mục đã đặt tên trong notebook, không đồng nghĩa một trang PDF là một bài tập riêng.

## Đã kiểm tra

- Chạy từng notebook từ kernel Python mới, tuần tự toàn bộ ô, không cho phép bỏ qua lỗi. Đã kiểm tra cả lỗi sinh trong quá trình hiển thị đối tượng Plotnine, không chỉ trạng thái thực thi ô.
- Đối chiếu notebook đã chạy với **mã biên soạn mới nhất**, tránh giao kết quả cũ sau chỉnh sửa. Mỗi ô code có execution_count liên tục và không có output lỗi.
- Cùng tuần, hai bản có mã tính toán thống kê giống hệt và kết quả số/chuỗi giống nhau; chỉ khác mã vẽ, thiết lập backend và hoạt động tương tác. Đã loại thời gian hiển thị trong summary khỏi phép so sánh chuỗi.
- Notebook đúng schema; không có ký tự điều khiển làm hỏng LaTeX; đáp án đóng/mở đúng khối; attachment có dữ liệu nhúng; toàn bộ ô đánh dấu vẽ có PNG.
- Không có đường dẫn máy cá nhân hoặc tải/cài thư viện trong code học viên. Bản Plotnine không gọi trực tiếp Matplotlib/Plotly.
- Các CSV mới giống nhau giữa hai bản. Kiểm tra số dòng/số đếm và mốc tính từ nguồn: ba CI tuần 09; 286/827 và421/1691; nhị thức62/100; siêu bội4/33; Gilbert; Benford; bảng2×3; ATE/ATT/ATC; siêu thị; hệ số cars; precision/recall.
- Đã xem hình kết xuất của cả14 notebook, sửa nối nhầm hai đuôi, lỗi dodge, thứ tự facet, nhãn dài và sơ đồ sát mép. Đồ thị quá khớp dùng trục log có giải thích để không che các mức RMSE nhỏ.
- Ba output Plotly được kiểm tra cấu trúc Figure hợp lệ; có slider cỡ mẫu, leverage và ma trận validation theo ngưỡng. Không coi việc lưu JSON là bằng chứng đã thao tác trên mọi trình duyệt.
- Gói ZIP được kiểm tra CRC, số notebook, đường dẫn tệp tương đối, attachment và mã SHA-256. Không cần thực thi lại sau khi giải nén vì nội dung notebook và dữ liệu được đối chiếu byte/hash với bản đã chạy.

## Môi trường và giới hạn

Python: `3.14.6 | packaged by Anaconda, Inc. | (main, Jul  9 2026, 14:29:05) [MSC v.1942 64 bit (AMD64)]`. Các phiên bản thư viện nằm trong `requirements_w09_w15.txt`; chi tiết máy kiểm tra và hash nằm trong `qa/VERIFICATION.json` của thư mục biên soạn.

Đã kiểm tra bằng Jupyter kernel cục bộ; chưa chạy trực tiếp trên Colab hoặc từng máy học viên. Ảnh/sơ đồ tham khảo có nguồn; mô phỏng mới không phải dữ liệu thực. Điểm gốc của một số hình trong slide không đi kèm nên phần mô phỏng giữ cơ chế/hình dạng, không khẳng định trùng số liệu gốc; các bảng bài tính tay nguồn vẫn giữ riêng. Giới hạn dữ liệu quan sát, phụ thuộc cụm/thời gian, suy rộng lịch sử và giả định nhân quả được nêu ở đúng bài.

Notebook tuần01–07 không được sửa trong đợt này. Nội dung mới chỉ phục vụ tuần09–15; tuần08 là buổi giữa kỳ.
