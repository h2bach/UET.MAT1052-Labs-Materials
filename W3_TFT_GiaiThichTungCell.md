# Hướng dẫn đọc từng cell — Tuần 3 với dữ liệu TFT

ThS. Hoàng Hữu Bách — BM. Khoa học & Kỹ thuật tính toán - Khoa Công nghệ Thông tin, VNU-UET

Tài liệu này đi kèm notebook [W3_TFT_NguPhapDoHoaVaDieuKienHoa.ipynb](./W3_TFT_NguPhapDoHoaVaDieuKienHoa.ipynb). Mục tiêu là giúp người mới không chỉ chạy được mã Python, mà còn hiểu:

- mỗi cell đang làm gì và vì sao cần làm như vậy;
- tên biến biểu diễn đại lượng nào trong một trận TFT;
- từng hàm và từng thao tác biến đổi dữ liệu có tác dụng gì;
- nên đọc bảng, biểu đồ và con số đầu ra ra sao;
- kết luận nào được phép rút ra, kết luận nào còn cần thận trọng.

Notebook có 77 cell, được đánh số từ **Cell 00** đến **Cell 76** trong tài liệu này. Số thứ tự dùng hệ đếm bắt đầu từ 0, giống cách Python đánh chỉ số. Mỗi mục cũng ghi ID của cell để có thể đối chiếu chính xác nếu vị trí cell trong notebook thay đổi.

> **Lưu ý về dữ liệu:** toàn bộ dữ liệu TFT trong notebook là dữ liệu mô phỏng, được tạo ra ngay trong notebook để học tập. Các mối liên hệ trong dữ liệu do cơ chế mô phỏng quy định; chúng không phải bằng chứng về cân bằng thật của một phiên bản TFT cụ thể.

## Một số quy ước xuất hiện nhiều lần

| Tên | Ý nghĩa |
|---|---|
| **DataFrame** | Bảng dữ liệu hai chiều của pandas, gồm hàng và cột. |
| **Series** | Một cột dữ liệu một chiều của pandas. |
| **np** | Tên viết tắt của thư viện NumPy, dùng cho tính toán số và sinh số ngẫu nhiên. |
| **pd** | Tên viết tắt của pandas, dùng để tạo, lọc, nhóm và tóm tắt bảng dữ liệu. |
| **p9** | Tên viết tắt của Plotnine, dùng ggplot + aes + các lớp geom để vẽ biểu đồ. |
| **rng** | Bộ sinh số ngẫu nhiên. Vì có hạt giống cố định nên kết quả mô phỏng có thể tái lập. |
| **g**, **g_...** | Đối tượng ggplot; thêm lớp bằng +, gọi show() để hiển thị. |
| **aes** | Ánh xạ tên cột dữ liệu vào x, y, color, fill, shape, size. |
| **d** | Bảng đi qua lambda trong một pipeline; đọc ý nghĩa theo từng cell. |
| **groupby** | Chia dữ liệu thành các nhóm theo một hoặc nhiều biến. |
| **agg** | Tính các đại lượng tóm tắt cho từng nhóm. |
| **assign** | Tạo thêm cột mới mà không sửa trực tiếp bảng ban đầu. |
| **query** | Lọc hàng bằng một biểu thức điều kiện dễ đọc. |
| **loc** | Chọn hàng/cột bằng nhãn hoặc điều kiện logic. |
| **iloc** | Chọn hàng/cột bằng vị trí số nguyên. |
| **lambda** | Một hàm ngắn, không cần đặt tên, thường dùng ngay trong một thao tác. |
| **observed=True** | Khi nhóm các biến phân loại, chỉ giữ những tổ hợp thực sự xuất hiện trong dữ liệu. |

---

## Phần 1 — Khởi tạo dữ liệu và ngữ pháp đồ họa

### Cell 00 — Giới thiệu notebook

- **Loại:** Markdown
- **ID:** tft-001-title

Cell này đặt bối cảnh cho toàn bộ bài học: dùng tình huống TFT để học ngữ pháp đồ họa và điều kiện hóa. Ba mục tiêu chính là nhận diện thành phần của biểu đồ, chọn hình học phù hợp và biết lọc/nhóm dữ liệu trước khi kết luận.

Phần mô tả đơn vị quan sát rất quan trọng: **mỗi hàng là kết quả của một người chơi trong một lobby**. Vì mỗi lobby có 8 người chơi, 120 lobby sẽ tạo ra 960 hàng. Nếu nhầm một hàng là một lobby, các mẫu số và diễn giải sau đó sẽ sai.

Cell cũng nói rõ dữ liệu là mô phỏng. Điều này cho phép notebook chạy ngoại tuyến và cho kết quả ổn định, nhưng không nên dùng các con số trong bài để khẳng định chiến thuật nào đang mạnh trong meta thật.

### Cell 01 — Nạp thư viện và đặt các quy ước chung

- **Loại:** Code
- **ID:** tft-002-imports

#### Mục đích

Chuẩn bị các công cụ cần dùng, đặt kiểu hiển thị biểu đồ và khai báo những danh sách phân loại dùng xuyên suốt notebook.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `np` | NumPy: mảng số, logarit và mô phỏng số ngẫu nhiên. |
| `pd` | pandas: tạo, chọn, lọc, nhóm và tóm tắt bảng. |
| `p9` | Plotnine: xây biểu đồ bằng dữ liệu + aes + các lớp geom. |
| `display` | Hiển thị bảng trong Jupyter. |
| `bang_histogram(values, bins, density)` | Hàm tạo bảng khoảng histogram; values là giá trị nguồn, bins là số khoảng hoặc các mốc, density chọn tần số hay mật độ. |
| `height, edges` | Chiều cao và biên khoảng do np.histogram trả về; bảng kết quả có xmin, xmax, height. |
| `phan_tram(values), value` | Hàm đổi từng tỷ lệ 0–1 thành nhãn phần trăm, như 0.5 thành 50%. |
| `rng` | Bộ sinh số ngẫu nhiên với hạt giống 202503; giữ nguyên chuỗi mô phỏng của bản gốc. |
| `BAC` | Bốn bậc theo thứ tự: Bạc, Vàng, Bạch Kim, Kim Cương. |
| `CHIEN_THUAT` | Ba chiến thuật: Reroll cấp 6, Tempo cấp 7, Fast 8. |
| `LOI` | Ba loại lõi: Kinh tế, Giao tranh, Linh hoạt. |
| `MAU_CHIEN_THUAT` | Từ điển gán màu cố định cho từng chiến thuật. |

#### Các hành động trong cell

1. Nạp NumPy, pandas, Plotnine và display. Không cần API pyplot trong notebook này.

2. Đặt figure_format="png" để notebook lưu sẵn hình tĩnh; theme_bw, figure_size, dpi, legend_position và element_text đặt nền/nhãn chung.

3. bang_histogram dùng np.histogram rồi pd.DataFrame; giữ nguyên các biên và số đếm khi đổi backend. phan_tram chỉ đổi nhãn hiển thị.

4. pd.set_option đặt cách hiển thị bảng. Tạo rng với đúng seed 202503 và khai báo danh sách/màu dùng chung.

#### Điều cần nhớ

Đặt hạt giống không làm dữ liệu hết ngẫu nhiên về mặt mô phỏng; nó chỉ làm cho một chuỗi ngẫu nhiên cụ thể có thể tái lập. Đây là yêu cầu quan trọng khi viết học liệu hoặc báo cáo phân tích.

### Cell 02 — Tạo dữ liệu TFT mô phỏng

- **Loại:** Code
- **ID:** tft-003-generate-data

#### Mục đích

Đây là cell xây dựng toàn bộ dữ liệu dùng trong bài. Có thể coi nó là một **quy trình sinh dữ liệu**: từ bậc xếp hạng và đặc điểm người chơi, notebook tạo lobby, hành vi trong trận, điểm hiệu suất ẩn, thứ hạng cuối trận và một chuỗi lịch sử của một người chơi.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `rows, so_lobby` | Danh sách tích lũy các bản ghi và quy mô 120 lobby. |
| `bac_skill, scout_base` | Kỹ năng nền và mức scout nền theo bậc; đây là lựa chọn của cơ chế mô phỏng. |
| `player_pools, player_skill` | Danh sách người chơi thuộc mỗi bậc và kỹ năng ổn định của mỗi người. |
| `player_no, bac_roster, ids, player_id` | Bộ đếm mã người; bậc đang tạo roster; 60 mã của bậc đó; mã một người chơi. |
| `lobby_no, bac, lobby_id` | Số lobby đang tạo, bậc của lobby và mã L001…L120. |
| `p_nhanh, nhip_lobby` | Xác suất lobby nhanh theo bậc và nhịp Chậm/Nhanh được lấy ngẫu nhiên. |
| `nguoi_choi_lobby, lobby_rows` | Tám người khác nhau được chọn và tám bản ghi tạm của lobby. |
| `p_chien_thuat, chien_thuat` | Xác suất ba chiến thuật theo nhịp và chiến thuật của người đang tạo. |
| `loi, ky_nang` | Loại lõi và kỹ năng ẩn gồm thành phần ổn định cộng dao động trong trận. |
| `cap_co_so, cap_4_1` | Cấp cơ sở của chiến thuật và cấp tại stage 4-1, được giới hạn trong 5–9. |
| `roll_base, so_lan_roll` | Mức roll nền theo chiến thuật và số lần roll có nhiễu, giới hạn 0–55. |
| `vang_base, vang_4_1` | Vàng nền và vàng ở stage 4-1, giới hạn 0–80. |
| `mau_bonus, mau_4_1` | Phần cộng/trừ máu do chiến thuật/nhịp và máu ở 4-1, giới hạn 1–100. |
| `so_tuong_3_sao, so_lan_scout` | Số tướng ba sao và số lần scout, sinh theo phân phối Poisson. |
| `gia_tri_doi_hinh` | Giá trị đội hình kết hợp cấp, số lần roll, tướng ba sao và nhiễu. |
| `hieu_qua` | Phần cộng/trừ hiệu suất theo tổ hợp nhịp lobby × chiến thuật. |
| `diem_hieu_suat, _diem_hieu_suat` | Điểm hiệu suất ẩn trong tính toán và khóa tạm lưu điểm trong bản ghi. |
| `thu_tu, placement, idx` | Chỉ số người chơi sau khi xếp điểm giảm dần, hạng 1–8 và chỉ số bản ghi cần gán hạng. |
| `top4, win` | True nếu placement ≤ 4 hoặc placement = 1. |
| `sat_thuong_nguoi_choi` | Sát thương lên người chơi được mô phỏng theo placement và nhiễu, giới hạn 15–150. |
| `tran_tft` | Bảng chính 960 hàng: mỗi hàng là một người chơi trong một lobby. |
| `tong_sat_thuong` | Biến sát thương có đuôi phải dài, sinh bằng exp của biến chuẩn và làm tròn về số nguyên. |
| `chi_so_thieu` | 38 chỉ số hàng được chọn để đặt so_lan_scout thành NaN, xấp xỉ 4% của 960 hàng. |
| `so_tran, xu_huong, placement_lich_su` | 30 trận; xu hướng từ 0.15 đến −0.55; chuỗi placement mô phỏng có nhiễu, giới hạn 1–8. |
| `lich_su, tran_thu` | Bảng lịch sử một người chơi giả định và số thứ tự trận 1–30. |
| `placement_tb_5_tran` | Trung bình placement trong tối đa 5 trận gần nhất. |
| `r` | Một bản ghi trong biểu thức lấy điểm hiệu suất để xếp hạng; các nhãn phân loại được gắn bằng pd.Categorical. |

#### Các hành động trong cell

1. Tạo roster 60 người/bậc; rng.normal tạo kỹ năng ổn định theo người. rng.choice lấy một bậc và nhịp cho từng lobby, rồi lấy 8 người không hoàn lại.

2. Trong mỗi lobby, lấy chiến thuật và lõi theo các xác suất đã nêu trong code. np.clip giới hạn các đại lượng tại đúng cận; rng.poisson, rng.normal tạo nhiễu và các biến đếm.

3. Tính gia_tri_doi_hinh, hieu_qua và diem_hieu_suat theo đúng công thức trong notebook. Lưu điểm ẩn tạm để xếp hạng, không dùng nó như dữ liệu quan sát.

4. np.argsort trên dấu âm của điểm xếp từ cao xuống thấp. enumerate(start=1) gán placement 1–8, tạo top4/win và sát thương lên người chơi; xóa khóa điểm ẩn trước khi append vào rows.

5. pd.DataFrame và pd.Categorical tạo bảng với thứ tự nhóm cố định. exp tạo tong_sat_thuong có đuôi phải dài. Chọn 38 hàng scout và đặt NaN.

6. np.linspace, np.arange, np.clip và np.rint tạo lịch sử 30 trận. rolling(5,min_periods=1).mean() tính trung bình trượt; ở đầu chuỗi chỉ dùng các trận đã có.

7. In số lobby và số quan sát; biểu thức cuối chọn các lượt của người P044. Không gọi mạng hoặc lấy dữ liệu Riot Games.

#### Đầu ra

Cell in số lobby, số hàng và các lượt của người chơi P044. Kết quả mong đợi là **120 lobby** và **960 hàng**, vì 120 × 8 = 960.

#### Lưu ý thống kê

Cell này cho thấy dữ liệu quan sát không tự xuất hiện: chúng được tạo bởi một cơ chế. Nếu nhiều biến cùng đi vào **diem_hieu_suat**, mối liên hệ giữa một biến và thứ hạng có thể bị trộn với ảnh hưởng của những biến khác. Đây là lý do các phần sau dùng lọc, nhóm và điều kiện hóa.

### Cell 03 — Từ điển dữ liệu và đơn vị quan sát

- **Loại:** Markdown
- **ID:** tft-004-dictionary

Cell định nghĩa ý nghĩa của các cột quan trọng. Đây là bước nên làm trước mọi phân tích: xác định một hàng là gì, mỗi cột đo gì và thang đo có hướng như thế nào.

Đặc biệt, **placement càng nhỏ càng tốt**. Đây là chiều ngược với nhiều đại lượng quen thuộc như điểm số. Khi đọc tương quan hoặc biểu đồ, phải luôn nhớ hạng 1 tốt hơn hạng 8.

Câu Q00 kiểm tra mẫu số: tỷ lệ top 4 theo chiến thuật được tính trên **tất cả lượt người chơi-trận thuộc chiến thuật đó**, không phải trên số người chơi duy nhất hay số lobby.

### Cell 04 — Kiểm tra tính hợp lệ của dữ liệu

- **Loại:** Code
- **ID:** tft-005-data-checks

#### Mục đích

Xác nhận dữ liệu mô phỏng tuân thủ các ràng buộc cơ bản trước khi dùng để phân tích.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `kiem_tra_placement` | min, max và số placement khác nhau trong mỗi lobby. |
| `tran_tft` | Bảng cần kiểm tra các ràng buộc cấu trúc trước khi phân tích. |

#### Các hành động trong cell

1. groupby("lobby_id")["placement"].agg(["min","max","nunique"]) kiểm tra mỗi lobby có đúng min=1, max=8 và tám hạng khác nhau.

2. assert kiểm tra các ràng buộc; lỗi sẽ dừng notebook. top4.mean()==0.5 vì mỗi lobby có đúng 4 top4/8 người.

3. duplicated(["lobby_id","player_id"]) kiểm tra trùng người trong một lobby. groupby("player_id").nunique() kiểm tra bậc ổn định theo người.

4. describe(include="all").T lấy mô tả số và phân loại; chỉ giữ count, unique, mean, min, max và fillna("") để ô không áp dụng hiển thị trống.

#### Cách đọc đầu ra

Bảng hiển thị count, unique, mean, min và max cho các cột; ô không áp dụng để trống. **count** của so_lan_scout nhỏ hơn 960 vì cell tạo dữ liệu đã cố ý cài một số giá trị thiếu.

### Cell 05 — Mở đầu phần ngữ pháp đồ họa

- **Loại:** Markdown
- **ID:** tft-006-part-1

Cell nêu tư tưởng cốt lõi: một biểu đồ không chỉ là một “loại hình” có sẵn mà là sự kết hợp của dữ liệu, ánh xạ thẩm mỹ, hình học, phép biến đổi thống kê, hệ tọa độ và chia ô. Cách nhìn này giúp người học thiết kế biểu đồ có chủ đích.

### Cell 06 — Bốn câu hỏi, bốn hình học

- **Loại:** Code
- **ID:** tft-007-four-plots

#### Mục đích

Đặt bốn biểu đồ cạnh nhau để cho thấy loại câu hỏi quyết định hình học cần dùng.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `dem` | Số lượt người-chơi–trận theo từng chiến thuật, giữ thứ tự CHIEN_THUAT. |
| `dem_hinh` | Bảng số đếm với hai cột chien_thuat và n để đưa vào ggplot. |
| `hist_placement` | Biên và tần số histogram, với các biên 0.5, 1.5, …, 8.5. |
| `nhom_vang, c` | Ba Series vàng, lấy từng chiến thuật c; giữ nguyên dữ liệu dùng cho hộp. |
| `g_cot, g_hist, g_diem, g_hop` | Bốn đối tượng Plotnine: cột, histogram, điểm và hộp. |

#### Các hành động trong cell

1. value_counts(sort=False), rename_axis và reset_index tạo bảng đếm cho geom_col.

2. bang_histogram dùng các biên np.arange(0.5,9.5,1); geom_rect vẽ đúng số đếm trong mỗi khoảng placement.

3. ggplot + aes + geom_point vẽ từng người-chơi–trận. scale_y_reverse giữ hạng 1 ở trên, 8 ở dưới.

4. geom_boxplot tóm tắt vang_4_1 theo chien_thuat. scale_fill_manual lấy đúng MAU_CHIEN_THUAT.

5. Ghép bốn biểu đồ bằng | (cạnh nhau) và / (trên/dưới). & theme áp dụng cỡ hình, góc nhãn và tắt chú giải lặp cho cả khung; show() hiển thị PNG.

#### Cách đọc đầu ra

- Biểu đồ cột trả lời “có bao nhiêu”.
- Histogram trả lời “phân phối có hình dạng thế nào”.
- Scatter trả lời “hai đại lượng có cùng thay đổi không”.
- Boxplot trả lời “các nhóm khác nhau về trung vị và độ phân tán ra sao”.

**Đọc code vẽ bằng Plotnine.** Đọc ánh xạ đầu tiên `x='chien_thuat', y='n', fill='chien_thuat'` trong `aes`; tên biến được lấy từ bảng dữ liệu của lớp tương ứng. `geom_col` vẽ cột có độ dài lấy trực tiếp từ giá trị `y` đã tính trong bảng. `geom_rect` vẽ mỗi hình chữ nhật từ các cận `xmin`, `xmax`, `ymin` và `ymax`. `geom_point` mỗi điểm lấy tọa độ từ hai biến được ánh xạ vào `x` và `y`. Thử đổi một thuộc tính hiển thị đang có trong lớp vẽ hoặc `theme`, rồi chạy lại ô; giữ dữ liệu để so sánh hình trước và sau.

### Cell 07 — Phân tích ngữ pháp của biểu đồ

- **Loại:** Markdown
- **ID:** tft-008-grammar

Q01 yêu cầu người học gọi đúng tên các thành phần: biến x, biến y, hình học, thẩm mỹ và chia ô. Đây là luyện tập “đọc cấu trúc” thay vì chỉ nhận xét hình đẹp hay xấu.

Các khái niệm mapping, geometry và facet được giới thiệu trước khi xuất hiện trong ví dụ tiếp theo.

### Cell 08 — Một biểu đồ có nhiều ánh xạ

- **Loại:** Code
- **ID:** tft-009-grammar-scatter

#### Mục đích

Minh họa cách một điểm dữ liệu có thể mang nhiều lớp thông tin: vị trí, màu và kích thước.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `mau` | Mẫu 260 hàng được lấy với random_state=20, độc lập với rng mô phỏng. |
| `mau_hinh` | Bảng mẫu thêm cột kích thước dành riêng cho lớp vẽ. |
| `kich_thuoc_diem` | Căn bậc hai của (10 + 1.4 × gia_tri_doi_hinh)/π; đổi diện tích điểm của bản gốc sang đơn vị size của Plotnine. |
| `g` | Biểu đồ ánh xạ máu vào x, placement vào y, chiến thuật vào màu và giá trị đội hình vào kích thước. |

#### Các hành động trong cell

1. sample(260,random_state=20) giữ đúng mẫu cố định của bản gốc.

2. assign tính kich_thuoc_diem từ công thức diện tích ban đầu; np.sqrt và π đổi sang đơn vị kích thước của Plotnine. stroke=0 tránh thêm viền làm thay đổi diện tích.

3. aes ánh xạ máu, placement, màu và size. scale_size_identity dùng trực tiếp kích thước đã tính; scale_color_manual thống nhất màu chiến thuật.

4. guides với override_aes chỉ làm điểm trong chú giải đủ rõ. scale_y_reverse và labs đặt hướng trục, đơn vị và nhãn; show() lưu hình trong output.

#### Cách đọc

Mỗi điểm là một lượt người chơi-trận. Hai điểm gần nhau có máu và thứ hạng gần nhau; màu cho biết chiến thuật; điểm lớn hơn biểu thị đội hình có giá trị cao hơn. Biểu đồ cho thấy nhiều biến cùng lúc, nhưng cũng có nguy cơ quá tải thị giác.

**Đọc code vẽ bằng Plotnine.** Đọc ánh xạ đầu tiên `x='mau_4_1', y='placement', color='chien_thuat'` trong `aes`; tên biến được lấy từ bảng dữ liệu của lớp tương ứng. `geom_point` mỗi điểm lấy tọa độ từ hai biến được ánh xạ vào `x` và `y`. Thử đổi một thuộc tính hiển thị đang có trong lớp vẽ hoặc `theme`, rồi chạy lại ô; giữ dữ liệu để so sánh hình trước và sau.

### Cell 09 — Tách cấu trúc biểu đồ thành lời

- **Loại:** Markdown
- **ID:** tft-010-grammar-explain

Cell giải mã chính xác biểu đồ trước: dữ liệu nào, biến nào lên trục nào, màu và kích thước biểu diễn gì. Sau đó nhấn mạnh: giữ nguyên biến nhưng đổi geometry sẽ thay đổi câu hỏi thống kê. Điểm phù hợp để nhìn từng quan sát; boxplot phù hợp để so sánh phân phối nhóm.

### Cell 10 — Cùng biến, khác hình học

- **Loại:** Code
- **ID:** tft-011-geom-compare

#### Mục đích

So sánh trực tiếp hai cách biểu diễn xếp hạng theo chiến thuật.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `bang_diem` | Danh sách bảng con, rồi bảng dài chứa x đã jitter, placement và chien_thuat. |
| `j, chien_thuat` | Chỉ số 0–2 và nhãn chiến thuật đang xử lý. |
| `y, x` | Mảng placement và vị trí ngang lấy từ rng.normal(j + 1, 0.055, size=len(y)). |
| `du_lieu_hop, c` | Ba Series placement theo chiến thuật c, giữ nguyên dữ liệu nguồn. |
| `g_diem, g_hop` | Hai đối tượng Plotnine: từng quan sát và tóm tắt bằng hộp. |

#### Các hành động trong cell

1. Lặp từng chiến thuật theo đúng thứ tự, giữ nguyên lời gọi rng.normal(j+1,0.055,size=len(y)). Jitter chỉ dịch vị trí ngang để nhìn được các điểm chồng nhau.

2. pd.concat ghép bảng điểm. geom_point vẽ x đã jitter; scale_x_continuous gắn nhãn ba chiến thuật vào vị trí 1,2,3.

3. geom_boxplot dùng dữ liệu placement gốc theo nhóm. Không áp dụng jitter lên giá trị placement.

4. Hai hình đều scale_y_reverse với đầy đủ hạng 1–8. | ghép cạnh nhau; theme tắt chú giải lặp vì màu đã tương ứng nhãn x.

#### Cách đọc

Biểu đồ điểm giữ lại từng quan sát và cho thấy cỡ mẫu. Boxplot gọn hơn nhưng che bớt cấu trúc rời rạc của hạng 1–8. Không có geometry nào luôn tốt hơn; lựa chọn phụ thuộc câu hỏi.

**Đọc code vẽ bằng Plotnine.** Đọc ánh xạ đầu tiên `x='chien_thuat', y='placement', fill='chien_thuat'` trong `aes`; tên biến được lấy từ bảng dữ liệu của lớp tương ứng. `geom_boxplot` tính hộp và râu từ các quan sát trong từng nhóm. `geom_point` mỗi điểm lấy tọa độ từ hai biến được ánh xạ vào `x` và `y`. Thử đổi một thuộc tính hiển thị đang có trong lớp vẽ hoặc `theme`, rồi chạy lại ô; giữ dữ liệu để so sánh hình trước và sau.

### Cell 11 — Hình học và facet

- **Loại:** Markdown
- **ID:** tft-012-geom-note

Cell tổng kết sự đánh đổi giữa điểm và boxplot, rồi giới thiệu facet: chia một biểu đồ thành nhiều ô theo một biến phân loại để so sánh cùng một mối liên hệ trong các nhóm.

### Cell 12 — Chia ô theo bậc xếp hạng

- **Loại:** Code
- **ID:** tft-013-facet-rank

#### Mục đích

Quan sát mối liên hệ máu–thứ hạng riêng trong từng bậc, thay vì gộp toàn bộ người chơi.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `KY_HIEU` | Từ điển ánh xạ chiến thuật sang hình điểm o, s, ^. |
| `g` | Một đối tượng ggplot chia thành bốn facet theo bac_xep_hang. |

#### Các hành động trong cell

1. aes(color="chien_thuat",shape="chien_thuat") mã hóa cùng chiến thuật bằng màu và hình điểm.

2. scale_color_manual và scale_shape_manual định nghĩa hai bảng mã; geom_point dùng alpha=0.34 để thấy chồng lấp.

3. facet_wrap("bac_xep_hang",nrow=1) chia bốn ô theo bậc, mặc định chung thang x/y. Không phải tạo bốn trục thủ công.

4. scale_y_reverse, labs và theme hoàn thiện hướng trục, nhãn và chú giải; show() xuất toàn bộ bốn facet.

#### Cách đọc

Đọc từng ô như cùng một câu hỏi trong một điều kiện bậc cụ thể. Nếu hình dạng quan hệ khác nhau giữa các ô, kết luận gộp toàn bộ bậc có thể che mất tính không đồng nhất.

**Đọc code vẽ bằng Plotnine.** Đọc ánh xạ đầu tiên `x='mau_4_1', y='placement', color='chien_thuat', shape='chien_thuat'` trong `aes`; tên biến được lấy từ bảng dữ liệu của lớp tương ứng. `geom_point` mỗi điểm lấy tọa độ từ hai biến được ánh xạ vào `x` và `y`. Facet chia cùng một biểu đồ theo biến nhóm; kiểm tra tham số `scales` trước khi so độ lớn giữa các ô. Thử đổi một thuộc tính hiển thị đang có trong lớp vẽ hoặc `theme`, rồi chạy lại ô; giữ dữ liệu để so sánh hình trước và sau.

### Cell 13 — Bài tập mapping và setting

- **Loại:** Markdown
- **ID:** tft-014-mapping-setting

Cell phân biệt:

- **mapping:** màu thay đổi theo một biến dữ liệu;
- **setting:** mọi điểm dùng cùng một màu do người vẽ chọn.

Đây không chỉ là khác biệt cú pháp. Mapping tạo ra một mã hóa thông tin và thường cần chú giải; setting chỉ là quyết định trình bày.

### Cell 14 — Màu cố định và màu ánh xạ

- **Loại:** Code
- **ID:** tft-015-mapping-plot

#### Mục đích

Đưa khái niệm ở Cell 13 vào hai biểu đồ cụ thể.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `mau_nho` | Mẫu 240 lượt người-chơi–trận với random_state=3. |
| `g_thiet_lap` | Biểu đồ có color cố định bên ngoài aes: mọi điểm màu tím. |
| `g_anh_xa` | Biểu đồ có color="chien_thuat" trong aes: màu mã hóa chiến thuật. |

#### Các hành động trong cell

1. sample(240,random_state=3) tạo cùng một tập quan sát cho hai hình.

2. Hình trái đặt color="#7E57C2" trong geom_point, bên ngoài aes: đây là thiết lập cố định.

3. Hình phải đặt color="chien_thuat" trong aes và chọn màu bằng scale_color_manual: đây là ánh xạ theo biến.

4. Cả hai đặt cùng trục placement đảo chiều rồi ghép bằng |; không thay dữ liệu hoặc biến trên x/y.

#### Cách đọc

Biểu đồ trái chỉ cho thấy quan hệ vàng–placement. Biểu đồ phải cho phép hỏi thêm liệu ba chiến thuật có chiếm các vùng khác nhau hay không. Đổi màu cố định không làm xuất hiện thông tin mới; ánh xạ màu theo biến thì có.

**Đọc code vẽ bằng Plotnine.** Đọc ánh xạ đầu tiên `x='vang_4_1', y='placement'` trong `aes`; tên biến được lấy từ bảng dữ liệu của lớp tương ứng. `geom_point` mỗi điểm lấy tọa độ từ hai biến được ánh xạ vào `x` và `y`. Thử đổi một thuộc tính hiển thị đang có trong lớp vẽ hoặc `theme`, rồi chạy lại ô; giữ dữ liệu để so sánh hình trước và sau.

### Cell 15 — Chọn geometry theo ngữ nghĩa

- **Loại:** Markdown
- **ID:** tft-016-geometry-semantics

Q02 đặt câu hỏi về việc dùng đường nối. Một đường ngầm khẳng định các điểm có thứ tự và có quan hệ kế tiếp. Vì vậy không nên nối các người chơi độc lập chỉ vì họ đang nằm trong cùng một bảng.

### Cell 16 — Khi nào đường nối gây hiểu sai

- **Loại:** Code
- **ID:** tft-017-line-semantics

#### Mục đích

Đặt cạnh nhau một đường nối sai ngữ nghĩa và một đường nối đúng ngữ nghĩa.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `ngang` | 24 hàng lấy với random_state=12, sắp theo player_id; chúng thuộc những người khác nhau. |
| `bang_ngang, thu_tu_hang` | Bảng thêm chỉ số 1–24 theo thứ tự hàng, chỉ phục vụ ví dụ nối sai ngữ nghĩa. |
| `g_sai` | Đường nối các hàng của những người khác nhau. |
| `g_dung` | Đường nối lịch sử 30 trận của cùng một người, dùng tran_thu. |

#### Các hành động trong cell

1. sample và sort_values tạo 24 quan sát của những người khác nhau. assign thêm thứ tự hàng 1–24; geom_line + geom_point nối chúng trong hình minh họa sai ngữ nghĩa.

2. Biểu đồ đúng dùng lich_su với tran_thu, thứ tự thực của 30 trận của một người.

3. scale_y_reverse đặt chiều hạng giống nhau. | và theme đưa hai cách dùng cùng geometry cạnh nhau để so sánh ý nghĩa.

#### Ý nghĩa

Một biểu đồ có thể chạy đúng cú pháp nhưng sai về ngữ nghĩa. Kiểm tra “điểm A có thực sự đứng trước điểm B không?” trước khi dùng line chart.

**Đọc code vẽ bằng Plotnine.** Đọc ánh xạ đầu tiên `x='thu_tu_hang', y='placement'` trong `aes`; tên biến được lấy từ bảng dữ liệu của lớp tương ứng. `geom_point` mỗi điểm lấy tọa độ từ hai biến được ánh xạ vào `x` và `y`. `geom_line` nối các điểm theo thứ tự của `x`; đọc `group` hoặc ánh xạ màu để biết các đường được tách thế nào. Thử đổi một thuộc tính hiển thị đang có trong lớp vẽ hoặc `theme`, rồi chạy lại ô; giữ dữ liệu để so sánh hình trước và sau.

### Cell 17 — Đáp án về đường nối

- **Loại:** Markdown
- **ID:** tft-018-line-answer

Cell xác nhận đường chỉ phù hợp khi có thứ tự có nghĩa, như thời gian của cùng một người chơi. Đây là kết luận phương pháp, không phụ thuộc riêng TFT.

### Cell 18 — Mở đầu phần lịch sử theo thời gian

- **Loại:** Markdown
- **ID:** tft-019-part-2

Cell chuyển từ ngữ pháp chung sang một tình huống dữ liệu theo thời gian. Mục tiêu là phân biệt điểm rời rạc, đường nối, đường làm mượt và chú thích.

### Cell 19 — Xem dữ liệu lịch sử trước khi vẽ

- **Loại:** Code
- **ID:** tft-020-history-head

#### Mục đích

Kiểm tra cấu trúc dữ liệu gốc trước khi trực quan hóa.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `lich_su` | Lịch sử 30 trận của một người chơi giả định. |
| `head(10)` | Chọn 10 hàng đầu để xem tran_thu, placement, chiến thuật, top4 và trung bình trượt. |

#### Các hành động trong cell

1. head(10) hiển thị 10 trận đầu, không lọc hay sửa bảng lich_su.

2. Đọc tran_thu theo thời gian và đối chiếu placement với placement_tb_5_tran trước khi xem đường.

#### Cách đọc

Mỗi trận có một kết quả của cùng một người chơi giả định. Trước khi nối đường, cần xác nhận cột tran_thu có thứ tự thời gian và các hàng thực sự thuộc cùng một đối tượng.

### Cell 20 — Điểm rời rạc và đường xu hướng

- **Loại:** Code
- **ID:** tft-021-history-plots

#### Mục đích

So sánh hai mức độ xử lý cùng một chuỗi lịch sử: chỉ hiển thị quan sát và thêm đường giúp nhìn xu hướng.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `lich_su_dai` | Bảng dài được melt từ placement và placement_tb_5_tran. |
| `duong, hang` | Tên chuỗi và giá trị placement/trung bình của chuỗi đó; mỗi trận có hai hàng trong bảng dài. |
| `g_diem` | Biểu đồ từng trận bằng điểm riêng. |
| `g_duong` | Biểu đồ chồng đường placement và trung bình trượt 5 trận. |

#### Các hành động trong cell

1. melt giữ tran_thu làm biến nhận diện, chuyển hai chuỗi thành cột duong/hang; dữ liệu dài thuận tiện để ánh xạ màu và nhóm đường.

2. Hình trái chỉ geom_point. Hình phải geom_line theo duong, thêm geom_point cho placement bằng lớp dữ liệu riêng với inherit_aes=False.

3. scale_color_manual đặt màu và tên hai chuỗi; scale_y_reverse giữ đủ hạng 1–8. | ghép hai hình và show() hiển thị.

#### Cách đọc

Đường trung bình 5 trận giúp thấy xu hướng nhưng không thay thế dữ liệu gốc. Một chuỗi ngắn có thể thay đổi hình dạng đáng kể khi đổi cửa sổ, nên cần trình bày cả điểm/đường thật.

**Đọc code vẽ bằng Plotnine.** Đọc ánh xạ đầu tiên `x='tran_thu', y='placement'` trong `aes`; tên biến được lấy từ bảng dữ liệu của lớp tương ứng. `geom_point` mỗi điểm lấy tọa độ từ hai biến được ánh xạ vào `x` và `y`. `geom_line` nối các điểm theo thứ tự của `x`; đọc `group` hoặc ánh xạ màu để biết các đường được tách thế nào. Thử đổi một thuộc tính hiển thị đang có trong lớp vẽ hoặc `theme`, rồi chạy lại ô; giữ dữ liệu để so sánh hình trước và sau.

### Cell 21 — Câu hỏi về làm mượt

- **Loại:** Markdown
- **ID:** tft-022-history-question

Q03 yêu cầu so sánh ưu, nhược điểm của điểm rời rạc và đường nối. Cell cũng chuẩn bị cho khái niệm cửa sổ trung bình trượt: cửa sổ lớn hơn tạo đường mượt hơn nhưng phản ứng chậm hơn với thay đổi mới.

### Cell 22 — Chú thích trận tốt nhất

- **Loại:** Code
- **ID:** tft-023-annotated-history

#### Mục đích

Minh họa cách thêm chú thích dựa trên dữ liệu thay vì ghi cứng một vị trí.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `placement_tot` | Placement nhỏ nhất trong lịch sử, tức hạng tốt nhất. |
| `tran_tot` | Trận đầu tiên đạt placement_tot; iloc[0] chọn lần xuất hiện đầu. |
| `lich_su_chu_thich` | Bảng dài chứa cả placement và trung bình trượt. |
| `duong, hang` | Tên chuỗi và giá trị trên trục placement. |
| `g` | Biểu đồ đường, điểm, đoạn mũi tên và lời chú thích. |

#### Các hành động trong cell

1. min lấy placement tốt nhất; lọc theo giá trị đó, chọn tran_thu rồi iloc[0] lấy trận đầu đạt hạng tốt nhất.

2. melt đưa lịch sử vào dạng dài; geom_line và geom_point thể hiện chuỗi gốc và trung bình trượt.

3. annotate("segment",arrow=p9.arrow(...)) vẽ mũi tên tới trận được chọn; annotate("text") ghi lời cảnh báo. Vị trí chữ chỉ phục vụ trình bày.

4. scale_y_reverse, scale_color_manual và labs tạo trục, chú giải và tiêu đề có thể đọc độc lập.

#### Cách đọc

Nếu có nhiều trận đồng hạng tốt nhất, **idxmin** chọn lần xuất hiện đầu tiên. Chú thích phải hỗ trợ thông điệp cụ thể, không nên dùng quá nhiều làm che dữ liệu.

**Đọc code vẽ bằng Plotnine.** Đọc ánh xạ đầu tiên `x='tran_thu', y='hang', color='duong'` trong `aes`; tên biến được lấy từ bảng dữ liệu của lớp tương ứng. `geom_point` mỗi điểm lấy tọa độ từ hai biến được ánh xạ vào `x` và `y`. `geom_line` nối các điểm theo thứ tự của `x`; đọc `group` hoặc ánh xạ màu để biết các đường được tách thế nào. Thử đổi một thuộc tính hiển thị đang có trong lớp vẽ hoặc `theme`, rồi chạy lại ô; giữ dữ liệu để so sánh hình trước và sau.

### Cell 23 — Nguyên tắc truyền đạt bằng chú thích

- **Loại:** Markdown
- **ID:** tft-024-communication-note

Cell nhắc rằng chú thích là một quyết định truyền thông. Chỉ nên đánh dấu điểm phục vụ câu hỏi; việc chọn một điểm nổi bật sau khi đã xem toàn bộ dữ liệu có thể tạo ấn tượng quá mức nếu không nói rõ tiêu chí.

### Cell 24 — Bài thực hành thay đổi tham số

- **Loại:** Markdown
- **ID:** tft-025-modify-heading

Cell mở một hoạt động “sửa và quan sát”. Người học không viết lại toàn bộ biểu đồ mà thay đúng một tham số để thấy quan hệ giữa mã và kết quả.

### Cell 25 — Điều chỉnh cửa sổ trung bình trượt

- **Loại:** Code
- **ID:** tft-026-modify-code

#### Mục đích

Cho người học chủ động đổi độ mượt của đường xu hướng.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `CUA_SO` | Số trận trong cửa sổ trung bình trượt; mặc định 5, thử 3 và 10. |
| `duong_muot` | Series rolling(CUA_SO, min_periods=1).mean() trên placement. |
| `bang_muot` | Bảng chứa placement và trung bình, sau đó melt thành dạng dài. |
| `duong, hang` | Nhận diện hai đường và giá trị cần vẽ. |
| `g` | Biểu đồ Plotnine có tiêu đề/chú giải dùng giá trị CUA_SO hiện tại. |

#### Các hành động trong cell

1. Sửa CUA_SO thành 3, 5 hoặc 10 rồi chạy lại Cell 25. Không cần tạo lại dữ liệu.

2. rolling(CUA_SO,min_periods=1).mean() dùng tối đa CUA_SO trận gần nhất; đầu chuỗi dùng ít trận hơn.

3. Tạo bang_muot, melt hai chuỗi và vẽ geom_line. Lớp điểm của lich_su vẫn giữ từng placement.

4. Chuỗi f trong labels/title đưa giá trị CUA_SO hiện tại vào nhãn. show() tạo PNG mới sau mỗi lần chạy lại.

#### Cách đọc và thử nghiệm

- **CUA_SO = 3:** đường bám dữ liệu sát hơn, nhạy hơn với dao động mới.
- **CUA_SO = 10:** đường mượt hơn nhưng che nhiều biến động ngắn hạn.

Không có một cửa sổ đúng tuyệt đối; lựa chọn phải gắn với câu hỏi và độ dài chuỗi.

**Đọc code vẽ bằng Plotnine.** Đọc ánh xạ đầu tiên `x='tran_thu', y='hang', color='duong'` trong `aes`; tên biến được lấy từ bảng dữ liệu của lớp tương ứng. `geom_point` mỗi điểm lấy tọa độ từ hai biến được ánh xạ vào `x` và `y`. `geom_line` nối các điểm theo thứ tự của `x`; đọc `group` hoặc ánh xạ màu để biết các đường được tách thế nào. Thử đổi một thuộc tính hiển thị đang có trong lớp vẽ hoặc `theme`, rồi chạy lại ô; giữ dữ liệu để so sánh hình trước và sau.

### Cell 26 — Câu hỏi sau thử nghiệm

- **Loại:** Markdown
- **ID:** tft-027-modify-question

Cell yêu cầu ghi lại quan sát thay vì chỉ chạy mã. Người học cần phân biệt “mượt” với “tốt”: làm mượt nhiều hơn không tự động tạo kết luận đáng tin hơn.

---

## Phần 2 — Cú pháp pandas và dữ liệu thiếu

### Cell 27 — Ngữ pháp phân tích trong Python

- **Loại:** Markdown
- **ID:** tft-028-part-3

Cell chuyển từ cấu trúc biểu đồ sang cấu trúc lệnh phân tích: chọn dữ liệu, lọc hàng, chọn cột, biến đổi, nhóm và tóm tắt. Trình tự này sẽ xuất hiện lặp lại trong các pipeline phía sau.

### Cell 28 — Lọc một bậc rồi vẽ

- **Loại:** Code
- **ID:** tft-029-python-grammar

#### Mục đích

Minh họa một quy trình ngắn: tạo bảng con, sau đó trực quan hóa theo nhóm.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `du_lieu_hinh` | Bản sao chỉ gồm các lượt ở bậc Vàng. |
| `g` | Biểu đồ tạo từ đúng bảng con, aes và lớp điểm. |

#### Các hành động trong cell

1. query("bac_xep_hang == 'Vàng'").copy() quyết định quần thể con trước khi vẽ.

2. ggplot nhận đúng du_lieu_hinh. aes("mau_4_1","placement",color="chien_thuat") là ánh xạ; geom_point là hình học.

3. scale_color_manual chọn bảng màu; scale_y_reverse đưa hạng 1 lên trên. labs đặt giao tiếp với người đọc; show() hiển thị.

#### Cách đọc

Mọi điểm đều thuộc bậc Gold. Vì đã điều kiện hóa theo bậc, sự khác biệt nhìn thấy giữa màu không còn do so sánh Gold với Silver/Platinum/Diamond, nhưng vẫn có thể chịu ảnh hưởng của nhiều biến khác.

**Đọc code vẽ bằng Plotnine.** Đọc ánh xạ đầu tiên `x='mau_4_1', y='placement', color='chien_thuat'` trong `aes`; tên biến được lấy từ bảng dữ liệu của lớp tương ứng. `geom_point` mỗi điểm lấy tọa độ từ hai biến được ánh xạ vào `x` và `y`. Thử đổi một thuộc tính hiển thị đang có trong lớp vẽ hoặc `theme`, rồi chạy lại ô; giữ dữ liệu để so sánh hình trước và sau.

### Cell 29 — Câu hỏi về thứ tự thao tác

- **Loại:** Markdown
- **ID:** tft-030-python-question

Cell yêu cầu người học nhận ra việc lọc diễn ra **trước** khi vẽ. Nếu vẽ toàn bộ rồi chỉ đổi tiêu đề thành Gold, hình không tự động trở thành dữ liệu Gold. Tên biến và nhãn không thay thế thao tác dữ liệu.

### Cell 30 — Đổi một thành phần: từ scatter sang boxplot

- **Loại:** Code
- **ID:** tft-031-change-one-component

#### Mục đích

Giữ dữ liệu Gold nhưng đổi câu hỏi: từ liên hệ hai biến số sang so sánh phân phối hạng theo lõi bổ trợ.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `du_lieu_loi, loai` | Ba Series placement theo từng loại lõi trong LOI. |
| `g` | Biểu đồ hộp dùng loai_loi làm x, placement làm y và fill theo lõi. |

#### Các hành động trong cell

1. Danh sách du_lieu_loi lấy placement của từng loại lõi trong cùng bậc Vàng; không đổi quần thể con.

2. aes đặt nhóm lõi trên x, placement trên y và màu tô theo lõi. geom_boxplot tóm tắt trung vị/tứ phân vị.

3. scale_fill_manual giữ màu của từng lõi; scale_y_reverse đảo chiều hạng. Không dùng vòng lặp tô patch.

#### Cách đọc

Mỗi hộp tóm tắt phân phối hạng của một nhóm lõi trong bậc Gold. Boxplot không cho biết nguyên nhân lõi tạo ra thứ hạng; đây chỉ là so sánh mô tả.

**Đọc code vẽ bằng Plotnine.** Đọc ánh xạ đầu tiên `x='loai_loi', y='placement', fill='loai_loi'` trong `aes`; tên biến được lấy từ bảng dữ liệu của lớp tương ứng. `geom_boxplot` tính hộp và râu từ các quan sát trong từng nhóm. Thử đổi một thuộc tính hiển thị đang có trong lớp vẽ hoặc `theme`, rồi chạy lại ô; giữ dữ liệu để so sánh hình trước và sau.

### Cell 31 — Bài học về thay đổi thành phần

- **Loại:** Markdown
- **ID:** tft-032-python-note

Cell khuyến khích thay từng yếu tố một. Đây là cách học mã hiệu quả vì người học có thể gắn sự thay đổi trong output với một thay đổi cụ thể trong code.

### Cell 32 — Mở đầu dữ liệu thiếu

- **Loại:** Markdown
- **ID:** tft-033-missing-heading

Cell đặt vấn đề rằng một biểu đồ có thể âm thầm dùng ít hàng hơn bảng gốc khi một biến bị thiếu. Vì vậy, trước khi vẽ phải biết còn bao nhiêu quan sát hoàn chỉnh và các hàng bị loại có đặc điểm gì.

### Cell 33 — Loại hàng thiếu cho một phân tích cụ thể

- **Loại:** Code
- **ID:** tft-034-missing-code

#### Mục đích

Tạo dữ liệu hoàn chỉnh cho hai biến scouting và thứ hạng, đồng thời công khai số hàng bị loại.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `du_scout` | Bảng bỏ các hàng thiếu so_lan_scout; tran_tft vẫn giữ nguyên. |
| `g` | Biểu đồ scout–placement chỉ trên hàng đủ telemetry. |

#### Các hành động trong cell

1. dropna(subset=["so_lan_scout"]) chỉ loại hàng thiếu biến dùng trong phân tích này, không loại mọi hàng có thiếu ở cột khác.

2. len, isna và sum báo tổng hàng, hàng đủ scout và hàng thiếu.

3. ggplot dùng du_scout, aes ánh xạ scout/placement, geom_point dùng alpha=0.22 để thấy điểm chồng; scale_y_reverse giữ hạng 1–8.

#### Đầu ra

Dữ liệu có 960 hàng, 922 hàng đầy đủ cho hai biến này và 38 hàng bị thiếu scouting. Con số có thể kiểm tra trực tiếp thay vì để thư viện âm thầm bỏ qua.

#### Lưu ý thống kê

Loại hàng chỉ an toàn khi cơ chế thiếu không làm mẫu còn lại bị lệch nghiêm trọng. Trong dữ liệu thật, cần kiểm tra thiếu có tập trung ở bậc, chiến thuật hoặc loại trận nào không.

**Đọc code vẽ bằng Plotnine.** Đọc ánh xạ đầu tiên `x='so_lan_scout', y='placement'` trong `aes`; tên biến được lấy từ bảng dữ liệu của lớp tương ứng. `geom_point` mỗi điểm lấy tọa độ từ hai biến được ánh xạ vào `x` và `y`. Thử đổi một thuộc tính hiển thị đang có trong lớp vẽ hoặc `theme`, rồi chạy lại ô; giữ dữ liệu để so sánh hình trước và sau.

### Cell 34 — Trả lời về dữ liệu thiếu

- **Loại:** Markdown
- **ID:** tft-035-missing-answer

Cell giải thích vì sao cỡ mẫu của biểu đồ nhỏ hơn dữ liệu gốc và cảnh báo rằng missingness có thể mang thông tin. Không nên tự động điền 0 cho số lần scout thiếu, vì “không quan sát được” khác với “quan sát được bằng 0”.

---

## Phần 3 — Điều kiện hóa và lọc dữ liệu

### Cell 35 — Mở đầu điều kiện hóa

- **Loại:** Markdown
- **ID:** tft-036-part-4

Cell giới thiệu điều kiện hóa dưới dạng câu hỏi “trong số những quan sát thỏa điều kiện X, phân phối Y thế nào?”. Đây là cầu nối từ lọc dữ liệu sang tư duy xác suất có điều kiện.

### Cell 36 — Chọn cột khác với lọc hàng

- **Loại:** Markdown
- **ID:** tft-037-select-vs-filter

Cell phân biệt hai thao tác thường bị nhầm:

- chọn cột trả lời “giữ lại biến nào?”;
- lọc hàng trả lời “giữ lại quan sát nào?”.

Một bảng có thể đồng thời được lọc hàng rồi chọn một số cột để hiển thị.

### Cell 37 — Lọc một điều kiện

- **Loại:** Code
- **ID:** tft-038-filter-one

#### Mục đích

Tạo tập con chỉ gồm bậc Diamond và xem một số cột quan trọng.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `kim_cuong` | Bảng con thỏa bac_xep_hang == "Kim Cương". |
| `len(kim_cuong)` | Số lượt người-chơi–trận ở bậc này, không phải số người duy nhất. |
| `head()` | Xem 5 hàng đầu của các cột được chọn. |

#### Các hành động trong cell

1. query giữ các hàng bậc Kim Cương; len in cỡ mẫu sau điều kiện hóa.

2. Chọn sáu cột bằng danh sách trong [] rồi head() xem 5 hàng đầu. Không groupby nên một hàng vẫn là một người-chơi–trận.

#### Lưu ý

**diamond** là một DataFrame mới dùng cho phân tích có điều kiện. Việc chỉ hiển thị 5 cột không xóa các cột khác khỏi biến diamond; danh sách cột chỉ nằm trong biểu thức truyền cho display.

### Cell 38 — Đọc điều kiện bằng lời

- **Loại:** Markdown
- **ID:** tft-039-filter-read

Cell luyện cách chuyển mã thành câu: “giữ các lượt người chơi-trận có bậc Diamond”. Việc diễn đạt bằng lời giúp phát hiện điều kiện sai trước khi phân tích.

### Cell 39 — Kết hợp nhiều điều kiện

- **Loại:** Code
- **ID:** tft-040-filter-multiple

#### Mục đích

Phân biệt giao của hai điều kiện với hợp của hai điều kiện.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `fast8_khoe` | Các hàng vừa Fast 8 vừa mau_4_1 ≥ 50. |
| `reroll_hoac_fast8` | Các hàng có chiến thuật thuộc tập Reroll cấp 6 hoặc Fast 8. |
| `isin` | Kiểm tra mỗi nhãn có nằm trong danh sách cho trước hay không. |

#### Các hành động trong cell

1. query kết hợp and: một hàng phải vừa Fast 8 vừa đủ 50 máu.

2. isin trả về Boolean cho các chiến thuật trong danh sách; [] giữ các hàng True, thể hiện Reroll hoặc Fast 8.

3. len báo số hàng của hai tập; fast8_khoe.head() hiển thị tập giao.

#### Cách đọc đầu ra

Đối chiếu bảng/giá trị hiển thị với các biến và thao tác vừa nêu; đơn vị quan sát vẫn là một người-chơi–trận cho tới bước nhóm.

### Cell 40 — Logic lọc và lựa chọn ngưỡng

- **Loại:** Markdown
- **ID:** tft-041-filter-logic

Cell tổng kết cú pháp query, phép **isin** và toán tử so sánh. Cảnh báo quan trọng là không nên thử rất nhiều ngưỡng rồi chỉ báo cáo ngưỡng cho kết quả đẹp nhất; hành vi đó làm tăng nguy cơ “khám phá” một mẫu ngẫu nhiên. Q04 yêu cầu người học dịch một câu điều kiện tự nhiên thành mã.

### Cell 41 — Tạo biến Boolean

- **Loại:** Code
- **ID:** tft-042-boolean-vars

#### Mục đích

Biến một điều kiện thành cột True/False để có thể hiển thị, nhóm hoặc tính tỷ lệ.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `vi_du_logic` | Bảng thêm hai cột Boolean, không sửa tran_tft. |
| `con_50_mau_o_4_1` | True nếu mau_4_1 ≥ 50. |
| `ket_qua_top4` | True nếu placement ≤ 4. |

#### Các hành động trong cell

1. assign tạo hai cột bằng các phép so sánh >= và <=, giữ nguyên bảng nguồn.

2. Chọn bốn cột liên quan và head(8) để đối chiếu giá trị với True/False.

#### Cách đọc đầu ra

Đối chiếu bảng/giá trị hiển thị với các biến và thao tác vừa nêu; đơn vị quan sát vẫn là một người-chơi–trận cho tới bước nhóm.

### Cell 42 — Trung bình của Boolean là tỷ lệ

- **Loại:** Code
- **ID:** tft-043-boolean-mean

#### Mục đích

Cho thấy cách tính tỷ lệ trực tiếp từ một cột True/False.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `vi_du_logic` | Bảng Boolean được tạo ở Cell 41. |
| `mean()` | Trung bình True/False như 1/0; trả về tỷ lệ trên tất cả 960 hàng. |

#### Các hành động trong cell

1. mean trên từng cột Boolean tính tổng True chia tổng hàng.

2. print báo tỷ lệ còn ít nhất 50 máu và tỷ lệ top4; các giá trị dùng thang 0–1.

#### Cách đọc đầu ra

Đối chiếu bảng/giá trị hiển thị với các biến và thao tác vừa nêu; đơn vị quan sát vẫn là một người-chơi–trận cho tới bước nhóm.

### Cell 43 — Vì sao phép tính Boolean hoạt động

- **Loại:** Markdown
- **ID:** tft-044-boolean-note

Cell giải thích mã hóa True = 1, False = 0. Tổng Boolean là số trường hợp đúng; trung bình Boolean là số trường hợp đúng chia tổng số quan sát không thiếu.

### Cell 44 — Mở đầu biến đổi logarit

- **Loại:** Markdown
- **ID:** tft-045-log-heading

Cell chuẩn bị cho tình huống biến số lệch phải. Logarit thường giúp nén các giá trị rất lớn và làm rõ cấu trúc ở phần thân phân phối, nhưng làm thay đổi đơn vị diễn giải.

### Cell 45 — So sánh thang gốc và log10

- **Loại:** Code
- **ID:** tft-046-log-plot

#### Mục đích

Quan sát cùng một biến sát thương trên hai thang đo.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `hist_goc` | Biên và tần số 28 khoảng của tong_sat_thuong. |
| `hist_log` | Biên và tần số 28 khoảng của np.log10(tong_sat_thuong). |
| `g_goc, g_log` | Hai biểu đồ hình chữ nhật tương ứng với hai thang đo. |

#### Các hành động trong cell

1. bang_histogram giữ đúng 28 khoảng của từng thang, số đếm tính bằng np.histogram.

2. np.log10 đổi tong_sat_thuong sang log cơ số 10; không thay giá trị gốc trong tran_tft.

3. geom_rect vẽ hai histogram theo xmin/xmax/height. | ghép hai thang, labs ghi đúng đơn vị trục; show() lưu hình.

#### Lưu ý

Logarit chỉ xác định trực tiếp cho giá trị dương. Cell tạo dữ liệu đã bảo đảm sát thương dương bằng cách cắt cận dưới. Với dữ liệu có 0, cần một quyết định rõ ràng như dùng log1p hoặc xử lý 0 theo ý nghĩa thực tế.

**Đọc code vẽ bằng Plotnine.** `geom_rect` vẽ mỗi hình chữ nhật từ các cận `xmin`, `xmax`, `ymin` và `ymax`. Thử đổi một thuộc tính hiển thị đang có trong lớp vẽ hoặc `theme`, rồi chạy lại ô; giữ dữ liệu để so sánh hình trước và sau.

### Cell 46 — Ý nghĩa của phép đổi thang

- **Loại:** Markdown
- **ID:** tft-047-log-note

Cell nhấn mạnh biến đổi log không xóa ngoại lệ hay “sửa” dữ liệu. Nó thay đổi cách khoảng cách được biểu diễn: chênh lệch theo tỷ lệ trở nên dễ nhìn hơn chênh lệch tuyệt đối.

---

## Phần 4 — Pipeline lọc, tạo biến, nhóm và tóm tắt

### Cell 47 — Giới thiệu pipeline

- **Loại:** Markdown
- **ID:** tft-048-part-5

Cell trình bày chuỗi hành động phân tích: lọc → tạo biến → nhóm → tóm tắt → sắp xếp. Mỗi bước làm thay đổi đối tượng hoặc mẫu số của bước sau, nên thứ tự là một phần của câu hỏi thống kê.

### Cell 48 — Pipeline hoàn chỉnh cho lobby nhanh

- **Loại:** Code
- **ID:** tft-049-pipeline

#### Mục đích

So sánh ba chiến thuật trong riêng các lobby có nhịp nhanh và tạo một bảng tóm tắt có thể đọc trực tiếp.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `tom_tat_nhanh` | Bảng tóm tắt chiến thuật trong riêng lobby Nhanh, index là chien_thuat. |
| `con_nhieu_mau, d` | Cột Boolean mau_4_1 ≥ 50; d trong lambda là bảng đã lọc đi qua assign. |
| `so_tran` | Số lượt người-chơi–trận trong từng chiến thuật của lobby nhanh. |
| `placement_tb` | Placement trung bình; nhỏ hơn là tốt hơn. |
| `ti_le_top4` | Trung bình top4 trong từng nhóm, đúng mẫu số của nhóm. |
| `ti_le_con_nhieu_mau` | Trung bình cột con_nhieu_mau trong từng nhóm. |

#### Các hành động trong cell

1. query lọc lobby Nhanh. assign với lambda d tạo con_nhieu_mau trên chính bảng đã lọc.

2. groupby("chien_thuat",observed=True) chỉ giữ nhóm thực có dữ liệu.

3. agg named aggregation tính size và mean, mỗi cặp chỉ rõ cột nguồn/hàm. Mẫu số ti_le_top4 là so_tran của nhóm trong lobby Nhanh.

4. sort_values("ti_le_top4",ascending=False) xếp từ cao xuống thấp. Cell giữ chien_thuat ở index; không reset_index hay round riêng ở đây.

#### Cách đọc đầu ra

Trong dữ liệu mô phỏng, Fast 8 có tỷ lệ top 4 cao nhất trong lobby nhanh, tiếp theo là Tempo rồi Reroll. Tuy nhiên, đây là so sánh mô tả trong một điều kiện; chưa phải bằng chứng rằng chọn Fast 8 gây ra top 4.

### Cell 49 — Câu hỏi về đơn vị và mẫu số

- **Loại:** Markdown
- **ID:** tft-050-pipeline-question

Cell yêu cầu xác định một hàng trong bảng kết quả đại diện cho gì: một **nhóm chiến thuật trong các lobby nhanh**, không còn là một người chơi-trận. Mẫu số của ti_le_top4 là so_tran của từng dòng.

### Cell 50 — Lọc và nhóm trả lời hai câu hỏi khác nhau

- **Loại:** Code
- **ID:** tft-051-filter-vs-group

#### Mục đích

Đối chiếu “chỉ xem Fast 8” với “giữ tất cả và so sánh theo chiến thuật”.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `tran_tft` | Bảng nguồn của cả hai cách phân tích. |
| `placement_tb, ti_le_top4` | Hai thống kê được đặt tên bằng named aggregation. |
| `display` | Hiển thị kết quả lọc Fast 8 và kết quả nhóm tất cả chiến thuật; cell không gán hai bảng này vào tên biến riêng. |

#### Các hành động trong cell

1. Pipeline đầu query Fast 8 rồi agg hai thống kê, chỉ trả lời về Fast 8.

2. Pipeline sau groupby chiến thuật rồi agg cùng hai thống kê, tạo một hàng mỗi chiến thuật.

3. display hiển thị hai kết quả trực tiếp. Bảng lọc agg có ô không áp dụng; không coi ô trống là một giá trị thống kê.

#### Cách đọc

Lọc trả lời: “Trong Fast 8, kết quả thế nào?”. Nhóm trả lời: “Các chiến thuật khác nhau thế nào?”. Hai thao tác không thể thay thế nhau dù đều có thể tạo ra một con số cho Fast 8.

### Cell 51 — Thứ tự thao tác quyết định mẫu phân tích

- **Loại:** Markdown
- **ID:** tft-052-order-note

Cell nhấn mạnh rằng lọc trước khi nhóm và nhóm trước khi lọc không nhất thiết tương đương. Đặc biệt, nếu lọc theo chính biến kết quả, tỷ lệ sau đó có thể trở nên vô nghĩa.

### Cell 52 — Ví dụ thứ tự sai làm tỷ lệ thành 100%

- **Loại:** Code
- **ID:** tft-053-order-matters

#### Mục đích

Minh họa một lỗi logic rất phổ biến: lọc chỉ các ca thành công rồi mới tính tỷ lệ thành công.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `so_sanh_thu_tu` | Bảng ghép hai Series tỷ lệ của cùng ba chiến thuật. |
| `Nhóm trước, tính tỉ lệ trên mọi trận` | Cột đúng câu hỏi tỷ lệ top4: mẫu số chứa cả thành công và không thành công. |
| `Lọc top 4 trước, rồi lấy mean` | Cột minh họa thay đổi mẫu số: tất cả hàng còn lại đều True nên mean bằng 1. |

#### Các hành động trong cell

1. Series đầu nhóm toàn bộ rồi lấy mean top4.

2. Series sau query("top4") trước khi nhóm nên mẫu số chỉ còn hàng thành công và mean luôn 1.

3. pd.concat với từ điển đặt nhãn mô tả rõ hai cột; axis=1 ghép cột theo index chiến thuật. Code hợp lệ về Python nhưng cột thứ hai trả lời câu hỏi khác.

#### Bài học

Nhãn cột “Lọc top 4 trước, rồi lấy mean” không nói Python đã báo lỗi; mã vẫn chạy chính xác. Sai ở đây là câu hỏi phân tích và mẫu số. Đây là lý do phải mô tả tập dữ liệu sau mỗi bước lọc.

### Cell 53 — Mở đầu tóm tắt theo nhóm

- **Loại:** Markdown
- **ID:** tft-054-group-summary-heading

Cell chuẩn bị mở rộng từ một tỷ lệ sang nhiều đại lượng cho mỗi chiến thuật: cỡ mẫu, hạng trung bình, tỷ lệ top 4, tỷ lệ thắng và trung bình tài nguyên.

### Cell 54 — Bảng tóm tắt nhiều đại lượng

- **Loại:** Code
- **ID:** tft-055-group-table

#### Mục đích

Tạo một bảng mô tả đầy đủ hơn cho ba chiến thuật trên toàn bộ dữ liệu.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `tom_tat_chien_thuat` | Bảng một hàng cho mỗi chiến thuật trên toàn dữ liệu. |
| `so_tran` | Số lượt người-chơi–trận. |
| `placement_tb` | Placement trung bình. |
| `ti_le_top4, ti_le_thang` | Trung bình các cột Boolean top4 và win. |
| `mau_4_1_tb, vang_4_1_tb` | Trung bình máu và vàng tại stage 4-1. |

#### Các hành động trong cell

1. groupby chiến thuật với observed=True chia toàn bảng thành ba nhóm.

2. agg lấy size của placement, mean của placement/top4/win/máu/vàng; win đã là Boolean nên không cần lambda tạo lại điều kiện thắng.

3. reset_index đưa chien_thuat thành cột; không làm tròn số nguồn. Cách pandas hiển thị đã được đặt ở Cell 01.

#### Cách đọc

Không nên chỉ nhìn một cột. Ví dụ một chiến thuật có tỷ lệ top 4 tốt hơn có thể đồng thời có phân phối bậc hoặc nhịp lobby khác. **so_tran** luôn cần được báo cáo cùng tỷ lệ để đánh giá độ ổn định.

### Cell 55 — Vẽ tỷ lệ top 4 từ bảng đã tóm tắt

- **Loại:** Code
- **ID:** tft-056-group-plot

#### Mục đích

Chuyển cột ti_le_top4 của bảng tóm tắt thành biểu đồ cột phần trăm.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `tom_tat_chien_thuat` | Bảng đã tóm tắt, không phải dữ liệu từng trận. |
| `g` | Biểu đồ cột của ti_le_top4, có đường tham chiếu 0.5. |

#### Các hành động trong cell

1. ggplot nhận bảng tóm tắt; aes đặt chien_thuat lên x và ti_le_top4 lên y. geom_col dùng đúng chiều cao đã tính, không đếm hàng lần nữa.

2. scale_fill_manual giữ màu. geom_hline(yintercept=0.5,linetype="dashed") tạo mốc chung toàn lobby; caption giải thích đường này.

3. scale_y_continuous(labels=phan_tram,limits=(0,0.75)) đổi nhãn thành phần trăm và đặt gốc 0.

#### Cách đọc

Chiều cao cột là tỷ lệ, không phải số lượng. Biểu đồ dựa trên bảng đã tóm tắt nên mỗi cột đại diện một nhóm, không phải một quan sát cá nhân.

**Đọc code vẽ bằng Plotnine.** Đọc ánh xạ đầu tiên `x='chien_thuat', y='ti_le_top4', fill='chien_thuat'` trong `aes`; tên biến được lấy từ bảng dữ liệu của lớp tương ứng. `geom_hline` thêm đường ngang tại `yintercept`. `geom_col` vẽ cột có độ dài lấy trực tiếp từ giá trị `y` đã tính trong bảng. Thử đổi một thuộc tính hiển thị đang có trong lớp vẽ hoặc `theme`, rồi chạy lại ô; giữ dữ liệu để so sánh hình trước và sau.

### Cell 56 — Bài tập nhóm theo hai biến

- **Loại:** Markdown
- **ID:** tft-057-group-exercise

Cell đặt yêu cầu phân tầng kết quả theo cả nhịp lobby và chiến thuật. Mục tiêu là kiểm tra liệu thứ hạng chung giữa chiến thuật có còn giữ nguyên trong từng loại lobby hay không.

### Cell 57 — Tóm tắt theo nhịp lobby và chiến thuật

- **Loại:** Code
- **ID:** tft-058-group-two-vars

#### Mục đích

Tạo sáu nhóm từ tích của 2 mức nhịp lobby và 3 chiến thuật.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `top4_theo_nhip` | Bảng nhóm theo nhịp lobby × chiến thuật. |
| `so_tran` | Số lượt trong đúng tổ hợp nhóm. |
| `ti_le_top4` | Tỷ lệ top4 với mẫu số là số lượt của đúng tổ hợp đó. |

#### Các hành động trong cell

1. groupby(["nhip_lobby","chien_thuat"],observed=True) tạo các tổ hợp thực xuất hiện.

2. agg tính size của top4 và mean top4. reset_index đưa hai biến nhóm thành cột để đọc sáu hàng.

#### Cách đọc

So sánh chiến thuật **trong cùng một nhịp**, rồi mới so sánh nhịp trong cùng chiến thuật. Không nên so hai hàng vừa khác nhịp vừa khác chiến thuật rồi gán chênh lệch cho một yếu tố duy nhất.

### Cell 58 — Giới thiệu nghịch lý Simpson

- **Loại:** Markdown
- **ID:** tft-059-simpson-intro

Cell chỉ ra rằng kết luận gộp có thể khác kết luận trong từng nhóm điều kiện. Dữ liệu thật phía trên gợi ý vấn đề, nhưng để nhìn hiện tượng thật rõ, cell sau dùng một ví dụ số được thiết kế chính xác.

### Cell 59 — Tạo ví dụ Simpson có kiểm soát

- **Loại:** Code
- **ID:** tft-060-simpson-table

#### Mục đích

Xây dựng một bảng nhỏ trong đó Fast 8 có tỷ lệ top 4 cao hơn Reroll ở cả lobby chậm lẫn nhanh, nhưng thấp hơn khi gộp hai loại lobby.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `simpson_tft` | Bảng bốn hàng nhịp lobby × chiến thuật chứa top4 và tong. |
| `top4, tong` | Số lượt đạt top4 và tổng lượt trong từng tổ hợp. |
| `ti_le_top4` | top4/tong, tính riêng mỗi hàng. |
| `theo_nhip` | Bảng pivot tỷ lệ, hàng theo Chậm/Nhanh và cột theo chiến thuật. |
| `gop` | Bảng cộng top4, tong qua hai nhịp rồi mới chia để tính tỷ lệ gộp. |

#### Các hành động trong cell

1. pd.DataFrame tạo đúng bốn hàng số đếm. Phép chia top4/tong tạo tỷ lệ từng hàng.

2. pivot và loc[["Chậm","Nhanh"]] đặt thứ tự hàng trong bảng tỷ lệ có điều kiện.

3. groupby(...)[["top4","tong"]].sum() cộng tử và mẫu trước khi chia; không lấy mean đơn giản của tỷ lệ nhóm.

4. print/display trình bày hai bảng để đối chiếu tỷ lệ có điều kiện và tỷ lệ gộp.

#### Cách đọc số liệu

- Lobby chậm: Fast 8 95%, Reroll 90%.
- Lobby nhanh: Fast 8 20%, Reroll 10%.
- Gộp: Fast 8 35%, Reroll 82%.

Sự đảo chiều xảy ra vì Fast 8 có phần lớn quan sát ở lobby nhanh, nơi top 4 khó hơn; Reroll có phần lớn quan sát ở lobby chậm, nơi top 4 dễ hơn.

### Cell 60 — Trực quan hóa nghịch lý Simpson

- **Loại:** Code
- **ID:** tft-061-simpson-plot

#### Mục đích

Đặt tỷ lệ có điều kiện và tỷ lệ gộp cạnh nhau để thấy sự đảo chiều.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `bang_simpson` | Bảng dài ghép tỷ lệ từng nhịp và tỷ lệ gộp, không tính lại tỷ lệ. |
| `nhom, o` | Nhãn trục x và nhãn facet; categorical giữ ô từng nhịp ở trái, ô gộp ở phải. |
| `d` | Bảng tạm trong lambda tạo nhom từ chien_thuat ở ô gộp. |
| `g` | Một biểu đồ cột dodge, chia hai facet free_x và dùng cùng trục y 0–100%. |

#### Các hành động trong cell

1. pd.concat ghép dữ liệu từng nhịp với bảng gộp. assign đặt nhãn nhom/o; không tính lại thống kê.

2. pd.Categorical cho o giữ thứ tự trái là từng nhịp, phải là gộp. facet_wrap(...,scales="free_x") cho mỗi ô có nhãn x phù hợp.

3. geom_col(position="dodge") đặt cột hai chiến thuật cạnh nhau; cả hai facet dùng cùng y 0–100%. scale_fill_manual giữ bảng mã màu.

#### Bài học

Biểu đồ không tự giải quyết nhiễu. Điều quan trọng là chọn đúng mức tổng hợp và hiển thị biến phân tầng có liên quan.

**Đọc code vẽ bằng Plotnine.** Đọc ánh xạ đầu tiên `x='nhom', y='ti_le_top4', fill='chien_thuat'` trong `aes`; tên biến được lấy từ bảng dữ liệu của lớp tương ứng. `geom_col` vẽ cột có độ dài lấy trực tiếp từ giá trị `y` đã tính trong bảng. Facet chia cùng một biểu đồ theo biến nhóm; kiểm tra tham số `scales` trước khi so độ lớn giữa các ô. Thử đổi một thuộc tính hiển thị đang có trong lớp vẽ hoặc `theme`, rồi chạy lại ô; giữ dữ liệu để so sánh hình trước và sau.

### Cell 61 — Giải thích sự đảo chiều

- **Loại:** Markdown
- **ID:** tft-062-simpson-explain

Cell diễn giải nguyên nhân bằng trọng số mẫu. Tỷ lệ gộp không phải trung bình đơn giản của hai tỷ lệ nhóm; nó là trung bình có trọng số, trong đó nhóm có nhiều quan sát đóng góp nhiều hơn. Khi phân bố chiến thuật giữa lobby dễ và khó rất khác nhau, kết luận gộp có thể đảo chiều.

Cell cũng nhắc rằng phân tầng là công cụ mô tả quan trọng nhưng chưa đủ để khẳng định nhân quả. Việc chọn biến điều kiện cần dựa trên hiểu biết về cơ chế tạo dữ liệu.

### Cell 62 — Số lượng và tỷ lệ dùng mẫu số khác nhau

- **Loại:** Code
- **ID:** tft-063-count-vs-rate

#### Mục đích

So sánh bảng đếm với bảng tỷ lệ top 4 theo loại lõi bổ trợ.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `bang_loi` | Bảng chéo số đếm loại lõi × top4, reindex theo LOI. |
| `ti_le_loi` | Bảng chéo normalize="index": mỗi hàng được chia cho tổng chính hàng đó. |
| `dem_dai, ti_le_dai` | Hai bảng dài dùng để vẽ, giữ lại cả Ngoài top 4 và Top 4. |
| `ket_qua, n, rate` | Nhãn kết quả, số đếm và tỷ lệ; categorical giữ thứ tự loại lõi như LOI. |
| `g_dem, g_ty_le` | Biểu đồ cột cạnh nhau của số đếm và cột chồng tỷ lệ. |

#### Các hành động trong cell

1. pd.crosstab đếm các tổ hợp; normalize="index" chia từng hàng cho tổng của chính loại lõi đó. reindex(LOI) giữ thứ tự Kinh tế, Giao tranh, Linh hoạt.

2. rename đổi True/False thành nhãn có nghĩa; reset_index và melt tạo bảng dài. pd.Categorical giữ thứ tự nhóm sau biến đổi.

3. Hình trái geom_col(position="dodge") so sánh số đếm. Hình phải position_stack(reverse=True) đặt Ngoài top 4 dưới, Top 4 trên theo bản gốc.

4. labels=phan_tram chỉ đổi nhãn trục của tỷ lệ. Hai loại biểu đồ giữ mẫu số khác nhau và được ghép bằng |.

#### Cách đọc

Bảng đếm trả lời “có bao nhiêu lượt top 4?”. Bảng tỷ lệ trả lời “trong các lượt dùng lõi này, bao nhiêu phần đạt top 4?”. Một nhóm lớn có thể có nhiều ca top 4 nhưng tỷ lệ thấp hơn nhóm nhỏ.

**Đọc code vẽ bằng Plotnine.** Đọc ánh xạ đầu tiên `x='loai_loi', y='n', fill='ket_qua'` trong `aes`; tên biến được lấy từ bảng dữ liệu của lớp tương ứng. `geom_col` vẽ cột có độ dài lấy trực tiếp từ giá trị `y` đã tính trong bảng. Thử đổi một thuộc tính hiển thị đang có trong lớp vẽ hoặc `theme`, rồi chạy lại ô; giữ dữ liệu để so sánh hình trước và sau.

### Cell 63 — Ghi nhớ mẫu số

- **Loại:** Markdown
- **ID:** tft-064-count-vs-rate-note

Cell nhấn mạnh rằng mọi tỷ lệ phải đi cùng câu hỏi “chia cho cái gì?”. Khi **normalize="index"**, mẫu số là tổng từng hàng, tức tổng số lượt trong từng loại lõi.

### Cell 64 — Mở đầu trục tung dễ gây hiểu sai

- **Loại:** Markdown
- **ID:** tft-065-axis-heading

Cell chuyển từ xử lý dữ liệu sang quyết định trình bày. Cùng một tỷ lệ có thể trông chênh lệch rất lớn nếu trục tung bị cắt sát giá trị.

### Cell 65 — Trục đầy đủ và trục bị cắt

- **Loại:** Code
- **ID:** tft-066-axis-plot

#### Mục đích

Cho thấy tác động thị giác của giới hạn trục y.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `rates` | Series ti_le_top4 có index chien_thuat, reindex đúng CHIEN_THUAT. |
| `bang_rates` | Bảng dùng cho cả hai hình; categorical giữ cùng thứ tự chiến thuật. |
| `lo, hi` | Cận dưới max(0, min(rates) − 0.035) và cận trên min(1, max(rates) + 0.035). |
| `g_day_du, g_cat` | Hai hình cùng dữ liệu, màu và geom; khác coord_cartesian với ylim=(0,1) hoặc (lo,hi). |

#### Các hành động trong cell

1. set_index, chọn Series và reindex giữ tỷ lệ theo đúng thứ tự CHIEN_THUAT. reset_index tạo bang_rates; categorical giữ thứ tự trên x.

2. Tính lo/hi đúng cận động ±0.035 quanh min/max, giới hạn trong 0–1.

3. Cả hai hình dùng cùng ggplot, geom_col và bảng màu; chỉ coord_cartesian(ylim=...) khác nhau. coord_cartesian cắt khung nhìn, không loại hay tính lại dữ liệu.

4. Định dạng phần trăm và ghép cạnh nhau giúp thấy tác động của phạm vi trục.

#### Cách đọc

Biểu đồ phải phóng đại chênh lệch vì bỏ phần trục từ 0 tới cận **lo**. Với biểu đồ cột, chiều dài cột thường được so từ gốc 0, nên cắt trục đặc biệt dễ gây ấn tượng sai. Nếu cần phóng to khác biệt, nên báo rõ và cân nhắc dùng điểm với khoảng tin cậy.

**Đọc code vẽ bằng Plotnine.** Đọc ánh xạ đầu tiên `x='chien_thuat', y='rate', fill='chien_thuat'` trong `aes`; tên biến được lấy từ bảng dữ liệu của lớp tương ứng. `geom_col` vẽ cột có độ dài lấy trực tiếp từ giá trị `y` đã tính trong bảng. Thử đổi một thuộc tính hiển thị đang có trong lớp vẽ hoặc `theme`, rồi chạy lại ô; giữ dữ liệu để so sánh hình trước và sau.

### Cell 66 — Nguyên tắc chọn trục

- **Loại:** Markdown
- **ID:** tft-067-axis-note

Cell kết luận rằng thay đổi trục không thay dữ liệu nhưng thay đổi cách người xem cảm nhận kích thước hiệu ứng. Người phân tích có trách nhiệm làm rõ giới hạn trục.

---

## Phần 5 — Thử thách điều kiện hóa và mini case study

### Cell 67 — Câu hỏi thử thách về máu và top 4

- **Loại:** Markdown
- **ID:** tft-068-part-6

Cell đặt bài toán theo hai tầng: trước hết so sánh gộp theo mức máu, sau đó kiểm tra lại trong từng bậc. Cấu trúc này luyện thói quen không dừng ở một kết luận tổng hợp duy nhất.

### Cell 68 — Kết quả gộp theo nhóm máu

- **Loại:** Code
- **ID:** tft-069-challenge-pooled

#### Mục đích

So sánh các quan sát có máu dưới 50 với các quan sát có máu từ 50 trở lên trên toàn bộ dữ liệu.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `phan_tich_mau` | Bảng gộp theo hai nhóm máu, chưa điều kiện hóa theo bậc. |
| `nhom_mau` | np.where tạo nhãn Ít nhất 50 hoặc Dưới 50 từ mau_4_1. |
| `so_tran, ti_le_top4, placement_tb` | Cỡ mẫu, tỷ lệ top4 và placement trung bình trong mỗi nhóm. |

#### Các hành động trong cell

1. assign + np.where đặt nhãn hai nhóm máu theo ngưỡng 50.

2. groupby("nhom_mau",observed=True) nhóm toàn bộ bậc. agg tính size top4, mean top4 và mean placement.

3. sort_index xếp nhãn nhóm; một hàng đầu ra là một nhóm máu, không còn là một người chơi.

#### Cách đọc

Trong dữ liệu mô phỏng, nhóm máu ≥ 50 có tỷ lệ top 4 cao hơn và hạng trung bình tốt hơn. Đây là một mối liên hệ mô tả mạnh, nhưng máu được đo trong quá trình trận đấu và có thể vừa phản ánh vừa chịu ảnh hưởng của tình trạng thắng thế.

### Cell 69 — Điều kiện hóa thêm theo bậc

- **Loại:** Code
- **ID:** tft-070-challenge-conditioned

#### Mục đích

Kiểm tra mối liên hệ máu–top 4 riêng trong Silver, Gold, Platinum và Diamond.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `phan_tich_mau_theo_bac` | Bảng theo tổ hợp bac_xep_hang × nhom_mau. |
| `nhom_mau` | Hai mức máu giữ cùng định nghĩa ≥ 50 với Cell 68. |
| `so_tran, ti_le_top4` | Cỡ mẫu và tỷ lệ top4 trong đúng bậc và nhóm máu. |

#### Các hành động trong cell

1. assign tạo cùng nhãn nhom_mau như Cell 68.

2. groupby(["bac_xep_hang","nhom_mau"],observed=True) thêm điều kiện bậc trước khi tính tỷ lệ.

3. agg size/mean top4 và reset_index tạo bảng có hai biến nhóm; một hàng là một tổ hợp bậc × nhóm máu.

#### Cách đọc

So hai nhóm máu trong cùng một bậc. Nếu mối liên hệ vẫn cùng chiều ở cả bốn bậc, nó không chỉ là hệ quả của việc các bậc có phân bố máu khác nhau. Dù vậy, vẫn chưa thể gọi là tác động nhân quả vì còn nhiều biến chưa điều kiện hóa và thứ tự thời gian cần xem xét.

### Cell 70 — Vẽ tỷ lệ có điều kiện theo bậc

- **Loại:** Code
- **ID:** tft-071-challenge-plot

#### Mục đích

Biến bảng conditioned thành biểu đồ cột ghép để so sánh hai nhóm máu trong từng bậc.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `nhom` | Thứ tự Dưới 50, Ít nhất 50 của các cột trong mỗi bậc. |
| `bang_mau` | Bản sao bảng tỷ lệ đã điều kiện hóa, thêm thứ tự categorical cho nhom_mau. |
| `g` | Biểu đồ cột dodge theo bậc, tỷ lệ trên y, màu tô theo nhóm máu. |

#### Các hành động trong cell

1. copy giữ bảng tóm tắt gốc. pd.Categorical quy định thứ tự Dưới 50 rồi Ít nhất 50.

2. aes đặt bậc lên x, tỷ lệ lên y, nhóm máu vào fill; geom_col(position="dodge",width=0.72) đặt hai cột cạnh nhau trong mỗi bậc.

3. scale_fill_manual giữ màu hai nhóm; scale_y_continuous đặt 0–100% và phan_tram đổi nhãn. Không tính lại tỷ lệ trong lớp vẽ.

#### Cách đọc

So sánh chiều cao hai cột trong mỗi cụm bậc. Không chỉ nhìn các cột cùng màu qua các bậc, vì câu hỏi chính là chênh lệch nhóm máu trong cùng điều kiện bậc.

**Đọc code vẽ bằng Plotnine.** Đọc ánh xạ đầu tiên `x='bac_xep_hang', y='ti_le_top4', fill='nhom_mau'` trong `aes`; tên biến được lấy từ bảng dữ liệu của lớp tương ứng. `geom_col` vẽ cột có độ dài lấy trực tiếp từ giá trị `y` đã tính trong bảng. Thử đổi một thuộc tính hiển thị đang có trong lớp vẽ hoặc `theme`, rồi chạy lại ô; giữ dữ liệu để so sánh hình trước và sau.

### Cell 71 — Diễn giải và câu hỏi mở

- **Loại:** Markdown
- **ID:** tft-072-open-challenge

Cell cung cấp diễn giải mô tả: nhóm máu cao có kết quả tốt hơn cả khi gộp lẫn trong từng bậc. Đồng thời cell chặn một suy luận sai: không thể kết luận “giữ máu gây ra top 4” từ mối liên hệ này.

Câu hỏi mở yêu cầu người học tự chọn một điều kiện TFT, xác định mẫu số, bảng tóm tắt và loại biểu đồ. Đây là bước chuyển từ làm theo mẫu sang thiết kế phân tích.

### Cell 72 — Mở đầu mini case study về scouting

- **Loại:** Markdown
- **ID:** tft-073-case-heading

Cell đặt câu hỏi tổng hợp: số lần scout liên hệ thế nào với top 4? Bài toán sử dụng lại kỹ năng xử lý thiếu, tạo nhóm, tính tỷ lệ và trực quan hóa.

### Cell 73 — Tạo nhóm scouting và bảng tóm tắt

- **Loại:** Code
- **ID:** tft-074-case-table

#### Mục đích

Chuyển số lần scout từ biến đếm sang ba mức dễ so sánh, rồi tính kết quả cho từng mức.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `case_scout` | Bảng thống kê sau bỏ scout thiếu, tạo nhóm scout, nhóm và tóm tắt. |
| `d` | Bảng đã dropna đi qua lambda trong assign. |
| `nhom_scout` | Các nhãn 0–1 lần, 2–3 lần, Từ 4 lần từ các biên −0.1, 1, 3, +∞. |
| `n, ti_le_top4, placement_tb` | Số lượt, tỷ lệ top4 và placement trung bình trong từng nhóm scout. |

#### Các hành động trong cell

1. dropna chỉ giữ hàng có scout. assign với lambda d gọi pd.cut trên bảng này.

2. pd.cut mặc định đóng bên phải: (−0.1,1], (1,3], (3,+∞]. Với số đếm không âm, ba nhóm đúng 0–1, 2–3 và từ 4 lần.

3. groupby nhom_scout với observed=True và agg tạo n, ti_le_top4, placement_tb; reset_index đưa nhãn nhóm thành cột.

#### Cách đọc

Trong dữ liệu mô phỏng, nhóm scout ≥4 có tỷ lệ top 4 cao nhất. Tuy nhiên, việc chia 0–1, 2–3, ≥4 là một quyết định phân tích; đổi ngưỡng có thể đổi kết quả. Cần báo rõ các ngưỡng và không thử nhiều cách rồi chỉ chọn cách đẹp nhất.

### Cell 74 — Vẽ kết quả case study

- **Loại:** Code
- **ID:** tft-075-case-plot

#### Mục đích

Trình bày tỷ lệ top 4 theo ba nhóm scouting và ghi trực tiếp cỡ mẫu lên cột.

#### Tên biến và đối tượng

| Tên | Giải thích |
|---|---|
| `bang_case` | Bản sao case_scout có thêm hai cột phục vụ nhãn. |
| `d, nhan_n` | Bảng đi qua lambda và chuỗi nhãn "n = ..." của cỡ mẫu. |
| `y_nhan` | ti_le_top4 + 0.025 để nhãn nằm trên đầu cột. |
| `g` | Biểu đồ cột tỷ lệ có geom_text ghi cỡ mẫu. |

#### Các hành động trong cell

1. assign tạo nhan_n từ n.astype(str) và y_nhan cao hơn đầu cột 0.025.

2. geom_col dùng ti_le_top4 đã tính; geom_text ánh xạ y_nhan/nhan_n để ghi cỡ mẫu.

3. scale_fill_manual chọn màu nhóm; scale_y_continuous đặt 0–100%, phan_tram đổi nhãn; show() hiển thị PNG.

#### Cách đọc

Đọc đồng thời chiều cao cột và n. Một tỷ lệ từ nhóm rất nhỏ thường bất định hơn tỷ lệ từ nhóm lớn, dù notebook chưa vẽ khoảng tin cậy.

**Đọc code vẽ bằng Plotnine.** Đọc ánh xạ đầu tiên `y='y_nhan'` trong `aes`; tên biến được lấy từ bảng dữ liệu của lớp tương ứng. `geom_text` đặt chữ từ biến `label` tại tọa độ của từng hàng. `geom_col` vẽ cột có độ dài lấy trực tiếp từ giá trị `y` đã tính trong bảng. Thử đổi một thuộc tính hiển thị đang có trong lớp vẽ hoặc `theme`, rồi chạy lại ô; giữ dữ liệu để so sánh hình trước và sau.

### Cell 75 — Kết luận case study và giới hạn

- **Loại:** Markdown
- **ID:** tft-076-case-answer

Cell diễn giải kết quả dưới dạng **liên hệ**, không dùng ngôn ngữ nhân quả. Những người chơi có lợi thế hoặc kỹ năng cao có thể vừa scout nhiều vừa top 4 nhiều; do đó scouting có thể là dấu hiệu của một trạng thái hoặc phong cách chơi, không nhất thiết là nguyên nhân độc lập.

Cell cũng nhắc lại tác động của dữ liệu thiếu và phân nhóm ngưỡng.

### Cell 76 — Tổng kết tuần học

- **Loại:** Markdown
- **ID:** tft-077-summary

Cell cuối gom các năng lực chính:

- đọc biểu đồ theo dữ liệu, mapping, geometry và facet;
- dùng điểm, đường, boxplot và cột đúng với cấu trúc câu hỏi;
- phân biệt chọn cột, lọc hàng, tạo biến, nhóm và tóm tắt;
- kiểm tra dữ liệu thiếu và mẫu số;
- nhận ra kết quả gộp có thể che kết quả có điều kiện;
- mô tả mối liên hệ mà không vội khẳng định nhân quả.

Câu hỏi kết thúc yêu cầu người học tự thiết kế một phân tích TFT. Một câu trả lời tốt phải nêu rõ: đơn vị quan sát, biến kết quả, biến giải thích, điều kiện lọc, mẫu số của tỷ lệ và giới hạn diễn giải.

---

## Bảng tra nhanh các hành động pandas/Plotnine trong notebook

| Hành động | Cách hiểu ngắn gọn | Cell tiêu biểu |
|---|---|---|
| **head** | Xem một số hàng đầu để kiểm tra cấu trúc. | 02, 19, 37 |
| **query** | Giữ các hàng thỏa điều kiện. | 28, 37, 39, 48, 50, 52 |
| **dropna** | Loại hàng thiếu ở các cột được chỉ định. | 33, 73 |
| **assign** | Tạo cột mới trong một pipeline. | 41, 48, 68 |
| **groupby** | Chia dữ liệu thành nhóm để tính riêng. | 48, 50, 54, 57, 69, 73 |
| **agg** | Tạo một hay nhiều thống kê tóm tắt. | 48, 50, 54, 57, 68, 69, 73 |
| **reset_index** | Đưa biến nhóm từ index trở lại cột. | 48, 54, 57, 69, 73 |
| **pivot** | Chuyển bảng dài thành bảng rộng. | 59 |
| **crosstab** | Lập bảng chéo đếm hoặc tỷ lệ. | 62 |
| **rolling** | Tính thống kê trên cửa sổ các quan sát liên tiếp. | 02, 25 |
| **ggplot + aes + geom_point** | Chọn dữ liệu, ánh xạ và vẽ từng quan sát của hai biến số. | 06, 08, 12, 14, 28, 33 |
| **geom_line** | Vẽ đường theo biến x có thứ tự; nhóm đường qua aes. | 16, 20, 22, 25 |
| **geom_boxplot** | So sánh phân phối một biến số giữa các nhóm. | 06, 10, 30 |
| **geom_col** | Vẽ chiều cao số lượng hoặc tỷ lệ đã tóm tắt. | 06, 55, 60, 65, 70, 74 |
| **scale_y_reverse** | Đưa hạng 1 lên phía trên, giữ đầy đủ hạng 1–8. | Nhiều cell có trục placement |
| **scale_y_continuous(labels=phan_tram)** | Giữ tỷ lệ 0–1, đổi nhãn trục thành phần trăm. | 55, 60, 65, 70, 74 |
| **facet_wrap** | Chia một biểu đồ thành các ô theo biến nhóm. | 12, 60 |
| **coord_cartesian** | Chỉ thay phạm vi nhìn, không loại dữ liệu. | 65 |
| **show()** | Hiển thị và lưu output PNG của biểu đồ Plotnine. | Các cell vẽ |
| **melt** | Chuyển nhiều cột giá trị thành bảng dài cho aes/geom. | 20, 22, 25, 62 |
| **geom_rect + bang_histogram** | Vẽ histogram với đúng biên và tần số/mật độ đã tính. | 06, 45 |
| **\|**, **/** | Ghép các biểu đồ khác nhau cạnh nhau hoặc trên/dưới. | 06, 10, 14, 16, 20, 45, 62, 65 |

## Cách tự kiểm tra sau khi học

Trước khi chấp nhận một biểu đồ hoặc bảng kết quả, hãy trả lời được sáu câu hỏi:

1. Một hàng dữ liệu đại diện cho đối tượng nào?
2. Những hàng nào đã bị lọc hoặc bị loại do thiếu dữ liệu?
3. Mỗi biến và mỗi tên viết tắt có ý nghĩa gì?
4. Nếu có tỷ lệ, tử số và mẫu số là gì?
5. Biểu đồ đang thể hiện quan sát thô, phân phối hay số liệu đã tóm tắt?
6. Kết luận là mô tả mối liên hệ hay đang vô tình khẳng định nhân quả?

Nếu chưa trả lời được một trong sáu câu, nên quay lại cell tạo dữ liệu hoặc pipeline trước khi diễn giải kết quả.
