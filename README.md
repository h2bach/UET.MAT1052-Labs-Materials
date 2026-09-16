# UET.MAT1052 - Xác suất thống kê

## Học liệu tương tác bằng Jupyter Notebook

**ThS. Hoàng Hữu Bách**<br>
**BM. Khoa học & Kỹ thuật tính toán - Khoa Công nghệ Thông tin, VNU-UET**

## 1. Giới thiệu học phần

UET.MAT1052 - Xác suất thống kê giúp sinh viên hình thành một quy trình làm việc có căn cứ với dữ liệu: đặt câu hỏi, nhận diện cấu trúc dữ liệu, mô tả và trực quan hóa, xây dựng mô hình, đánh giá mức độ chắc chắn, rồi diễn giải kết quả trong đúng bối cảnh.

Lộ trình môn học đi từ dữ liệu và thống kê mô tả đến xác suất, suy luận thống kê, phân tích nhân quả và dự đoán. Qua đó, sinh viên từng bước phát triển bốn nhóm năng lực chính:

- phân loại, mô tả và trực quan hóa dữ liệu;
- hiểu xác suất, biến ngẫu nhiên và các phân phối thông dụng;
- vận dụng ước lượng, kiểm định và hồi quy;
- phân tích thiết kế nghiên cứu, quan hệ nhân quả và bài toán dự đoán.

Python 3 là ngôn ngữ thực hành chính thức. Notebook có thể chạy bằng JupyterLab trên máy cá nhân hoặc Google Colab trên trình duyệt.

## 2. Lộ trình 15 buổi theo đề cương

| Buổi | Chủ đề | Nội dung chính | Notebook hiện có |
|---:|---|---|---|
| 1 | Các câu hỏi và dữ liệu | Vai trò của dữ liệu; các loại khẳng định; phân loại dữ liệu; đơn vị quan sát, biến và khung dữ liệu | [`W1_CauHoiVaDuLieu.ipynb`](./W1_CauHoiVaDuLieu.ipynb) |
| 2 | Tóm tắt dữ liệu (1/3) | Bảng liên hợp; số đếm và tỉ lệ; dữ liệu phân loại; dữ liệu số; biểu đồ và mô tả phân phối | [`W2_TomTatDuLieu.ipynb`](./W2_TomTatDuLieu.ipynb) |
| 3 | Tóm tắt dữ liệu (2/3) | Ngữ pháp đồ họa; thuộc tính hình ảnh; hình học; điều kiện hóa; lọc; pipeline và phép toán theo nhóm | [`W3_NguPhapDoHoaVaDieuKienHoa.ipynb`](./W3_NguPhapDoHoaVaDieuKienHoa.ipynb) |
| 4 | Tóm tắt dữ liệu (3/3) | Tương quan; hồi quy tuyến tính đơn; hồi quy đa biến; biến phân loại và diễn giải hệ số | [`W4_TuongQuanVaHoiQuyTuyenTinh.ipynb`](./W4_TuongQuanVaHoiQuyTuyenTinh.ipynb) |
| 5 | Khái quát dữ liệu (1/7) | Nền tảng và tiên đề xác suất; sơ đồ Venn; xác suất có điều kiện; độc lập; quy tắc cộng và nhân | Chưa có trong repository |
| 6 | Khái quát dữ liệu (2/7) | Phân phối xác suất; quy tắc đếm; biến ngẫu nhiên rời rạc; nhị thức, siêu bội và hàm phân phối tích lũy | Chưa có trong repository |
| 7 | Khái quát dữ liệu (3/7) | Kỳ vọng; phương sai; độ lệch chuẩn; phân phối liên tục; tổng và trung bình; định lý giới hạn trung tâm | Chưa có trong repository |
| 8 | Kiểm tra giữa kỳ | Ôn tập và đánh giá thống kê mô tả, trực quan hóa, xác suất và các phân phối thông dụng | Chưa có trong repository |
| 9 | Khái quát dữ liệu (5/7) | Mẫu và quần thể; nguồn sai số; phân phối mẫu; khoảng tin cậy cho trung bình và tỉ lệ | Chưa có trong repository |
| 10 | Khái quát dữ liệu (6/7) | Bootstrap; mở đầu kiểm định giả thuyết; p-value và các thành phần của một kiểm định | Chưa có trong repository |
| 11 | Khái quát dữ liệu (7/7) | Kiểm định giả thuyết; một phía và hai phía; mức ý nghĩa; sai lầm loại I và sức mạnh kiểm định | Chưa có trong repository |
| 12 | Phân tích nhân quả (1/2) | Phản thực; thách thức của nhân quả; thí nghiệm ngẫu nhiên và nguyên tắc thiết kế thực nghiệm | Chưa có trong repository |
| 13 | Phân tích nhân quả (2/2) | Nghiên cứu quan sát; thí nghiệm tự nhiên; nhiễu ẩn; thiết kế trước/sau và dữ liệu theo thời gian | Chưa có trong repository |
| 14 | Dự đoán (1/2) | Khái niệm dự đoán; hồi quy tuyến tính; đánh giá và cải thiện mô hình dự đoán | Chưa có trong repository |
| 15 | Dự đoán (2/2) | Quá khớp; tập huấn luyện và tập kiểm tra; hồi quy logistic | Chưa có trong repository |

## 3. Học liệu hiện có

| Tuần | Trọng tâm thực hành | Dữ liệu tiêu biểu | Mở trên Colab |
|---|---|---|---|
| [Tuần 1 - Câu hỏi và dữ liệu](./W1_CauHoiVaDuLieu.ipynb) | Bốn loại khẳng định; đơn vị quan sát, biến, giá trị; dữ liệu số và phân loại; cấu trúc data frame; giới hạn của dữ liệu | `seattlepets`, `email50`, `loan50`, `mcu_films`, `penguins` | [Mở W1 bằng Colab](https://colab.research.google.com/github/h2bach/UET.MAT1052-Labs-Materials/blob/main/W1_CauHoiVaDuLieu.ipynb) |
| [Tuần 2 - Tóm tắt dữ liệu](./W2_TomTatDuLieu.ipynb) | Bảng đếm và bảng liên hợp; tỉ lệ có điều kiện; histogram, density, violin, boxplot; trung bình, trung vị, mốt, phương sai, độ lệch chuẩn và IQR | `penguins`, `loans`, `loan50`, `gpa_study_hours` | [Mở W2 bằng Colab](https://colab.research.google.com/github/h2bach/UET.MAT1052-Labs-Materials/blob/main/W2_TomTatDuLieu.ipynb) |
| [Tuần 3 - Ngữ pháp đồ họa và điều kiện hóa](./W3_NguPhapDoHoaVaDieuKienHoa.ipynb) | Dữ liệu - ánh xạ - hình học; lọc; pipeline; `groupby`; tóm tắt theo nhóm; phân phối biên và có điều kiện; nghịch lý Simpson | `penguins`, `arbuthnot`, `msleep` | [Mở W3 bằng Colab](https://colab.research.google.com/github/h2bach/UET.MAT1052-Labs-Materials/blob/main/W3_NguPhapDoHoaVaDieuKienHoa.ipynb) |
| [Tuần 4 - Tương quan và hồi quy tuyến tính](./W4_TuongQuanVaHoiQuyTuyenTinh.ipynb) | Biểu đồ phân tán; tương quan Pearson; hồi quy đơn và đa biến; phần dư; bình phương tối thiểu; ngoại suy; biến chỉ báo; nhiễu và giới hạn của diễn giải nhân quả | `poverty_mo_phong`, `allbacks`, `zagat` | [Mở W4 bằng Colab](https://colab.research.google.com/github/h2bach/UET.MAT1052-Labs-Materials/blob/main/W4_TuongQuanVaHoiQuyTuyenTinh.ipynb) |

Các notebook sử dụng `numpy`, `pandas`, `matplotlib`, `scipy`, `plotly` và `statsmodels`. Đồ thị Plotly hỗ trợ interactive learning đối với các dữ liệu số/hình ảnh có thể thay đổi được, bộ điều khiển và hình 3D; trải nghiệm hiển thị tương tác tốt nhất khi máy có kết nối Internet.

Các notebook đọc dữ liệu bằng đường dẫn tương đối `datasets/<tên-file>`. Vì vậy, hãy giữ nguyên cấu trúc thư mục và khởi động JupyterLab từ thư mục gốc của repository. Không nên chép riêng notebook sang một thư mục khác nếu chưa điều chỉnh đường dẫn dữ liệu và hình ảnh.

## 4. Bắt đầu nhanh

### Lấy học liệu

Nếu đã cài Git:

```bash
git clone https://github.com/h2bach/UET.MAT1052-Labs-Materials.git
cd UET.MAT1052-Labs-Materials
```

Nếu chưa dùng Git, tải file ZIP từ [trang repository](https://github.com/h2bach/UET.MAT1052-Labs-Materials), giải nén, sau đó mở thư mục vừa giải nén.

### Tạo môi trường khuyến nghị

Sau khi cài Anaconda, mở **Anaconda Prompt** trên Windows hoặc **Terminal** trên macOS và chạy một lần:

```bash
conda create -n uet-mat1052 -c conda-forge python=3.12 jupyterlab numpy pandas matplotlib scipy plotly statsmodels
conda activate uet-mat1052
```

Mỗi lần học, kích hoạt môi trường, chuyển đến thư mục repository rồi mở JupyterLab:

```bash
conda activate uet-mat1052
cd "duong-dan-den/UET.MAT1052-Labs-Materials"
jupyter lab
```

Hướng dẫn từng bước cho Windows, macOS và Google Colab nằm trong phần [Phụ lục](#phụ-lục-a---cài-anaconda-và-jupyterlab-trên-windows).

## 5. Dữ liệu

Repository có 12 file CSV phục vụ trực tiếp cho các hoạt động học tập.

| File | Đơn vị quan sát hoặc nội dung | Dùng ở |
|---|---|---|
| `seattlepets.csv` | 52.519 giấy phép thú cưng tại Seattle | W1 |
| `email50.csv` | 50 thư điện tử với các đặc trưng phục vụ phân tích spam | W1 |
| `mcu_films.csv` | 23 phim thuộc Marvel Cinematic Universe | W1 |
| `penguins.csv` | 344 chim cánh cụt Palmer | W1-W3 |
| `loan50.csv` | 50 khoản vay với nhiều thuộc tính | W1-W2 |
| `loans.csv` | 10.000 khoản vay với bốn biến được chọn | W2 |
| `gpa_study_hours.csv` | GPA và số giờ tự học của 193 sinh viên | W2 |
| `arbuthnot.csv` | Số trẻ được ghi nhận theo năm tại London, 1629-1710 | W3 |
| `msleep.csv` | Thời gian ngủ và đặc trưng của 83 loài động vật có vú | W3 |
| `poverty_mo_phong.csv` | Dữ liệu mô phỏng về tốt nghiệp và nghèo đói của 51 bang | W4 |
| `allbacks.csv` | Thể tích, diện tích, khối lượng và loại bìa của 15 cuốn sách | W4 |
| `zagat.csv` | Đánh giá 168 nhà hàng Ý tại Manhattan | W4 |

Nguồn, giấy phép và ghi chú chi tiết cho từng bộ dữ liệu được trình bày tại [`datasets/README.md`](./datasets/README.md). Dữ liệu mô phỏng được ghi rõ để tránh nhầm với quan sát thực tế.

## 6. Nguồn và ghi nhận

Lộ trình nội dung bám theo học phần UET.MAT1052, biên dịch bởi TS. Hoàng Thị Điệp, TS. Nghiêm Nguyễn Việt Dũng, TS. Lê Thị Hường, Khoa Công nghệ Thông tin, Trường Đại học Công nghệ, ĐHQGHN. Cách tổ chức các chủ đề có tham khảo Stat 20 - *Introduction to Probability and Statistics* của UC Berkeley cùng các tài liệu và bộ dữ liệu thống kê mở.

---

# Phụ lục

## Phụ lục A - Cài Anaconda và JupyterLab trên Windows

### A.1. Chuẩn bị

- Dùng Windows 64-bit còn được Anaconda hỗ trợ; xem [yêu cầu hệ thống hiện hành](https://www.anaconda.com/docs/getting-started/anaconda/system-requirements).
- Dành tối thiểu khoảng 5 GB dung lượng trống cho Anaconda Distribution, chưa kể dữ liệu cá nhân.
- Nên dùng Chrome, Edge hoặc Firefox phiên bản mới.

### A.2. Cài Anaconda Distribution

1. Mở [trang tải Anaconda](https://www.anaconda.com/download).
2. Chọn **Windows 64-Bit Graphical Installer** của Anaconda Distribution.
3. Mở file `.exe` từ thư mục Downloads.
4. Chọn **Just Me (Recommended)**, trừ khi máy dùng chung và quản trị viên yêu cầu cách khác.
5. Chọn thư mục cài đặt không có dấu, ký tự đặc biệt hoặc khoảng trắng. Nếu tên tài khoản Windows có dấu/khoảng trắng, có thể dùng `C:\anaconda3`.
6. Giữ tùy chọn tạo shortcut. **Không chọn** `Add Anaconda3 to my PATH environment variable`; Anaconda khuyến nghị dùng Anaconda Prompt hoặc Navigator để tránh xung đột với Python khác.
7. Chọn **Install**, chờ cài xong rồi chọn **Finish**.

Hướng dẫn chính thức: [Windows graphical installer - Anaconda](https://www.anaconda.com/docs/getting-started/anaconda/install/windows-gui-install).

### A.3. Kiểm tra cài đặt

Mở Start, tìm **Anaconda Prompt**, sau đó chạy:

```bat
conda list
```

Nếu xuất hiện danh sách gói, Anaconda đã hoạt động.

### A.4. Tạo môi trường cho học phần

Trong Anaconda Prompt, chạy:

```bat
conda create -n uet-mat1052 -c conda-forge python=3.12 jupyterlab numpy pandas matplotlib scipy plotly statsmodels
conda activate uet-mat1052
```

Khi được hỏi `Proceed ([y]/n)?`, nhập `y` rồi nhấn Enter.

### A.5. Mở repository trong JupyterLab

Ví dụ nếu thư mục học liệu nằm trong Downloads:

```bat
cd /d "C:\Users\<ten-cua-ban>\Downloads\UET.MAT1052-Labs-Materials"
jupyter lab
```

Trình duyệt sẽ mở JupyterLab. Trong cột file bên trái, mở notebook theo thứ tự W1, W2, W3, W4. Giữ cửa sổ Anaconda Prompt đang chạy; khi muốn dừng JupyterLab, quay lại cửa sổ đó và nhấn `Ctrl + C`.

Từ lần học sau, chỉ cần:

```bat
conda activate uet-mat1052
cd /d "duong-dan-den\UET.MAT1052-Labs-Materials"
jupyter lab
```

Bạn cũng có thể mở **Anaconda Navigator**, chọn môi trường `uet-mat1052` và chọn **Launch** tại JupyterLab.

## Phụ lục B - Cài Anaconda và JupyterLab trên macOS

### B.1. Xác định loại chip

Mở **Apple menu > About This Mac**:

- nếu thấy Apple M1, M2, M3, M4 hoặc mới hơn, máy dùng **Apple silicon**;
- nếu thấy Intel Processor, máy dùng **Intel**.

Anaconda hiện cung cấp bộ cài mới cho Apple silicon. Việc xây dựng gói mới cho Intel Mac đã dừng; máy Intel có thể dùng [kho bộ cài cũ](https://repo.anaconda.com/archive/) hoặc chuyển sang Google Colab nếu gặp vấn đề tương thích.

### B.2. Cài Anaconda Distribution

1. Mở [trang tải Anaconda](https://www.anaconda.com/download).
2. Với Apple silicon, chọn **64-Bit (Apple silicon) Graphical Installer**.
3. Mở file `.pkg`, chọn **Continue**, đọc và chấp nhận điều khoản nếu đồng ý.
4. Chọn vị trí cài đặt và chọn **Install**. Bộ cài đồ họa mặc định đặt Anaconda tại `/opt/anaconda3`.
5. Sau khi hoàn tất, đóng và mở lại Terminal.

Hướng dẫn chính thức: [macOS graphical installer - Anaconda](https://www.anaconda.com/docs/getting-started/anaconda/install/mac-gui-install).

### B.3. Kiểm tra và tạo môi trường

Mở Terminal rồi chạy:

```bash
conda list
conda create -n uet-mat1052 -c conda-forge python=3.12 jupyterlab numpy pandas matplotlib scipy plotly statsmodels
conda activate uet-mat1052
```

Nếu Terminal báo `conda: command not found`, thử đóng/mở lại Terminal. Với vị trí cài mặc định, có thể chạy:

```bash
source /opt/anaconda3/bin/activate
conda init
```

Sau đó đóng và mở lại Terminal.

### B.4. Mở repository trong JupyterLab

Ví dụ nếu thư mục nằm trong Downloads:

```bash
cd "$HOME/Downloads/UET.MAT1052-Labs-Materials"
jupyter lab
```

JupyterLab sẽ mở trong trình duyệt. Giữ Terminal đang chạy; khi muốn dừng, quay lại Terminal và nhấn `Control + C`.

Bạn cũng có thể mở **Launchpad > Anaconda-Navigator**, chọn môi trường `uet-mat1052` và chọn **Launch** tại JupyterLab.

## Phụ lục C - Dùng Google Colab khi không cài được JupyterLab

[Google Colab](https://colab.research.google.com/) là dịch vụ Jupyter Notebook chạy trên trình duyệt và không yêu cầu cài đặt cục bộ. Cần có tài khoản Google và kết nối Internet.

### C.1. Mở notebook

Cách nhanh nhất là dùng liên kết **Mở bằng Colab** trong bảng [Học liệu hiện có](#3-học-liệu-hiện-có).

Một cách khác:

1. Mở [Google Colab](https://colab.research.google.com/) và đăng nhập.
2. Chọn **File > Upload notebook**.
3. Chọn một file `.ipynb` đã tải về.
4. Chọn **File > Save a copy in Drive** để tạo bản riêng trước khi chỉnh sửa.

### C.2. Lấy dữ liệu đi kèm

Mở notebook riêng lẻ trên Colab không tự động tải thư mục `datasets/` và `figures/`. Trước khi chạy các ô còn lại, thêm một ô mã ở đầu notebook và chạy **một lần**:

```python
%cd /content
!git clone --depth 1 https://github.com/h2bach/UET.MAT1052-Labs-Materials.git
%cd /content/UET.MAT1052-Labs-Materials
```

Sau bước này, các đường dẫn như `datasets/penguins.csv` sẽ hoạt động. Nếu đã clone trong phiên hiện tại, không cần chạy lại lệnh `git clone`.

Nếu Colab báo thiếu thư viện, chạy:

```python
%pip install -q numpy pandas matplotlib scipy plotly statsmodels
```

### C.3. Chạy và lưu kết quả

- Chạy từng ô bằng nút tam giác hoặc `Shift + Enter`.
- Chỉ chọn **Runtime > Run all** sau khi đã đọc và tin cậy mã trong notebook.
- File tải trực tiếp vào máy ảo Colab chỉ tồn tại tạm thời và có thể mất khi phiên hết hạn hoặc bị ngắt.
- Lưu notebook vào Google Drive hoặc tải kết quả về máy trước khi kết thúc.
- Máy ảo, thư viện cài thêm và file cục bộ không tự động đi cùng khi chia sẻ notebook.
- Chỉ gắn Google Drive hoặc cấp quyền truy cập file cho notebook mà bạn tin cậy.

Tài liệu chính thức: [Google Colab FAQ](https://research.google.com/colaboratory/faq.html).

## Phụ lục D - Xử lý lỗi thường gặp

### `ModuleNotFoundError`

Kiểm tra đã kích hoạt đúng môi trường rồi cài lại các thư viện:

```bash
conda activate uet-mat1052
conda install -c conda-forge numpy pandas matplotlib scipy plotly statsmodels
```

### `FileNotFoundError` với file trong `datasets/` hoặc `figures/`

Notebook đang được chạy từ sai thư mục hoặc đã bị tách khỏi repository. Dừng JupyterLab, chuyển đến thư mục gốc `UET.MAT1052-Labs-Materials`, rồi chạy lại `jupyter lab`.

### `jupyter` hoặc `conda` không được nhận diện

- Windows: dùng **Anaconda Prompt**, không dùng Command Prompt thông thường khi mới cài.
- macOS: đóng/mở lại Terminal; nếu cần, thực hiện bước `source /opt/anaconda3/bin/activate` và `conda init` trong Phụ lục B.

### Notebook dùng sai Python kernel

Trong JupyterLab, chọn **Kernel > Change Kernel** và chọn kernel thuộc môi trường `uet-mat1052`, sau đó chọn **Restart Kernel and Run All Cells**.

### Đồ thị Plotly không hiển thị hoặc mất tương tác

Kiểm tra kết nối Internet, chạy lại ô thiết lập Plotly ở đầu notebook và thử làm mới trang JupyterLab. Nếu đang xem bản tĩnh trên GitHub, hãy mở notebook bằng JupyterLab hoặc Colab để sử dụng đầy đủ tương tác.

## Nguồn hướng dẫn kỹ thuật

- [Anaconda - Windows graphical installer](https://www.anaconda.com/docs/getting-started/anaconda/install/windows-gui-install)
- [Anaconda - macOS graphical installer](https://www.anaconda.com/docs/getting-started/anaconda/install/mac-gui-install)
- [Anaconda - System requirements](https://www.anaconda.com/docs/getting-started/anaconda/system-requirements)
- [JupyterLab - Installation](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)
- [Google Colab - Frequently Asked Questions](https://research.google.com/colaboratory/faq.html)
