# Kiểm chứng toàn bộ notebook — plotnine

ThS. Hoàng Hữu Bách — BM. Khoa học & Kỹ thuật tính toán - Khoa Công nghệ Thông tin, VNU-UET

Branch `plotnine` có đủ 8 notebook Tuần 1–7 và bản TFT của Tuần 3. Mọi code vẽ dùng backend của branch. Giữ dữ liệu, công thức, lý thuyết Ngữ pháp đồ họa, mã bài tập, cell IDs và metadata nguồn; các đoạn chỉ dẫn code/thao tác được viết theo backend tương ứng.

| Notebook | Ô code đã chạy | PNG | Plotly |
|---|---:|---:|---:|
| [W1_CauHoiVaDuLieu.ipynb](W1_CauHoiVaDuLieu.ipynb) | 28 | 3 | 0 |
| [W2_TomTatDuLieu.ipynb](W2_TomTatDuLieu.ipynb) | 54 | 24 | 0 |
| [W3_NguPhapDoHoaVaDieuKienHoa.ipynb](W3_NguPhapDoHoaVaDieuKienHoa.ipynb) | 43 | 23 | 0 |
| [W3_TFT_NguPhapDoHoaVaDieuKienHoa.ipynb](W3_TFT_NguPhapDoHoaVaDieuKienHoa.ipynb) | 36 | 19 | 0 |
| [W4_TuongQuanVaHoiQuyTuyenTinh.ipynb](W4_TuongQuanVaHoiQuyTuyenTinh.ipynb) | 36 | 20 | 0 |
| [W5_NenTangVaTinhToanXacSuat.ipynb](W5_NenTangVaTinhToanXacSuat.ipynb) | 19 | 8 | 0 |
| [W6_PhanPhoiVaBienNgauNhien.ipynb](W6_PhanPhoiVaBienNgauNhien.ipynb) | 34 | 18 | 0 |
| [W7_KyVongPhuongSaiVaXapXiChuan.ipynb](W7_KyVongPhuongSaiVaXapXiChuan.ipynb) | 32 | 16 | 0 |

Cả 8 notebook đã chạy từ kernel sạch, tổng 282 ô code, không lỗi hoặc stderr trong output. Đã xem các hình lưu; 147 ô code giữ nguyên ở hai backend có cùng kết quả số sau khi chuẩn hóa việc chia output stdout thành nhiều khối. Giữ nguyên 57 tệp dữ liệu/ảnh nguồn. Guide TFT có đủ 77 mục theo từng cell.

Bản Plotnine dùng `aes`, các lớp `geom_*`, facet và lát cắt 2D. Các hoạt động tham số dùng `ipywidgets` hoặc sửa tham số rồi chạy lại; PNG ban đầu được lưu. Bản Matplotlib/Plotly giữ các hình tĩnh và hoạt động tương tác/3D hiện có. Hướng dẫn trong notebook và guide TFT khớp với code của từng bản.

Đã bỏ ký hiệu thừa `<\hat y>` trong công thức SSE của W4 ở cả hai branch để biểu thức là tổng bình phương phần dư chuẩn; phép tính hồi quy giữ nguyên. Những thay đổi Markdown còn lại là cú pháp vẽ và hướng dẫn thao tác, được kiểm tra theo ID và SHA-256 trong [manifest](qa/GRAPHICS_MARKDOWN_CHANGES.json).

Kiểm chứng tại máy; chưa chạy trực tiếp trên Colab và chưa kiểm kéo các widget Plotnine qua frontend. Tương tác cần kernel Jupyter đang chạy. Kết quả hiện tại là [QA toàn bộ notebook](qa/NOTEBOOKS_VALIDATION.json) và [đối chiếu hai backend](qa/NOTEBOOK_BACKEND_PARITY.json).

```bash
python -X utf8 tools/verify_notebooks.py
python -X utf8 tools/verify_notebooks.py --execute
```

Script dùng Python đang gọi lệnh, kiểm tra backend trong code và ví dụ Python ở Markdown, output thực thi, ảnh, công thức, mã bài tập và phần lý thuyết giữ nguyên. Commit nguồn `2937ae5` là mốc đối chiếu; clone nông/ZIP có thể không chứa mốc này.

Hướng dẫn Plot đã được viết theo code thực tế của từng branch tại [HUONG_DAN_PLOT.md](HUONG_DAN_PLOT.md) và ngay trước các ô vẽ trong cả 8 notebook. [Danh mục hướng dẫn theo cell](qa/PLOT_INSTRUCTIONS.json) cho phép đối chiếu từng hình.

Cập nhật phần Plot: 127 ô vẽ có chỉ dẫn API theo đúng branch; 9 đoạn code trong hướng dẫn Plot đã chạy tuần tự từ kernel sạch, không lỗi hoặc stderr. Hình PNG mới đã được xem. W1 dùng tham số hiển thị tách rõ khỏi công thức mô phỏng; bản Matplotlib dùng `Figure`/`Axes` cho ví dụ phân tán. Các notebook còn lại giữ code tính toán và bổ sung hướng dẫn trước ô vẽ. Xem [kết quả chạy ví dụ Plot](qa/PLOT_GUIDE_VALIDATION.json).

```bash
python -X utf8 tools/verify_notebooks.py --execute-guide
```
