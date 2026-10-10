# Hướng dẫn vẽ biểu đồ bằng Matplotlib / Plotly

ThS. Hoàng Hữu Bách — BM. Khoa học & Kỹ thuật tính toán - Khoa Công nghệ Thông tin, VNU-UET

Tài liệu thực hành của branch `matplotlib-plotly`. Các đoạn code dưới đây dùng dữ liệu thật `penguins.csv` của học phần. Chạy lần lượt từ phần 1 trong cùng một notebook; các phần sau dùng các biến đã tạo trước. Đường dẫn dữ liệu tính từ thư mục gốc repository.

Với Matplotlib, tạo `Figure` và `Axes`, rồi truyền dữ liệu vào từng lệnh của hệ trục. Với Plotly, tạo hình từ data frame hoặc ghép các trace, sau đó đặt nhãn và bộ điều khiển. Những lựa chọn dữ liệu, ánh xạ và dạng hình học vẫn theo phần Ngữ pháp đồ họa trong W3.

Khi sửa hình, giữ cùng dữ liệu để so sánh. Ô mô phỏng trong các bài học có thể lấy mẫu mới khi chạy lại; dùng cùng seed và chạy từ kernel sạch để tái lập mẫu. Màu, nhãn hoặc độ trong suốt giúp đọc hình; thay chúng không làm thay đổi phép tính thống kê.

## 1. Chuẩn bị bảng và thư viện

`plt` tạo hình và hệ trục của Matplotlib. `px` nhận bảng cùng tên cột; `go` cho phép dựng từng trace của Plotly. Các ví dụ dùng cùng mẫu đã lọc để so sánh cách vẽ.

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

import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
```

## 2. Biểu đồ phân tán với Figure và Axes

`fig` là toàn bộ khung hình; `ax` là hệ trục nhận dữ liệu. Vòng lặp lọc theo loài, rồi truyền các mảng x và y cùng màu cố định cho mỗi nhóm. `s` là diện tích điểm, còn `alpha` là độ trong suốt. Thử tăng `s` lên 40; tọa độ dữ liệu vẫn giữ nguyên.

```python
fig, ax = plt.subplots(figsize=(7, 4))
for loai, bang in chim.groupby("species", observed=True):
    ax.scatter(bang["flipper_length_mm"], bang["body_mass_g"],
               s=22, alpha=0.65, color=mau[loai], label=loai)
ax.set(xlabel="Chiều dài cánh (mm)", ylabel="Khối lượng (g)",
       title="Cánh và khối lượng chim cánh cụt")
ax.legend(title="Loài")
fig.tight_layout()
plt.show()
```

## 3. Biểu đồ cột từ bảng đếm

`ax.bar` nhận vị trí nhóm và số đếm đã tính. Nó không tự đếm các hàng trong bảng `chim`. Thử đối chiếu độ dài từng cột với bảng `dem` để kiểm tra biểu đồ trước khi diễn giải.

```python
dem = chim.groupby("species", observed=True).size().reset_index(name="so_chim")
fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(dem["species"], dem["so_chim"], color=[mau[n] for n in dem["species"]])
ax.set(xlabel="Loài", ylabel="Số chim đủ dữ liệu", title="Đếm chim trong mẫu đang dùng")
fig.tight_layout()
display(dem)
plt.show()
```

## 4. Histogram và các cận chia

`bins` là mảng cận khoảng, không phải số đếm. Các cận ở đây phủ toàn bộ mẫu và cách nhau 5 mm. Với mặc định của `hist`, trục y là số quan sát; khi đặt `density=True`, trục y là mật độ và diện tích được chuẩn hóa.

```python
can = np.arange(30, 70, 5)
fig, ax = plt.subplots(figsize=(7, 4))
ax.hist(chim["bill_length_mm"], bins=can, color="#0072B2", edgecolor="white")
ax.set(xlabel="Chiều dài mỏ (mm)", ylabel="Số chim", title="Histogram với khoảng rộng 5 mm")
fig.tight_layout()
plt.show()
```

## 5. So nhóm trên nhiều hệ trục

Mỗi `ax` nhận dữ liệu của một loài. `sharex=True` và `sharey=True` giữ cùng thang trục để so sánh độ lớn và vị trí. Đây là cách triển khai thao tác chia ô trong phần Ngữ pháp đồ họa bằng Matplotlib.

```python
fig, axes = plt.subplots(1, len(nhom), figsize=(10, 3.5), sharex=True, sharey=True)
for ax, loai in zip(axes, nhom):
    bang = chim.loc[chim["species"] == loai]
    ax.scatter(bang["flipper_length_mm"], bang["body_mass_g"],
               s=22, alpha=0.65, color=mau[loai])
    ax.set(title=loai, xlabel="Chiều dài cánh (mm)")
axes[0].set_ylabel("Khối lượng (g)")
fig.tight_layout()
plt.show()
```

## 6. PMF và CDF rời rạc

Cột PMF nhận các xác suất đã tính. `step(where="post")` giữ giá trị sau điểm nhảy trên đoạn nằm ngang tiếp theo. Kiểm tra các mức tích lũy 0.04, 0.36 và 1. Dùng đường thẳng nối ba giá trị sẽ mô tả sai CDF của phân phối rời rạc này.

```python
x = np.array([0, 1, 2])
p = np.array([0.04, 0.32, 0.64])
F = p.cumsum()
assert np.isclose(p.sum(), 1)
fig, axes = plt.subplots(1, 2, figsize=(9, 3.5))
axes[0].bar(x, p, width=0.6)
axes[0].set(xlabel="Giá trị X", ylabel="Xác suất", title="PMF", xticks=x)
axes[1].step([-0.5, 0, 1, 2, 2.5], [0, 0.04, 0.36, 1, 1], where="post")
axes[1].scatter(x, F)
axes[1].set(xlabel="Ngưỡng t", ylabel="F(t)", title="CDF", xticks=x)
fig.tight_layout()
plt.show()
```

## 7. Vẽ đường hồi quy đã tính

`np.polyfit` tính hệ số; `ax.plot` chỉ vẽ đường từ các tọa độ đã tính. Lưới x được sắp tăng dần để nối điểm đúng thứ tự. Quan hệ trên mẫu gộp có thể khác trong từng loài; đường này mô tả liên hệ và không chứng minh nhân quả.

```python
x = chim["flipper_length_mm"].to_numpy()
y = chim["body_mass_g"].to_numpy()
b1, b0 = np.polyfit(x, y, 1)
luoi = np.linspace(x.min(), x.max(), 100)
fig, ax = plt.subplots(figsize=(7, 4))
ax.scatter(x, y, s=22, alpha=0.4)
ax.plot(luoi, b0 + b1 * luoi, color="#D55E00")
ax.set(xlabel="Chiều dài cánh (mm)", ylabel="Khối lượng (g)",
       title="Đường hồi quy trên toàn mẫu")
fig.tight_layout()
print("b0, b1:", round(b0, 3), round(b1, 3))
plt.show()
```

## 8. Tô diện tích dưới đường mật độ

`fill_between` tô từ 0 tới đường mật độ trong miền chọn. Giá trị in ra khoảng 0.682689 là diện tích, không phải chiều cao tại một điểm. Đây là cách đọc các miền xác suất trong W7.

```python
luoi = np.linspace(-4, 4, 401)
f = norm.pdf(luoi)
mien = (luoi >= -1) & (luoi <= 1)
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(luoi, f)
ax.fill_between(luoi[ mien ], 0, f[ mien ], color="#0072B2", alpha=0.3)
ax.set(xlabel="Giá trị", ylabel="Mật độ", title="Chuẩn tắc: miền từ -1 đến 1")
fig.tight_layout()
print("Xác suất trong miền:", round(norm.cdf(1) - norm.cdf(-1), 6))
plt.show()
```

## 9. Plotly: trace, rê chuột và thanh trượt

Plotly Express tạo các trace từ bảng và tên cột; rê chuột xem thêm chiều dài mỏ. Histogram tiếp theo dùng số đếm tính trước bởi NumPy, mỗi trace là một cách chia khoảng. Thanh trượt đổi `visible` và tiêu đề qua `steps`, nên dùng cùng mẫu ở mọi trạng thái. Bộ điều khiển này không gọi lại Python khi kéo; nơi xem cần hỗ trợ Plotly JavaScript.

```python
hinh_chim = px.scatter(chim, x="flipper_length_mm", y="body_mass_g", color="species",
                        color_discrete_map=mau, hover_data=["bill_length_mm"],
                        labels={"flipper_length_mm": "Chiều dài cánh (mm)",
                                "body_mass_g": "Khối lượng (g)", "species": "Loài"})
hinh_chim.show()

cac_do_rong = [2, 5, 10]
mac_dinh = 5
hinh = go.Figure()
for do_rong in cac_do_rong:
    can = np.arange(30, 70 + do_rong, do_rong)
    so_dem, can = np.histogram(chim["bill_length_mm"], bins=can)
    hinh.add_trace(go.Bar(x=(can[:-1] + can[1:]) / 2, y=so_dem,
                          width=np.diff(can), name=f"{do_rong} mm",
                          visible=(do_rong == mac_dinh)))
buoc = [dict(method="update", label=str(do_rong),
             args=[{"visible": [v == do_rong for v in cac_do_rong]},
                   {"title": {"text": f"Histogram: khoảng rộng {do_rong} mm"}}])
        for do_rong in cac_do_rong]
hinh.update_layout(title={"text": "Histogram: khoảng rộng 5 mm"},
                   xaxis_title="Chiều dài mỏ (mm)", yaxis_title="Số chim", showlegend=False,
                   sliders=[dict(active=cac_do_rong.index(mac_dinh), steps=buoc,
                                 currentvalue={"prefix": "Độ rộng (mm): "})])
hinh.show()
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

[Matplotlib: Figure và Axes](https://matplotlib.org/stable/users/explain/quick_start.html), [Plotly: tạo và cập nhật hình](https://plotly.com/python/creating-and-updating-figures/).
