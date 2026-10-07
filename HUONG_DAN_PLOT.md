# Hướng dẫn vẽ biểu đồ bằng Plotnine

ThS. Hoàng Hữu Bách — BM. Khoa học & Kỹ thuật tính toán - Khoa Công nghệ Thông tin, VNU-UET

Tài liệu thực hành của branch `plotnine`. Các đoạn code dưới đây dùng dữ liệu thật `penguins.csv` của học phần. Chạy lần lượt từ phần 1 trong cùng một notebook; các phần sau dùng các biến đã tạo trước. Đường dẫn dữ liệu tính từ thư mục gốc repository.

Bắt đầu bằng bảng dữ liệu, chọn tên cột trong `aes`, rồi thêm lớp `geom_*` phù hợp. Thêm facet khi cần so nhóm, `labs` để đặt nhãn và `theme` để định dạng. Hướng dẫn này triển khai các thành phần Ngữ pháp đồ họa đã học; phần lý thuyết và bài tập trong W3 giữ nguyên.

Khi sửa hình, giữ cùng dữ liệu để so sánh. Ô mô phỏng trong các bài học có thể lấy mẫu mới khi chạy lại; dùng cùng seed và chạy từ kernel sạch để tái lập mẫu. Màu, nhãn hoặc độ trong suốt giúp đọc hình; thay chúng không làm thay đổi phép tính thống kê.

## 1. Chuẩn bị bảng và thư viện

Một hàng là một con chim. Chỉ giữ các hàng đủ dữ liệu cho cả bộ ví dụ để phép so sánh dùng cùng mẫu. `p9` là tên viết tắt của Plotnine.

```python
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import norm
from IPython.display import display

# Mở JupyterLab tại thư mục repository để dùng đường dẫn này.
chim = pd.read_csv(Path("datasets") / "penguins.csv")
chim = chim.dropna(subset=["species", "flipper_length_mm", "body_mass_g", "bill_length_mm"])
nhom = sorted(chim["species"].unique())
mau = dict(zip(nhom, ["#0072B2", "#D55E00", "#009E73"]))
print("Số hàng đủ dữ liệu cho các ví dụ:", len(chim))

import plotnine as p9
import ipywidgets as widgets
```

## 2. Biểu đồ phân tán và ánh xạ màu

`aes` nhận tên cột trong bảng. `color="species"` nằm trong `aes` nên màu thay đổi theo loài và có legend. `alpha` và `size` đặt ngoài `aes` nên áp dụng cố định cho mọi điểm. Thử thay `size` từ 1.8 thành 3; vị trí điểm vẫn giữ nguyên.

```python
hinh = (
    p9.ggplot(chim, p9.aes(x="flipper_length_mm", y="body_mass_g", color="species"))
    + p9.geom_point(alpha=0.65, size=1.8)
    + p9.scale_color_manual(values=mau)
    + p9.labs(x="Chiều dài cánh (mm)", y="Khối lượng (g)", color="Loài",
              title="Cánh và khối lượng chim cánh cụt")
    + p9.theme_minimal()
)
display(hinh)
```

## 3. Biểu đồ cột từ bảng đếm

Bảng `dem` đã có số đếm trong `so_chim`, nên dùng `geom_col`. `geom_bar` với mặc định đếm hàng phù hợp với dữ liệu thô; dùng nó trên bảng `dem` sẽ đếm hàng của bảng tóm tắt. Thử đối chiếu độ dài từng cột với bảng in ra.

```python
dem = chim.groupby("species", observed=True).size().reset_index(name="so_chim")
hinh = (
    p9.ggplot(dem, p9.aes(x="species", y="so_chim", fill="species"))
    + p9.geom_col()
    + p9.scale_fill_manual(values=mau)
    + p9.labs(x="Loài", y="Số chim đủ dữ liệu", title="Đếm chim trong mẫu đang dùng")
    + p9.theme_minimal()
    + p9.theme(legend_position="none")
)
display(dem)
display(hinh)
```

## 4. Histogram và độ rộng khoảng

`binwidth=5` chia khoảng rộng 5 mm; `boundary=30` cố định một cận chia và `closed="left"` dùng khoảng đóng trái như quy ước của NumPy/Matplotlib trong các ví dụ này. Histogram này đếm quan sát; diện tích không được chuẩn hóa về 1. Trong W2, một số hình cần cận hoặc mật độ tính sẵn, nên dùng bảng cận và `geom_rect` để giữ đúng phép tính của bài.

```python
hinh = (
    p9.ggplot(chim, p9.aes(x="bill_length_mm"))
    + p9.geom_histogram(binwidth=5, boundary=30, closed="left", fill="#0072B2", color="white")
    + p9.labs(x="Chiều dài mỏ (mm)", y="Số chim", title="Histogram với khoảng rộng 5 mm")
    + p9.theme_minimal()
)
display(hinh)
```

## 5. Facet để so nhóm

Facet lọc các hàng vào từng ô theo `species`, rồi dùng cùng lớp điểm. `scales="fixed"` giúp so sánh vị trí và độ lớn trên cùng thang trục. Trong W4, lát cắt 2D cũng dùng cách so sánh theo nhóm hoặc theo một giá trị cố định.

```python
hinh = (
    p9.ggplot(chim, p9.aes(x="flipper_length_mm", y="body_mass_g", color="species"))
    + p9.geom_point(alpha=0.65)
    + p9.scale_color_manual(values=mau)
    + p9.facet_wrap("species", nrow=1, scales="fixed")
    + p9.labs(x="Chiều dài cánh (mm)", y="Khối lượng (g)")
    + p9.theme_minimal()
    + p9.theme(figure_size=(10, 3.5), legend_position="none")
)
display(hinh)
```

## 6. PMF và CDF rời rạc

PMF dùng xác suất đã tính, nên dùng `geom_col`. CDF lấy tổng tích lũy và dùng `geom_step(direction="hv")`. Với phân phối rời rạc này, đoạn nằm ngang đi từ giá trị tại điểm nhảy tới điểm nhảy kế tiếp. Kiểm tra lần lượt các mức 0.04, 0.36 và 1.

```python
pmf = pd.DataFrame({"x": [0, 1, 2], "p": [0.04, 0.32, 0.64]})
pmf["F"] = pmf["p"].cumsum()
assert np.isclose(pmf["p"].sum(), 1)
duong = pd.DataFrame({"x": [-0.5, 0, 1, 2, 2.5], "F": [0, 0.04, 0.36, 1, 1]})
hinh_pmf = (p9.ggplot(pmf, p9.aes("x", "p")) + p9.geom_col(width=0.6)
            + p9.labs(x="Giá trị X", y="Xác suất", title="PMF") + p9.theme_minimal())
hinh_cdf = (p9.ggplot(duong, p9.aes("x", "F"))
            + p9.geom_step(direction="hv")
            + p9.geom_point(data=pmf)
            + p9.labs(x="Ngưỡng t", y="F(t)", title="CDF") + p9.theme_minimal())
display(hinh_pmf)
display(hinh_cdf)
```

## 7. Vẽ đường hồi quy đã tính

`np.polyfit` tính hệ số, rồi bảng `duong` lưu các tọa độ của đường. Lớp đường có bảng và ánh xạ riêng; `inherit_aes=False` làm rõ sự tách biệt đó. Quan hệ của mẫu gộp có thể khác quan hệ trong từng loài; đường này mô tả liên hệ và không chứng minh nhân quả.

```python
x = chim["flipper_length_mm"].to_numpy()
y = chim["body_mass_g"].to_numpy()
b1, b0 = np.polyfit(x, y, 1)
duong = pd.DataFrame({"x": np.linspace(x.min(), x.max(), 100)})
duong["y_du_doan"] = b0 + b1 * duong["x"]
hinh = (
    p9.ggplot(chim, p9.aes("flipper_length_mm", "body_mass_g"))
    + p9.geom_point(alpha=0.4)
    + p9.geom_line(data=duong, mapping=p9.aes("x", "y_du_doan"),
                   inherit_aes=False, color="#D55E00")
    + p9.labs(x="Chiều dài cánh (mm)", y="Khối lượng (g)", title="Đường hồi quy trên toàn mẫu")
    + p9.theme_minimal()
)
print("b0, b1:", round(b0, 3), round(b1, 3))
display(hinh)
```

## 8. Tô diện tích dưới đường mật độ

`geom_area` tô phần dữ liệu của `mien`, còn `geom_line` vẽ toàn bộ đường. Giá trị in ra khoảng 0.682689 là diện tích, không phải chiều cao mật độ tại một điểm. Đây là cách đọc các miền xác suất ở W7.

```python
luoi = np.linspace(-4, 4, 401)
mat_do = pd.DataFrame({"x": luoi, "f": norm.pdf(luoi)})
mien = mat_do.loc[mat_do["x"].between(-1, 1)]
hinh = (
    p9.ggplot(mat_do, p9.aes("x", "f"))
    + p9.geom_area(data=mien, fill="#0072B2", alpha=0.3)
    + p9.geom_line()
    + p9.labs(x="Giá trị", y="Mật độ", title="Chuẩn tắc: miền từ -1 đến 1")
    + p9.theme_minimal()
)
print("Xác suất trong miền:", round(norm.cdf(1) - norm.cdf(-1), 6))
display(hinh)
```

## 9. Thay tham số bằng widget

Widget gọi lại hàm vẽ trên cùng bảng `chim`, nên thay độ rộng không sinh dữ liệu mới. Khi giao diện không hỗ trợ widget, chạy `ve_histogram(2)` hoặc `ve_histogram(10)` trong một ô code. Các callback cần kernel hoạt động; GitHub chỉ hiển thị nội dung tĩnh và PNG đã lưu trong notebook.

```python
def ve_histogram(do_rong):
    hinh = (p9.ggplot(chim, p9.aes("bill_length_mm"))
            + p9.geom_histogram(binwidth=do_rong, boundary=30, closed="left",
                                fill="#0072B2", color="white")
            + p9.labs(x="Chiều dài mỏ (mm)", y="Số chim",
                      title=f"Khoảng rộng {do_rong} mm")
            + p9.theme_minimal())
    display(hinh)

# Lưu một hình ban đầu và hiện bộ điều khiển khi có frontend hỗ trợ.
ve_histogram(5)
bo_dieu_khien = widgets.interactive(
    ve_histogram, do_rong=widgets.SelectionSlider(options=[2, 5, 10], value=5,
                                                description="Độ rộng:"))
display(bo_dieu_khien)
```

## Tìm phần Plot trong các bài học

Các đoạn “Đọc code vẽ” nằm ngay trước ô vẽ tương ứng. Chúng giải thích API thật trong ô, cách thay thuộc tính và cách thao tác với hình.

| Bài | Thực hành Plot |
|---|---|
| [W1](./W1_CauHoiVaDuLieu.ipynb) | Sơ đồ dữ liệu, biểu đồ phân tán, histogram mô phỏng. |
| [W2](./W2_TomTatDuLieu.ipynb) | Biểu đồ đếm và tỉ lệ, histogram, KDE, violin và boxplot. |
| [W3](./W3_NguPhapDoHoaVaDieuKienHoa.ipynb) | Ánh xạ, dạng hình học, chia ô, biến đổi dữ liệu và so nhóm. |
| [W3 TFT](./W3_TFT_NguPhapDoHoaVaDieuKienHoa.ipynb) | Placement, loại lõi, điều kiện hóa và so sánh nhóm trên dữ liệu TFT mô phỏng. |
| [W4](./W4_TuongQuanVaHoiQuyTuyenTinh.ipynb) | Tương quan, đường hồi quy, phần dư và mô hình nhiều biến. |
| [W5](./W5_NenTangVaTinhToanXacSuat.ipynb) | Sơ đồ Venn, cây xác suất và hình so xác suất có điều kiện. |
| [W6](./W6_PhanPhoiVaBienNgauNhien.ipynb) | PMF, CDF và so các phân phối rời rạc. |
| [W7](./W7_KyVongPhuongSaiVaXapXiChuan.ipynb) | Kỳ vọng, phương sai, mật độ và diện tích, mô phỏng tổng và trung bình. |

## Tài liệu API chính thức

[Plotnine: ánh xạ thuộc tính](https://plotnine.org/guide/aesthetic-mappings.html), [các lớp hình học](https://plotnine.org/guide/geometric-objects.html), [facet](https://plotnine.org/guide/facets.html).
