# UET.MAT1052 — Notebook tuần 09–15

ThS. Hoàng Hữu Bách — BM. Khoa học & Kỹ thuật tính toán - Khoa Công nghệ Thông tin, VNU-UET

Bản **Plotnine**, bổ sung ngày 17/11/2026. Mỗi tuần là một notebook vừa giảng giải vừa tính toán, có lộ trình học trên lớp/tự luyện/đọc sâu, mục lục nhảy tới phần, câu hỏi dự đoán, tính tay, đáp án thu gọn và ô “Thử đổi”. Các ví dụ/bài tập của slide được giữ theo tên gốc; không tự gán mã hay mức độ mà slide không có.

| Tuần | Notebook | Nội dung |
|---|---|---|
| 09 | [Khái quát dữ liệu (5/7): Từ mẫu đến tổng thể và khoảng tin cậy](./W9_TuMauDenTongTheVaKhoangTinCay.ipynb) | Lấy mẫu; chệch/biến thiên; phân phối mẫu; không chệch/vững/hiệu quả; CI trung bình/tỉ lệ và cỡ mẫu; 5 bài CSV thật. |
| 10 | [Khái quát dữ liệu (6/7): Bootstrap và mở đầu kiểm định](./W10_BootstrapVaMoDauKiemDinh.ipynb) | Bootstrap; SE/CI phân vị; nhị thức; 924/20/70 phép gán; Gilbert tái dựng; giới hạn chọn mẫu. |
| 11 | [Khái quát dữ liệu (7/7): Kiểm định hai mẫu, χ² và lực kiểm định](./W11_KiemDinhHaiMauVaChiBinhPhuong.ipynb) | z/t gộp/Welch/t cặp; hai tỉ lệ; F tự chọn; χ² độ phù hợp/độc lập; loại I/II và lực. |
| 12 | [Phân tích Nhân quả (1/2): Kết quả tiềm năng và tác động trung bình](./W12_QuanHeNhanQua.ipynb) | Phản thực; ATE/ATT/ATC; SUTVA/ignorability/positivity; chuẩn hóa; mô phỏng gán ngẫu nhiên. |
| 13 | [Phân tích Nhân quả (2/2): Thiết kế thí nghiệm và nghiên cứu quan sát](./W13_ThietKeThiNghiemVaNghienCuuQuanSat.ipynb) | Hiệu lực; cấp đơn vị; RCT; khối/cụm; A/B; matching; trước–sau, DiD, ITS và phụ thuộc. |
| 14 | [Dự đoán (1/2): Đánh giá và cải thiện dự đoán](./W14_DanhGiaVaCaiThienDuDoan.ipynb) | OLS và gradient descent; kiểm định r/β; R²/RSE/RMSE; phần dư/ảnh hưởng; VIF; chọn biến; tương tác. |
| 15 | [Dự đoán (2/2): Quá khớp và hồi quy logistic](./W15_QuaKhopVaHoiQuyLogistic.ipynb) | Quá khớp; CV/validation/test cuối; sigmoid/odds; logistic; confusion matrix; precision/recall/F1; calibration. |

Hai bản dùng cùng dữ liệu, cùng phần thống kê, cùng bài tập và cùng mã tính toán. Bản Matplotlib/Plotly có hình tĩnh và thanh trượt Plotly ở các hoạt động cỡ mẫu, leverage và ngưỡng phân loại. Bản Plotnine dùng `ggplot`, `aes`, các lớp hình học và facet; thay tham số trong ô rồi chạy lại. Mỗi notebook đã lưu kết quả chạy và hình, nên có thể đọc trước khi mở kernel.

## Mở và chạy

1. Giải nén cả gói, giữ notebook cạnh `datasets/` và `figures/`.
2. Cài các thư viện trong môi trường Python riêng:

```bash
python -m pip install -r requirements_w09_w15.txt
jupyter lab
```

3. Mở bài từ bảng trên, chọn đúng Python kernel rồi **Restart Kernel and Run All Cells**.
4. Đọc và đoán trước khi chạy; mở đáp án sau khi tự làm. Thay tham số theo hướng dẫn và chạy lại các ô phụ thuộc.

Dữ liệu đã đi kèm; notebook không tải dữ liệu hay cài thư viện khi chạy. Đường dẫn sử dụng `DATA = Path('datasets')`. Với Google Colab, cần đưa cả thư mục dữ liệu vào cùng vị trí làm việc hoặc giải nén cả gói trong phiên; các notebook đã kiểm tra trên Jupyter kernel cục bộ, chưa kiểm tra trực tiếp trong Colab. Phiên bản kiểm tra: Python 3.14.6 và các phiên bản gói ghi trong `requirements_w09_w15.txt`; chúng là bản ghi môi trường đã chạy, không khẳng định chỉ những phiên bản ấy mới hoạt động.

## Dữ liệu và nguồn

| Tệp | Số dòng | Nội dung và giới hạn |
|---|---:|---|
| `nycflights.csv` | 32.735 | Chuyến bay từ New York năm 2013; `air_time` tính phút. |
| `ames.csv` | 2.930 | Giao dịch nhà Ames 2006–2010; `price` tính USD. |
| `ncbirths.csv` | 1.000 | Ca sinh North Carolina 2004; `weight` tính pound. |
| `offshore_drilling.csv` | 827 | Vị trí ủng hộ/phản đối/chưa ý kiến; giữ cả ba trong mẫu số. Đã bỏ dòng mô tả đầu CSV nguồn. |
| `smoking.csv` | 1.691 | Khảo sát hút thuốc; không tự khẳng định đại diện toàn dân số. |
| `cars.csv` | 50 | Tốc độ mph và quãng đường dừng feet; dữ liệu lịch sử của R `datasets`. |
| `stackloss.csv` | 21 | Dữ liệu vận hành, lấy bản đi kèm Statsmodels; đổi tên cột sang `stack_loss`, `air_flow`, `water_temp`, `acid_conc`. |
| `grad_job.csv` | 20 | Bảng **tổng hợp dùng giảng dạy** của STAT 20, chép lại đúng bảng nguồn; không phải hồ sơ sinh viên thật. |
| `kristen_gilbert_reconstructed.csv` | 1.641 | **Tái dựng** từ bảng 2×2 trong slide; `shift` chỉ là mã dòng giả lập, không phải thời gian. |
| `checkout_prepost.csv` | 4 | Bảng bốn siêu thị trước/sau trong học liệu; không thêm đối chứng giả vào bảng gốc. |

Nguồn dữ liệu: [OpenIntro](https://www.openintro.org/data/), [R: cars](https://stat.ethz.ch/R-manual/R-patched/library/datasets/html/cars.html), [Statsmodels: stackloss](https://www.statsmodels.org/stable/datasets/generated/stackloss.html), [kho gói STAT 20](https://github.com/stat20/stat20data) và bản dịch STAT 20 có sẵn trong dự án. URL, thao tác chuyển đổi và mã SHA-256 của các tệp tải được ghi trong `datasets/W09_W15_SOURCE_MANIFEST.json`.

Hình không có dữ liệu gốc đi kèm được dựng từ **mô phỏng ghi rõ**: tổng thể điểm nhà hàng, tác động cá nhân, vùng chồng lấn, trường/lớp/GPA, độ bền vật liệu, đa thức quá khớp và `qc`. Giữ riêng số liệu bài tính tay của slide với số của mô phỏng mới; không ép mô phỏng thành dữ liệu thực. Ảnh/sơ đồ tham khảo từ học liệu gốc có chú thích nguồn, được nhúng trong notebook và lưu thêm trong `figures/`.

## Đối chiếu slide và đề cương

Slide tuần 09–15 lần lượt có 97, 112, 77, 58, 74, 72, 46 trang. Metadata `source_pages`, `source_exercise`, `source_figure` giúp truy ngược ô về trang nguồn. Tuần 13 trong slide tập trung thiết kế thí nghiệm; notebook vẫn giữ phần này và bổ sung matching/thiết kế thời gian để đáp ứng mục 4.4–4.5 của đề cương. Tuần 12 có phần nối ngắn về gán ngẫu nhiên; tuần 14 có gradient descent để đáp ứng LLO14.1.

Các điểm đã hiệu chỉnh khi chuyển slide:

- SRS yêu cầu mọi tập con cỡ n đồng khả năng; mỗi cá thể có cùng xác suất chưa đủ.
- Biên sai số của CI là đại lượng của quy trình, không phải cận chắc chắn cho sai số đã xảy ra. Cỡ mẫu dự phòng không bảo đảm số phản hồi chính xác.
- VIF phóng đại **phương sai**; sai số chuẩn tăng theo căn VIF. Các phép tính hồi quy dùng hệ số đầy đủ thay vì chia các số đã làm tròn.
- Hệ số/p-value mô tả bằng chứng theo giả định, không khẳng định nguyên nhân hoặc loại trừ chắc chắn ngẫu nhiên. RSE/R² trong mẫu không đo trực tiếp sai số ngoài mẫu.
- Các thiết kế quan sát không có thứ hạng đáng tin tuyệt đối; gán ngẫu nhiên và chọn mẫu ngẫu nhiên hỗ trợ hai câu hỏi khác nhau.
- Dữ liệu dùng chọn mô hình/ngưỡng đóng vai validation; giữ test cuối riêng. CV phải giữ biến đổi trong mỗi fold và giữ cấu trúc thời gian/cụm khi cần.
- Hạ ngưỡng làm recall không giảm trên cùng dữ liệu; precision không bắt buộc thay đổi đơn điệu.

Xem `QA_REPORT.md` và `SOURCE_ALIGNMENT.md` để biết phạm vi kiểm tra, danh mục bài tập và các hình được dựng lại. Đối chiếu trang là kiểm tra truy vết, không tự là chứng minh mọi câu diễn giải đúng; các phép tính nguồn và hình đã được rà riêng.
