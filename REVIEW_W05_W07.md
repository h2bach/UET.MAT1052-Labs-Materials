# Bản review notebook Buổi 5–7 — Plotly/Matplotlib

ThS. Hoàng Hữu Bách — BM. Khoa học & Kỹ thuật tính toán - Khoa Công nghệ Thông tin, VNU-UET

Branch cục bộ: `matplotlib-plotly`. Đây là bản nội dung đầy đủ dùng Matplotlib/Plotly để review, song song với branch Plotnine.

## Mở bài học

| Buổi | Notebook | Nội dung |
|---|---|---|
| 5 | [W5_NenTangVaTinhToanXacSuat.ipynb](W5_NenTangVaTinhToanXacSuat.ipynb) | Biến cố, tiên đề, có điều kiện, độc lập, quy tắc cộng/nhân, toàn phần, Bayes, De Méré và bài tập tổng hợp |
| 6 | [W6_PhanPhoiVaBienNgauNhien.ipynb](W6_PhanPhoiVaBienNgauNhien.ipynb) | Quy tắc đếm, phân phối và tần suất, biến ngẫu nhiên, PMF/CDF, đều rời rạc, Bernoulli, nhị thức, siêu bội, Poisson, roulette |
| 7 | [W7_KyVongPhuongSaiVaXapXiChuan.ipynb](W7_KyVongPhuongSaiVaXapXiChuan.ipynb) | Kỳ vọng, phương sai, SD, hộp/iid, tổng/trung bình, liên tục, chuẩn, CLT và toàn bộ nội dung mở rộng của slide |

Mỗi notebook đồng thời là bài giảng và môi trường thực hành: tình huống, giải thích ký hiệu/giả định, ví dụ tính tay, code, kết quả, diễn giải và lời giải thu gọn. Matplotlib dựng hình tĩnh; Plotly dùng cho hoạt động thay tham số. Các ô mô phỏng nêu cơ chế sinh dữ liệu và seed 42.

Mở JupyterLab từ thư mục `Notebooks-Matplotlib-Plotly`, chọn notebook, rồi **Restart Kernel and Run All Cells**. Cần `numpy`, `pandas`, `matplotlib`, `scipy`, `plotly`; kiểm tra tự động cần thêm `nbformat`, `nbclient`, `nbconvert`. Ba notebook mới dùng renderer `plotly_mimetype` cho JupyterLab. Nếu dùng Colab, chọn `pio.renderers.default = "colab"` trong ô thiết lập; tải cả notebook và tài nguyên kèm theo khi cần. Notebook Buổi 6–7 có ảnh nguồn nhúng sẵn, Buổi 5 đọc ảnh tương đối trong `figures/`.

## Căn cứ nội dung

Đã đọc các hướng dẫn `Agent.md`, `skill.md`, `course_map.md`; toàn bộ đề cương 31 trang, slide tuần 1–7 (648 trang); Markdown và code của notebook hiện hành ở các module và bản phát hành; hướng dẫn TFT; toàn bộ dữ liệu CSV và nguồn trong README; toàn bộ nội dung học thuật của `STAT20_in_Vietnamese.html`.

HTML có 7 chương và 2 phụ lục, 599 heading, 206 ảnh, 52 bảng. Nội dung học thuật được đọc như tài liệu tham khảo. Các chỉ dẫn dành cho sinh viên trong tài liệu không được coi là yêu cầu mới của người dùng. Đọc toàn bộ nguồn phục vụ sự nối tiếp của khóa học; đối chiếu thống kê chi tiết tập trung vào Buổi 5–7.

Khung buổi học/LLO theo đề cương. Nội dung, ví dụ, bài tập và đáp án theo slide hiện tại. STAT20 bổ sung diễn giải và các mục đề cương còn thiếu. Số mục trong HTML khác đề cương:

| Buổi | Đề cương | Slide đã có | STAT20 tiếng Việt |
|---|---|---|---|
| 5 | 3.1–3.3, LLO5.1–5.2 | 93 trang, 18 mã bài tập | Mở đầu Chương 3 và §3.1–3.3 |
| 6 | 3.4–3.5, LLO6.1 | 80 trang, Ví dụ 1–21 | §3.4 và §4.1–4.6 |
| 7 | 3.6–3.7, LLO7.1 | 94 trang, Ví dụ 1–15, Bài tập 1–10 | §4.7–4.18 |

Không tự tạo mã W06/W07 hoặc nhãn mức độ khi slide chỉ ghi số ví dụ/bài tập. Buổi 5 giữ cả toàn phần và Bayes; Buổi 7 giữ Chebyshev, luật số lớn yếu, mũ, chi bình phương và t-Student vì các nội dung này đã có trong slide. Phần phân phối mũ/chi bình phương/t-Student chỉ giới thiệu đặc điểm của phân phối ở đúng phạm vi slide; suy luận thống kê theo lộ trình buổi sau.

Mỗi notebook có bảng đối chiếu nguồn và metadata `source_pages` ở các ô để truy lại trang slide. Các sơ đồ/ảnh minh họa STAT20 có chú thích và nguồn; đồ thị dữ liệu được dựng bằng code. Hình bổ sung phục vụ giải thích nội dung nguồn và được ghi rõ.

## Hiệu chỉnh có căn cứ

- Buổi 5: trong hộp hai vé đỏ/hai xanh, sau rút một vé xanh còn hai đỏ và một xanh. Sửa mô tả sai ở STAT20 §3.3.3. Phân biệt các vé đồng khả năng với các chuỗi màu; chuỗi màu khi rút hai lần không hoàn lại không đồng khả năng. Sally Clark được dùng để phân tích độc lập và đảo chiều điều kiện theo câu chuyện lịch sử của nguồn.
- Buổi 6: slide trang 57–58 ghi “Ví dụ 15” nhưng mô phỏng đúng hộp của Ví dụ 14; notebook ghi rõ đính chính này và giữ đủ hai ví dụ. Mô hình siêu bội ghi đầy đủ miền giá trị và phân biệt chính xác với xấp xỉ nhị thức. Các số trung gian được làm tròn sau khi tính tổng.
- Buổi 7: dùng hộp 10 vé khớp hình, PMF, kỳ vọng 1,9 và phương sai 2,09; đoạn code STAT20 §4.14 liệt kê 11 vé là không nhất quán. Ghi rõ điều kiện CLT, CDF của đều theo từng khoảng, mật độ khác xác suất, tổng/trung bình của hộp hữu hạn vẫn rời rạc. Kỳ vọng tuyến tính không đòi độc lập; công thức cộng phương sai cần kiểm tra phụ thuộc.

Khi kiểm tra trực quan đã sửa tiêu đề Plotly sau khi đổi tham số, cấu trúc khối đáp án thu gọn, nhãn CDF quá sát và legend che cột. Các chỉnh sửa này giữ nội dung thống kê và giúp đọc kết quả đúng.

## Kiểm chứng và phạm vi Git

Kết quả chốt ngày 07/10/2026 trên bản trong `Notebooks-Matplotlib-Plotly/`:

| Buổi | Tổng ô | Ô code đã chạy | Hình Matplotlib | Hình Plotly | Ảnh nguồn | Độ phủ slide |
|---|---:|---:|---:|---:|---:|---:|
| 5 | 91 | 19 | 6 | 2 | 20 | 93/93 trang |
| 6 | 119 | 34 | 17 | 1 | 4 | 80/80 trang |
| 7 | 79 | 32 | 14 | 2 | 5 | 94/94 trang |

Cả ba bản đã chạy từ kernel sạch, không output lỗi hoặc stderr; source–release đồng nhất và toàn bộ ảnh/attachment tồn tại. Đã kiểm tra hình, công thức và thao tác slider trong trình duyệt. Kiểm chứng chạy tại máy với phiên bản thư viện trong [QA JSON](./qa/W05_W07_VALIDATION.json); chưa chạy trực tiếp trên Colab. W5 sẵn sàng giảng dạy; W6–7 sẵn sàng review nội dung đầy đủ. Bài đầy đủ có nhiều hoạt động; giảng viên có thể chọn bài tập làm tại lớp và giao phần còn lại sau buổi học.

Chạy kiểm tra bản phát hành từ thư mục này:

```powershell
python -X utf8 tools/verify_w05_w07.py
```

Để thực thi lại cả ba notebook từ kernel sạch và lưu output:

```powershell
python -X utf8 tools/verify_w05_w07.py --execute
```

Script kiểm tra cấu trúc notebook, ID ô duy nhất, mọi ô code đã chạy, lỗi/cảnh báo trong output, ảnh/attachment, nội dung khối đáp án thực sự nằm trong `<details>`, đủ bài tập/ví dụ, source–release thống nhất và file Buổi 1–4 được giữ nguyên so với snapshot cục bộ.

Hai thư mục phát hành là hai Git worktree của repository học liệu: `Notebooks-Matplotlib-Plotly/` và `Notebooks-Plotnine/`. Các thay đổi cũ chưa commit được lưu tại commit `2b48b01`, là tổ tiên của cả hai branch hiện tại. So sánh bản mới với snapshot này:

```powershell
git diff --stat 2b48b01...matplotlib-plotly
```

Thư mục project gốc trước đó chưa có Git; đã tạo mốc `main` chứa nguồn hiện có và branch cùng tên để quản lý module 05–07 cùng cập nhật trạng thái trong `course_map.md`. Hai repository có lịch sử riêng. Bản phát hành được commit và push lên GitHub theo yêu cầu ngày 07/10/2026. Hai branch review được giữ riêng; chưa merge vào main. Snapshot cũ được giữ trong lịch sử commit, không dùng branch phụ. Việc chuyển backend chỉ áp dụng cho Buổi 5–7.

Nội dung Markdown, code và metadata của notebook Buổi 1–4, bản TFT, guide TFT, slide, HTML nguồn và CSV giữ nguyên. File W4 được lưu lại output/execution count trong lúc làm việc; bản lưu này được giữ và đưa vào Git theo yêu cầu push all. QA xác nhận chỉ hai trường execution count/output thay đổi, không thay đổi nội dung bài giảng. Vì thế nội dung Ngữ pháp đồ họa hiện có không bị thay đổi. Bản Plotnine dùng cùng dữ liệu, ánh xạ thuộc tính hình ảnh và dạng hình học đã ghi trong bài; giữ phần lý thuyết, giả định và diễn giải.

## Hai phiên bản và giới hạn chuyển đổi

| Thư mục | Branch GitHub | Backend Buổi 5–7 |
|---|---|---|
| `Notebooks-Matplotlib-Plotly` | [matplotlib-plotly](https://github.com/h2bach/UET.MAT1052-Labs-Materials/tree/matplotlib-plotly) | Matplotlib + Plotly |
| `Notebooks-Plotnine` | [plotnine](https://github.com/h2bach/UET.MAT1052-Labs-Materials/tree/plotnine) | Plotnine; ipywidgets ở Buổi 5–6 |

Chỉ chuyển code vẽ Buổi 5–7. Lý thuyết, công thức, đề bài, đáp án và metadata nguồn giữ nguyên; bảy ô Markdown chỉ thay lời hướng dẫn backend/thao tác. Xem [báo cáo đối chiếu hai backend](./qa/W05_W07_BACKEND_PARITY.json). Notebook Buổi 1–4/TFT có cùng nội dung ở hai folder và giữ backend hiện có. Hai branch đều chứa notebook cùng `datasets/`, `figures/`, README và QA để tải/chạy độc lập.

Các báo cáo QA độc lập ban đầu trong `qa/` đối chiếu nội dung gốc Matplotlib/Plotly. Kết quả cuối từng backend nằm ở `W05_W07_VALIDATION.json`. Plotnine không còn output hoặc import trực tiếp Plotly/Matplotlib trong ba notebook mới; Plotnine sử dụng Matplotlib ở bên trong thư viện.
