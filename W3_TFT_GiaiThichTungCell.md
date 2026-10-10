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
| **plt** | Tên viết tắt của matplotlib.pyplot, dùng để vẽ biểu đồ. |
| **rng** | Bộ sinh số ngẫu nhiên. Vì có hạt giống cố định nên kết quả mô phỏng có thể tái lập. |
| **fig** | Toàn bộ khung hình; có thể chứa một hoặc nhiều biểu đồ con. |
| **ax**, **axes** | Một trục biểu đồ hoặc tập hợp các trục biểu đồ con. |
| **d**, **g** | Tên biến ngắn cho một bảng con trong lúc lọc hoặc lặp. Đây chỉ là biến tạm. |
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
| **np** | NumPy; hỗ trợ mảng số, logarit, xác suất và số ngẫu nhiên. |
| **pd** | pandas; hỗ trợ bảng dữ liệu. |
| **plt** | pyplot; giao diện vẽ biểu đồ. |
| **PercentFormatter** | Bộ định dạng giúp trục tung hiển thị 0.5 thành 50%. |
| **display** | Hàm hiển thị DataFrame đẹp trong Jupyter. |
| **rng** | Bộ sinh số ngẫu nhiên được tạo với hạt giống 202503. |
| **BAC** | Danh sách bậc xếp hạng: Silver, Gold, Platinum, Diamond. Viết hoa để nhấn mạnh đây là một hằng số dùng chung. |
| **CHIEN_THUAT** | Ba nhóm chiến thuật: Reroll, Tempo, Fast 8. |
| **LOI** | Ba lối chơi: Chuỗi thắng, Cân bằng, Chuỗi thua. |
| **MAU_CHIEN_THUAT** | Từ điển ánh xạ mỗi chiến thuật sang một màu cố định. |

#### Các hành động trong cell

1. **import ... as ...** nạp thư viện và đặt bí danh ngắn để mã phía sau dễ đọc.
2. **plt.style.use** chọn bộ định dạng seaborn-v0_8-whitegrid, tạo nền lưới nhẹ cho biểu đồ.
3. **pd.set_option** quy định số cột tối đa và định dạng số thực khi pandas hiển thị bảng.
4. **np.random.default_rng(202503)** tạo bộ sinh số ngẫu nhiên hiện đại của NumPy. Số 202503 là hạt giống; chạy lại notebook vẫn nhận cùng dữ liệu.
5. Các danh sách và từ điển cuối cell đóng vai trò như “bảng mã” chung, tránh gõ lại tên nhóm hoặc màu ở nhiều nơi.

#### Điều cần nhớ

Đặt hạt giống không làm dữ liệu hết ngẫu nhiên về mặt mô phỏng; nó chỉ làm cho một chuỗi ngẫu nhiên cụ thể có thể tái lập. Đây là yêu cầu quan trọng khi viết học liệu hoặc báo cáo phân tích.

### Cell 02 — Tạo dữ liệu TFT mô phỏng

- **Loại:** Code
- **ID:** tft-003-generate-data

#### Mục đích

Đây là cell xây dựng toàn bộ dữ liệu dùng trong bài. Có thể coi nó là một **quy trình sinh dữ liệu**: từ bậc xếp hạng và đặc điểm người chơi, notebook tạo lobby, hành vi trong trận, điểm hiệu suất ẩn, thứ hạng cuối trận và một chuỗi lịch sử của một người chơi.

#### Nhóm biến 1: quy mô và hồ sơ người chơi

| Tên | Giải thích |
|---|---|
| **so_lobby** | Số lobby cần mô phỏng, bằng 120. |
| **so_nguoi_choi** | Số người chơi khác nhau trong danh sách mô phỏng, bằng 96. |
| **player_pools** | Từ điển chứa danh sách ID người chơi của từng bậc. |
| **player_skill** | Từ điển lưu mức kỹ năng ẩn của từng người chơi. |
| **bac_skill** | Mức kỹ năng cơ sở gắn với từng bậc xếp hạng. |
| **i** | Chỉ số tạm khi lặp qua các bậc. |
| **bac** | Bậc xếp hạng hiện tại trong vòng lặp. |
| **player_id** | Mã định danh người chơi, ví dụ P001. |
| **rows** | Danh sách rỗng dùng để tích lũy từng hàng dữ liệu trước khi tạo DataFrame. |

**player_pools** bảo đảm mỗi người chơi thuộc ổn định một bậc. **player_skill** thêm khác biệt cá nhân trong cùng một bậc bằng nhiễu chuẩn nhỏ. Kỹ năng này là biến ẩn dùng để tạo kết quả, không được đưa vào bảng cuối cùng như một thông tin quan sát trực tiếp.

#### Nhóm biến 2: tạo từng lobby

| Tên | Giải thích |
|---|---|
| **lobby_no** | Số thứ tự lobby trong vòng lặp, chạy từ 1 đến 120. |
| **lobby_id** | Mã lobby dạng L001, L002, ... |
| **bac** | Bậc chung của lobby đang được tạo. |
| **p_nhanh** | Xác suất lobby có nhịp nhanh, phụ thuộc vào bậc. |
| **nhip_lobby** | Nhãn Nhanh hoặc Chậm của lobby. |
| **nguoi_choi_lobby** | Tám người chơi được lấy không hoàn lại cho lobby. |
| **lobby_rows** | Tám bản ghi tạm của lobby hiện tại. |

**rng.choice(..., replace=False)** lấy 8 người chơi khác nhau trong cùng một lobby. Tham số **replace=False** có nghĩa là không hoàn lại, nên một người không thể xuất hiện hai lần trong cùng trận.

Xác suất lobby nhanh tăng theo bậc. Đây là một lựa chọn của mô hình mô phỏng, được dùng về sau để minh họa điều kiện hóa và nghịch lý Simpson.

#### Nhóm biến 3: hành vi và trạng thái của từng người chơi

| Tên | Giải thích |
|---|---|
| **p_chien_thuat** | Vector xác suất chọn Reroll, Tempo hoặc Fast 8 ở lobby hiện tại. |
| **chien_thuat** | Chiến thuật được lấy ngẫu nhiên cho một người chơi. |
| **loi** | Lối chơi được lấy ngẫu nhiên. |
| **ky_nang** | Kỹ năng ẩn của người chơi hiện tại. |
| **cap_do** | Cấp độ cuối trận, chịu ảnh hưởng của chiến thuật và nhiễu. |
| **vang** | Lượng vàng còn lại cuối trận. |
| **mau_linh_thu** | Máu linh thú ở thời điểm quan sát. |
| **gia_tri_doi_hinh** | Tổng giá trị đội hình, được giới hạn trong khoảng hợp lý. |
| **so_lan_scout** | Số lần người chơi quan sát bàn đối thủ. |
| **sat_thuong** | Tổng sát thương gây ra. |
| **loi_bo_tro** | Nhóm lõi bổ trợ: Kinh tế, Giao tranh hoặc Linh hoạt. |

Các phép **np.clip** cắt giá trị tại cận dưới và cận trên. Ví dụ máu không được âm hoặc vượt quá 100; cấp độ được giữ trong khoảng 5–10. **round** làm tròn đại lượng về đơn vị phù hợp.

Các biểu thức xác suất không nhằm tái tạo chính xác trò chơi. Chúng cố ý tạo ra những mối liên hệ có thể nhìn thấy: Fast 8 thường có cấp cao và nhiều vàng hơn; Reroll có cấu trúc tài nguyên khác; nhịp lobby và kỹ năng cũng tác động đến kết quả.

#### Nhóm biến 4: tạo kết quả cuối trận

| Tên | Giải thích |
|---|---|
| **score** | Điểm hiệu suất ẩn; điểm càng cao thì kết quả dự kiến càng tốt. |
| **strategy_bonus** | Phần cộng/trừ điểm do chiến thuật và nhịp lobby tương tác. |
| **style_bonus** | Phần cộng/trừ do lối chơi. |
| **perf** | Mảng gồm 8 điểm hiệu suất của người chơi trong lobby. |
| **order** | Thứ tự chỉ số sau khi sắp xếp điểm từ cao xuống thấp. |
| **placements** | Mảng chứa thứ hạng 1–8 được gán lại đúng vị trí từng người chơi. |
| **row** | Một từ điển đại diện cho một người chơi trong lobby. |
| **idx**, **place** | Chỉ số người chơi và thứ hạng tương ứng trong vòng lặp gán kết quả. |

**score** kết hợp kỹ năng, máu, giá trị đội hình, cấp độ, scouting, chiến thuật, lối chơi và nhiễu. Sau đó **np.argsort(-perf)** sắp điểm từ lớn xuống nhỏ; dấu trừ đảo chiều vì argsort mặc định xếp tăng dần. Người có điểm cao nhất nhận hạng 1.

Mỗi lobby luôn có đúng một hạng 1, một hạng 2, ..., một hạng 8. Điều này mô phỏng ràng buộc quan trọng của TFT tốt hơn việc sinh hạng độc lập cho từng hàng.

#### Nhóm biến 5: tạo bảng chính

| Tên | Giải thích |
|---|---|
| **tran_tft** | DataFrame chính, mỗi hàng là một người chơi trong một lobby. |
| **top4** | Biến Boolean, True nếu xếp hạng từ 1 đến 4. |
| **sat_thuong_log10** | Logarit cơ số 10 của tổng sát thương. |

**pd.DataFrame(rows)** chuyển danh sách từ điển thành bảng. **pd.Categorical** gắn thứ tự có ý nghĩa cho bậc, chiến thuật, lối chơi và lõi; nhờ đó bảng và biểu đồ không bị sắp theo alphabet ngoài ý muốn.

Khoảng 4% giá trị **so_lan_scout** được đặt thành thiếu bằng **np.nan**. Việc này tạo tình huống thực hành xử lý dữ liệu thiếu ở Cell 33.

#### Nhóm biến 6: tạo lịch sử một người chơi

| Tên | Giải thích |
|---|---|
| **ngay** | 20 ngày liên tiếp, tạo bằng pd.date_range. |
| **trend** | Xu hướng kỹ năng tăng dần theo thời gian. |
| **placement_history** | Chuỗi thứ hạng mô phỏng, có xu hướng cải thiện nhưng vẫn có nhiễu. |
| **lich_su** | DataFrame lịch sử của người chơi P007. |

Lịch sử này là dữ liệu theo thời gian của **cùng một người chơi**, nên nối các điểm bằng đường có ý nghĩa. Nó được dùng để đối chiếu với việc nối những người chơi không liên quan ở Cell 16.

#### Đầu ra

Cell in số lobby, số hàng và 5 hàng đầu. Kết quả mong đợi là **120 lobby** và **960 hàng**, vì 120 × 8 = 960.

#### Lưu ý thống kê

Cell này cho thấy dữ liệu quan sát không tự xuất hiện: chúng được tạo bởi một cơ chế. Nếu nhiều biến cùng đi vào **score**, mối liên hệ giữa một biến và thứ hạng có thể bị trộn với ảnh hưởng của những biến khác. Đây là lý do các phần sau dùng lọc, nhóm và điều kiện hóa.

### Cell 03 — Từ điển dữ liệu và đơn vị quan sát

- **Loại:** Markdown
- **ID:** tft-004-dictionary

Cell định nghĩa ý nghĩa của các cột quan trọng. Đây là bước nên làm trước mọi phân tích: xác định một hàng là gì, mỗi cột đo gì và thang đo có hướng như thế nào.

Đặc biệt, **xep_hang càng nhỏ càng tốt**. Đây là chiều ngược với nhiều đại lượng quen thuộc như điểm số. Khi đọc tương quan hoặc biểu đồ, phải luôn nhớ hạng 1 tốt hơn hạng 8.

Câu Q00 kiểm tra mẫu số: tỷ lệ top 4 theo chiến thuật được tính trên **tất cả lượt người chơi-trận thuộc chiến thuật đó**, không phải trên số người chơi duy nhất hay số lobby.

### Cell 04 — Kiểm tra tính hợp lệ của dữ liệu

- **Loại:** Code
- **ID:** tft-005-data-checks

#### Mục đích

Xác nhận dữ liệu mô phỏng tuân thủ các ràng buộc cơ bản trước khi dùng để phân tích.

#### Tên biến và biểu thức

| Tên/biểu thức | Giải thích |
|---|---|
| **groupby("lobby_id")** | Chia bảng theo từng lobby. |
| **sorted(s) == list(range(1, 9))** | Kiểm tra mỗi lobby có đúng bộ thứ hạng 1–8. |
| **top4.mean()** | Tính tỷ lệ top 4; Boolean True/False được coi là 1/0. |
| **duplicated(["lobby_id", "nguoi_choi"])** | Tìm trường hợp cùng người chơi xuất hiện lặp trong một lobby. |
| **groupby("nguoi_choi")["bac"].nunique()** | Đếm số bậc khác nhau của mỗi người chơi. |
| **kiem_tra** | Bảng mô tả phân phối của một số biến số. |

#### Các hành động

1. **assert** yêu cầu một điều kiện phải đúng. Nếu sai, Python dừng cell và báo lỗi, ngăn phân tích tiếp trên dữ liệu hỏng.
2. **apply(lambda s: ...)** chạy cùng một phép kiểm tra trên Series thứ hạng của từng lobby.
3. Tỷ lệ top 4 toàn bảng phải đúng 0.5 vì mỗi lobby có 4 vị trí top 4 trên 8 người.
4. Hai kiểm tra sau loại trừ trùng người trong lobby và thay đổi bậc bất hợp lý của cùng một người.
5. **describe().T** tính thống kê mô tả rồi chuyển hàng thành cột để dễ đọc.

#### Cách đọc đầu ra

Bảng hiển thị count, mean, std, min, các tứ phân vị và max cho xếp hạng, cấp độ, vàng, máu, giá trị đội hình, scouting và sát thương. **count** của scouting nhỏ hơn 960 vì cell tạo dữ liệu đã cố ý cài một số giá trị thiếu.

### Cell 05 — Mở đầu phần ngữ pháp đồ họa

- **Loại:** Markdown
- **ID:** tft-006-part-1

Cell nêu tư tưởng cốt lõi: một biểu đồ không chỉ là một “loại hình” có sẵn mà là sự kết hợp của dữ liệu, ánh xạ thẩm mỹ, hình học, phép biến đổi thống kê, hệ tọa độ và chia ô. Cách nhìn này giúp người học thiết kế biểu đồ có chủ đích.

### Cell 06 — Bốn câu hỏi, bốn hình học

- **Loại:** Code
- **ID:** tft-007-four-plots

#### Mục đích

Đặt bốn biểu đồ cạnh nhau để cho thấy loại câu hỏi quyết định hình học cần dùng.

#### Tên biến

| Tên | Giải thích |
|---|---|
| **fig** | Khung hình chung. |
| **axes** | Mảng 2 × 2 chứa bốn trục con. |
| **so_nguoi_theo_bac** | Số lượt người chơi-trận ở mỗi bậc. |
| **ax** | Biến tạm đại diện cho từng trục khi lặp. |

#### Bốn hành động vẽ

1. **value_counts().reindex(BAC)** đếm số hàng theo bậc rồi sắp lại đúng thứ tự Silver → Diamond; **bar** vẽ biểu đồ cột.
2. **hist** chia giá trị sát thương thành các khoảng và đếm tần số, thích hợp để xem phân phối một biến số.
3. **scatter** đặt máu trên trục x và thứ hạng trên trục y, thích hợp để xem mối liên hệ giữa hai biến số.
4. **boxplot(column=..., by=...)** so sánh phân phối xếp hạng giữa ba chiến thuật.

**invert_yaxis** đảo trục hạng để hạng 1 xuất hiện phía trên, phù hợp trực giác “cao hơn là tốt hơn”. **alpha** điều chỉnh độ trong suốt; các điểm chồng nhau vẫn có thể nhìn thấy mật độ. **tight_layout** tự điều chỉnh khoảng cách để nhãn không đè lên nhau.

#### Cách đọc đầu ra

- Biểu đồ cột trả lời “có bao nhiêu”.
- Histogram trả lời “phân phối có hình dạng thế nào”.
- Scatter trả lời “hai đại lượng có cùng thay đổi không”.
- Boxplot trả lời “các nhóm khác nhau về trung vị và độ phân tán ra sao”.

**Đọc code vẽ bằng Matplotlib.** `plt.subplots` tạo `Figure` chứa một hoặc nhiều `Axes`; từng lệnh trên `ax`/`axes` vẽ vào hệ trục tương ứng. `axes[0, 0].bar` dùng vị trí và độ dài cột đã tính để vẽ biểu đồ cột. `axes[0, 1].hist` chia quan sát theo `bins`; đọc `density` để phân biệt số đếm và mật độ. `axes[1, 0].scatter` đặt các cặp giá trị vào biểu đồ phân tán; `s` điều chỉnh diện tích điểm và `alpha` điều chỉnh độ trong suốt. Thử đổi một thuộc tính hiển thị đang có, như màu, kích thước hoặc nhãn, rồi chạy lại ô; giữ dữ liệu để so sánh.

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

#### Tên biến

| Tên | Giải thích |
|---|---|
| **mau** | Series màu, nhận màu tương ứng từ cột chien_thuat qua từ điển MAU_CHIEN_THUAT. |
| **kich_thuoc** | Series kích thước điểm, được tính từ gia_tri_doi_hinh. |
| **mau_chon** | Màu tương ứng với mẫu 260 hàng được vẽ. |
| **kich_thuoc_chon** | Kích thước tương ứng với mẫu 260 hàng. |
| **sample(260, random_state=7)** | Chọn 260 hàng cố định để biểu đồ đỡ dày. |
| **d** | Bảng mẫu 260 hàng được dùng trong biểu đồ. |

#### Các hành động

1. **map(MAU_CHIEN_THUAT)** chuyển nhãn chiến thuật thành mã màu.
2. Công thức kích thước chuẩn hóa giá trị đội hình vào khoảng kích thước nhìn được. Việc trừ min và chia cho khoảng biến thiên đưa dữ liệu về gần 0–1; sau đó nhân và cộng tạo cỡ điểm cuối cùng.
3. **sample(..., random_state=7)** lấy một mẫu có thể tái lập. Tham số này độc lập với rng ở Cell 01 vì đây là cơ chế ngẫu nhiên của pandas.
4. **loc[d.index]** lấy màu và kích thước đúng cho các hàng đã được chọn. Nếu không căn theo index, thẩm mỹ có thể gắn nhầm người chơi.
5. **scatter** ánh xạ máu vào x, hạng vào y, chiến thuật vào màu và giá trị đội hình vào kích thước.

#### Cách đọc

Mỗi điểm là một lượt người chơi-trận. Hai điểm gần nhau có máu và thứ hạng gần nhau; màu cho biết chiến thuật; điểm lớn hơn biểu thị đội hình có giá trị cao hơn. Biểu đồ cho thấy nhiều biến cùng lúc, nhưng cũng có nguy cơ quá tải thị giác.

**Đọc code vẽ bằng Matplotlib.** `plt.subplots` tạo `Figure` chứa một hoặc nhiều `Axes`; từng lệnh trên `ax`/`axes` vẽ vào hệ trục tương ứng. `ax.scatter` đặt các cặp giá trị vào biểu đồ phân tán; `s` điều chỉnh diện tích điểm và `alpha` điều chỉnh độ trong suốt. Thử đổi một thuộc tính hiển thị đang có, như màu, kích thước hoặc nhãn, rồi chạy lại ô; giữ dữ liệu để so sánh.

### Cell 09 — Tách cấu trúc biểu đồ thành lời

- **Loại:** Markdown
- **ID:** tft-010-grammar-explain

Cell giải mã chính xác biểu đồ trước: dữ liệu nào, biến nào lên trục nào, màu và kích thước biểu diễn gì. Sau đó nhấn mạnh: giữ nguyên biến nhưng đổi geometry sẽ thay đổi câu hỏi thống kê. Điểm phù hợp để nhìn từng quan sát; boxplot phù hợp để so sánh phân phối nhóm.

### Cell 10 — Cùng biến, khác hình học

- **Loại:** Code
- **ID:** tft-011-geom-compare

#### Mục đích

So sánh trực tiếp hai cách biểu diễn xếp hạng theo chiến thuật.

#### Tên biến

| Tên | Giải thích |
|---|---|
| **xpos** | Vị trí số 0, 1, 2 tương ứng với ba chiến thuật. |
| **jitter** | Nhiễu ngang rất nhỏ để các điểm không chồng khít. |
| **d** | Bảng con chỉ chứa các hàng của một chiến thuật. |
| **i** | Chỉ số chiến thuật trong vòng lặp. |
| **chien_thuat** | Nhãn chiến thuật đang được vẽ. |

#### Các hành động

Biểu đồ trái lặp qua từng chiến thuật, tạo vị trí x cố định rồi cộng **jitter**. Jitter không thay đổi dữ liệu xếp hạng; nó chỉ dịch điểm theo chiều ngang để thấy mật độ. Biểu đồ phải giữ nhãn trục x bằng **set_xticks** và **set_xticklabels** vì vị trí thực tế là số 0–2.

Biểu đồ phải dùng **boxplot** để tóm tắt trung vị, tứ phân vị và phạm vi. **patch_artist=True** cho phép tô màu hộp; vòng lặp tiếp theo gán màu theo chiến thuật.

#### Cách đọc

Biểu đồ điểm giữ lại từng quan sát và cho thấy cỡ mẫu. Boxplot gọn hơn nhưng che bớt cấu trúc rời rạc của hạng 1–8. Không có geometry nào luôn tốt hơn; lựa chọn phụ thuộc câu hỏi.

**Đọc code vẽ bằng Matplotlib.** `plt.subplots` tạo `Figure` chứa một hoặc nhiều `Axes`; từng lệnh trên `ax`/`axes` vẽ vào hệ trục tương ứng. `axes[1].boxplot` tính hộp và râu cho từng nhóm quan sát. `axes[0].scatter` đặt các cặp giá trị vào biểu đồ phân tán; `s` điều chỉnh diện tích điểm và `alpha` điều chỉnh độ trong suốt. Thử đổi một thuộc tính hiển thị đang có, như màu, kích thước hoặc nhãn, rồi chạy lại ô; giữ dữ liệu để so sánh.

### Cell 11 — Hình học và facet

- **Loại:** Markdown
- **ID:** tft-012-geom-note

Cell tổng kết sự đánh đổi giữa điểm và boxplot, rồi giới thiệu facet: chia một biểu đồ thành nhiều ô theo một biến phân loại để so sánh cùng một mối liên hệ trong các nhóm.

### Cell 12 — Chia ô theo bậc xếp hạng

- **Loại:** Code
- **ID:** tft-013-facet-rank

#### Mục đích

Quan sát mối liên hệ máu–thứ hạng riêng trong từng bậc, thay vì gộp toàn bộ người chơi.

#### Tên biến

| Tên | Giải thích |
|---|---|
| **fig, axes** | Khung hình và bốn trục nằm trên một hàng. |
| **markers** | Từ điển gán hình điểm o, s, ^ cho ba chiến thuật. |
| **ax** | Trục ứng với một bậc. |
| **bac** | Bậc đang được vẽ. |
| **d** | Bảng con của một bậc. |
| **g** | Bảng con nhỏ hơn, của một chiến thuật trong bậc đó. |

#### Các hành động

Vòng lặp ngoài dùng **zip(axes, BAC)** để ghép từng trục với từng bậc. Vòng lặp trong chia tiếp theo chiến thuật. Màu và hình điểm cùng mã hóa chiến thuật, giúp biểu đồ vẫn phân biệt được khi in trắng đen hoặc với người khó nhận màu.

**sharex=True, sharey=True** bắt buộc bốn ô dùng cùng thang đo; nhờ vậy so sánh trực tiếp là hợp lệ. Chú giải chỉ được đặt ở ô cuối để tránh lặp. Tham số **label** được đặt rỗng ở các ô trước.

#### Cách đọc

Đọc từng ô như cùng một câu hỏi trong một điều kiện bậc cụ thể. Nếu hình dạng quan hệ khác nhau giữa các ô, kết luận gộp toàn bộ bậc có thể che mất tính không đồng nhất.

**Đọc code vẽ bằng Matplotlib.** `plt.subplots` tạo `Figure` chứa một hoặc nhiều `Axes`; từng lệnh trên `ax`/`axes` vẽ vào hệ trục tương ứng. `ax.scatter` đặt các cặp giá trị vào biểu đồ phân tán; `s` điều chỉnh diện tích điểm và `alpha` điều chỉnh độ trong suốt. Thử đổi một thuộc tính hiển thị đang có, như màu, kích thước hoặc nhãn, rồi chạy lại ô; giữ dữ liệu để so sánh.

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

#### Tên biến và hành động

| Tên | Giải thích |
|---|---|
| **d** | Mẫu 220 hàng để hình không quá dày. |
| **color="steelblue"** | Setting: mọi điểm cùng màu xanh. |
| **g** | Bảng con của một chiến thuật. |
| **MAU_CHIEN_THUAT[...]** | Mapping được thực hiện thủ công bằng cách vẽ từng nhóm với màu tương ứng. |

Biểu đồ trái gọi **scatter** một lần. Biểu đồ phải gọi scatter ba lần trong vòng lặp, mỗi lần cho một chiến thuật và gắn **label** để tạo legend.

#### Cách đọc

Biểu đồ trái chỉ cho thấy quan hệ máu–hạng. Biểu đồ phải cho phép hỏi thêm liệu ba chiến thuật có chiếm các vùng khác nhau hay không. Đổi màu cố định không làm xuất hiện thông tin mới; ánh xạ màu theo biến thì có.

**Đọc code vẽ bằng Matplotlib.** `plt.subplots` tạo `Figure` chứa một hoặc nhiều `Axes`; từng lệnh trên `ax`/`axes` vẽ vào hệ trục tương ứng. `axes[0].scatter` đặt các cặp giá trị vào biểu đồ phân tán; `s` điều chỉnh diện tích điểm và `alpha` điều chỉnh độ trong suốt. `axes[1].scatter` đặt các cặp giá trị vào biểu đồ phân tán; `s` điều chỉnh diện tích điểm và `alpha` điều chỉnh độ trong suốt. Thử đổi một thuộc tính hiển thị đang có, như màu, kích thước hoặc nhãn, rồi chạy lại ô; giữ dữ liệu để so sánh.

### Cell 15 — Chọn geometry theo ngữ nghĩa

- **Loại:** Markdown
- **ID:** tft-016-geometry-semantics

Q02 đặt câu hỏi về việc dùng đường nối. Một đường ngầm khẳng định các điểm có thứ tự và có quan hệ kế tiếp. Vì vậy không nên nối các người chơi độc lập chỉ vì họ đang nằm trong cùng một bảng.

### Cell 16 — Khi nào đường nối gây hiểu sai

- **Loại:** Code
- **ID:** tft-017-line-semantics

#### Mục đích

Đặt cạnh nhau một đường nối sai ngữ nghĩa và một đường nối đúng ngữ nghĩa.

#### Tên biến

| Tên | Giải thích |
|---|---|
| **d_sai** | 18 hàng được lấy ngẫu nhiên từ nhiều người chơi khác nhau. |
| **sort_values("mau_linh_thu")** | Sắp theo máu để đường trông có vẻ liên tục, dù các điểm không phải một chuỗi thực. |
| **lich_su** | Dữ liệu theo ngày của cùng người chơi P007. |

#### Các hành động

Biểu đồ trái dùng **plot** để nối các người chơi độc lập theo thứ tự máu. Đường này là một cấu trúc do người vẽ áp đặt, không phản ánh quá trình theo thời gian hay cùng một cá thể.

Biểu đồ phải nối các quan sát của P007 theo ngày. **marker="o"** vừa hiển thị điểm, vừa hiển thị đường giữa các ngày liên tiếp. **tick_params(rotation=45)** xoay nhãn ngày để dễ đọc.

#### Ý nghĩa

Một biểu đồ có thể chạy đúng cú pháp nhưng sai về ngữ nghĩa. Kiểm tra “điểm A có thực sự đứng trước điểm B không?” trước khi dùng line chart.

**Đọc code vẽ bằng Matplotlib.** `plt.subplots` tạo `Figure` chứa một hoặc nhiều `Axes`; từng lệnh trên `ax`/`axes` vẽ vào hệ trục tương ứng. `axes[0].plot` nối điểm theo thứ tự của các mảng truyền vào; sắp xếp tọa độ trước nếu cần đường theo thứ tự x. `axes[1].plot` nối điểm theo thứ tự của các mảng truyền vào; sắp xếp tọa độ trước nếu cần đường theo thứ tự x. Thử đổi một thuộc tính hiển thị đang có, như màu, kích thước hoặc nhãn, rồi chạy lại ô; giữ dữ liệu để so sánh.

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

#### Tên và hành động

**lich_su.head(10)** lấy 10 hàng đầu của bảng lịch sử. Các cột gồm ngày, người chơi, hạng và chiến thuật. **display** trình bày bảng ở định dạng HTML trong notebook.

#### Cách đọc

Mỗi ngày có một kết quả của cùng P007. Trước khi nối đường, cần xác nhận cột ngày có thứ tự thời gian và các hàng thực sự thuộc cùng một đối tượng.

### Cell 20 — Điểm rời rạc và đường xu hướng

- **Loại:** Code
- **ID:** tft-021-history-plots

#### Mục đích

So sánh hai mức độ xử lý cùng một chuỗi lịch sử: chỉ hiển thị quan sát và thêm đường giúp nhìn xu hướng.

#### Tên biến

| Tên | Giải thích |
|---|---|
| **lich_su["ngay"]** | Trục thời gian. |
| **lich_su["xep_hang"]** | Kết quả từng ngày. |
| **rolling(5).mean()** | Trung bình trượt của 5 trận gần nhất. |
| **min_periods=1** | Cho phép tính trung bình ngay ở đầu chuỗi dù chưa đủ 5 quan sát. |

#### Các hành động

Biểu đồ trái dùng **scatter** để giữ các trận độc lập. Biểu đồ phải dùng **plot** cho kết quả từng trận và thêm một đường rolling mean. Trung bình trượt tại ngày hiện tại lấy ngày đó cùng tối đa bốn ngày trước, giúp làm giảm dao động ngắn hạn.

**invert_yaxis** được dùng ở cả hai ô vì hạng nhỏ hơn là tốt hơn. **legend** phân biệt đường từng trận và đường trung bình.

#### Cách đọc

Đường trung bình 5 trận giúp thấy xu hướng nhưng không thay thế dữ liệu gốc. Một chuỗi ngắn có thể thay đổi hình dạng đáng kể khi đổi cửa sổ, nên cần trình bày cả điểm/đường thật.

**Đọc code vẽ bằng Matplotlib.** `plt.subplots` tạo `Figure` chứa một hoặc nhiều `Axes`; từng lệnh trên `ax`/`axes` vẽ vào hệ trục tương ứng. `axes[0].scatter` đặt các cặp giá trị vào biểu đồ phân tán; `s` điều chỉnh diện tích điểm và `alpha` điều chỉnh độ trong suốt. `axes[1].plot` nối điểm theo thứ tự của các mảng truyền vào; sắp xếp tọa độ trước nếu cần đường theo thứ tự x. Thử đổi một thuộc tính hiển thị đang có, như màu, kích thước hoặc nhãn, rồi chạy lại ô; giữ dữ liệu để so sánh.

### Cell 21 — Câu hỏi về làm mượt

- **Loại:** Markdown
- **ID:** tft-022-history-question

Q03 yêu cầu so sánh ưu, nhược điểm của điểm rời rạc và đường nối. Cell cũng chuẩn bị cho khái niệm cửa sổ trung bình trượt: cửa sổ lớn hơn tạo đường mượt hơn nhưng phản ứng chậm hơn với thay đổi mới.

### Cell 22 — Chú thích trận tốt nhất

- **Loại:** Code
- **ID:** tft-023-annotated-history

#### Mục đích

Minh họa cách thêm chú thích dựa trên dữ liệu thay vì ghi cứng một vị trí.

#### Tên biến

| Tên | Giải thích |
|---|---|
| **best_idx** | Nhãn index của hàng có xếp hạng nhỏ nhất. |
| **best_row** | Toàn bộ hàng dữ liệu của trận tốt nhất. |
| **idxmin()** | Trả lại index tại giá trị nhỏ nhất. |
| **annotate** | Hàm đặt văn bản và mũi tên trên biểu đồ. |

#### Các hành động

1. **idxmin** tìm trận có hạng thấp nhất về số, tức kết quả tốt nhất.
2. **loc[best_idx]** lấy đúng hàng đó.
3. **xy** là điểm mũi tên hướng tới; **xytext** là vị trí tương đối của hộp chữ.
4. **textcoords="offset points"** diễn giải xytext theo đơn vị điểm ảnh tương đối, giúp chú thích không đè lên dữ liệu.
5. **arrowprops** quy định kiểu mũi tên.

#### Cách đọc

Nếu có nhiều trận đồng hạng tốt nhất, **idxmin** chọn lần xuất hiện đầu tiên. Chú thích phải hỗ trợ thông điệp cụ thể, không nên dùng quá nhiều làm che dữ liệu.

**Đọc code vẽ bằng Matplotlib.** `plt.subplots` tạo `Figure` chứa một hoặc nhiều `Axes`; từng lệnh trên `ax`/`axes` vẽ vào hệ trục tương ứng. `ax.plot` nối điểm theo thứ tự của các mảng truyền vào; sắp xếp tọa độ trước nếu cần đường theo thứ tự x. `ax.annotate` gắn lời chú thích vào tọa độ được chỉ định. Thử đổi một thuộc tính hiển thị đang có, như màu, kích thước hoặc nhãn, rồi chạy lại ô; giữ dữ liệu để so sánh.

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

#### Tên biến

| Tên | Giải thích |
|---|---|
| **CUA_SO** | Số trận trong cửa sổ trung bình trượt; viết hoa vì được xem như tham số người học chủ động cấu hình. |
| **trung_binh_truot** | Series chứa giá trị trung bình của CUA_SO trận gần nhất. |

#### Các hành động

**rolling(CUA_SO, min_periods=1).mean()** tạo đường làm mượt. Nhãn f-string **f"Trung bình trượt {CUA_SO} trận"** tự chèn giá trị hiện tại của biến vào chú giải. Nhờ vậy, nếu đổi 5 thành 3 hoặc 10, cả tính toán và nhãn đều cập nhật.

#### Cách đọc và thử nghiệm

- **CUA_SO = 3:** đường bám dữ liệu sát hơn, nhạy hơn với dao động mới.
- **CUA_SO = 10:** đường mượt hơn nhưng che nhiều biến động ngắn hạn.

Không có một cửa sổ đúng tuyệt đối; lựa chọn phải gắn với câu hỏi và độ dài chuỗi.

**Đọc code vẽ bằng Matplotlib.** `plt.subplots` tạo `Figure` chứa một hoặc nhiều `Axes`; từng lệnh trên `ax`/`axes` vẽ vào hệ trục tương ứng. `ax.plot` nối điểm theo thứ tự của các mảng truyền vào; sắp xếp tọa độ trước nếu cần đường theo thứ tự x. Thử đổi một thuộc tính hiển thị đang có, như màu, kích thước hoặc nhãn, rồi chạy lại ô; giữ dữ liệu để so sánh.

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

#### Tên biến

| Tên | Giải thích |
|---|---|
| **gold** | DataFrame chỉ chứa các hàng có bac bằng Gold. |
| **g** | Bảng con của một chiến thuật trong dữ liệu Gold. |
| **query("bac == 'Gold'")** | Điều kiện chọn các hàng Gold. |

#### Các hành động

1. **query** tạo dữ liệu điều kiện. Dấu hai bằng trong biểu thức là phép so sánh, không phải gán.
2. Vòng lặp đi qua danh sách CHIEN_THUAT để giữ thứ tự và màu nhất quán.
3. Với mỗi nhóm, **gold[gold["chien_thuat"] == chien_thuat]** tạo bảng con.
4. **scatter** vẽ máu và hạng; **label** cho phép tạo chú giải.

#### Cách đọc

Mọi điểm đều thuộc bậc Gold. Vì đã điều kiện hóa theo bậc, sự khác biệt nhìn thấy giữa màu không còn do so sánh Gold với Silver/Platinum/Diamond, nhưng vẫn có thể chịu ảnh hưởng của nhiều biến khác.

**Đọc code vẽ bằng Matplotlib.** `plt.subplots` tạo `Figure` chứa một hoặc nhiều `Axes`; từng lệnh trên `ax`/`axes` vẽ vào hệ trục tương ứng. `ax.scatter` đặt các cặp giá trị vào biểu đồ phân tán; `s` điều chỉnh diện tích điểm và `alpha` điều chỉnh độ trong suốt. Thử đổi một thuộc tính hiển thị đang có, như màu, kích thước hoặc nhãn, rồi chạy lại ô; giữ dữ liệu để so sánh.

### Cell 29 — Câu hỏi về thứ tự thao tác

- **Loại:** Markdown
- **ID:** tft-030-python-question

Cell yêu cầu người học nhận ra việc lọc diễn ra **trước** khi vẽ. Nếu vẽ toàn bộ rồi chỉ đổi tiêu đề thành Gold, hình không tự động trở thành dữ liệu Gold. Tên biến và nhãn không thay thế thao tác dữ liệu.

### Cell 30 — Đổi một thành phần: từ scatter sang boxplot

- **Loại:** Code
- **ID:** tft-031-change-one-component

#### Mục đích

Giữ dữ liệu Gold nhưng đổi câu hỏi: từ liên hệ hai biến số sang so sánh phân phối hạng theo lõi bổ trợ.

#### Tên và hành động

**gold.boxplot(column="xep_hang", by="loi_bo_tro")** dùng DataFrame đã lọc ở Cell 28. **column** là biến số cần so sánh; **by** là biến phân nhóm. **grid=False** tắt lưới nội bộ của boxplot; **plt.suptitle("")** xóa tiêu đề phụ tự động mà pandas tạo.

#### Cách đọc

Mỗi hộp tóm tắt phân phối hạng của một nhóm lõi trong bậc Gold. Boxplot không cho biết nguyên nhân lõi tạo ra thứ hạng; đây chỉ là so sánh mô tả.

**Đọc code vẽ bằng Matplotlib.** `plt.subplots` tạo `Figure` chứa một hoặc nhiều `Axes`; từng lệnh trên `ax`/`axes` vẽ vào hệ trục tương ứng. `ax.boxplot` tính hộp và râu cho từng nhóm quan sát. Thử đổi một thuộc tính hiển thị đang có, như màu, kích thước hoặc nhãn, rồi chạy lại ô; giữ dữ liệu để so sánh.

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

#### Tên biến

| Tên | Giải thích |
|---|---|
| **scout_day_du** | DataFrame chỉ gồm hàng có đủ so_lan_scout và xep_hang. |
| **dropna(subset=[...])** | Loại hàng thiếu ở đúng các cột được chỉ định. |
| **len(...)** | Đếm số hàng. |

#### Các hành động

1. In số hàng ban đầu bằng **len(tran_tft)**.
2. **dropna** tạo bảng mới; không thay đổi tran_tft.
3. In số hàng hoàn chỉnh và hiệu số để người đọc biết cỡ mẫu thực tế.
4. Vẽ scatter từ scout_day_du, không phải từ bảng gốc.

#### Đầu ra

Dữ liệu có 960 hàng, 922 hàng đầy đủ cho hai biến này và 38 hàng bị thiếu scouting. Con số có thể kiểm tra trực tiếp thay vì để thư viện âm thầm bỏ qua.

#### Lưu ý thống kê

Loại hàng chỉ an toàn khi cơ chế thiếu không làm mẫu còn lại bị lệch nghiêm trọng. Trong dữ liệu thật, cần kiểm tra thiếu có tập trung ở bậc, chiến thuật hoặc loại trận nào không.

**Đọc code vẽ bằng Matplotlib.** `plt.subplots` tạo `Figure` chứa một hoặc nhiều `Axes`; từng lệnh trên `ax`/`axes` vẽ vào hệ trục tương ứng. `ax.scatter` đặt các cặp giá trị vào biểu đồ phân tán; `s` điều chỉnh diện tích điểm và `alpha` điều chỉnh độ trong suốt. Thử đổi một thuộc tính hiển thị đang có, như màu, kích thước hoặc nhãn, rồi chạy lại ô; giữ dữ liệu để so sánh.

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

#### Tên và hành động

| Tên | Giải thích |
|---|---|
| **diamond** | DataFrame gồm các lượt người chơi-trận thuộc bậc Diamond. |
| **query("bac == 'Diamond'")** | Lọc hàng theo điều kiện bậc. |
| **[[...]]** | Chọn danh sách cột để hiển thị. |
| **head()** | Lấy 5 hàng đầu sau lọc. |

Cell in số hàng bằng **len(diamond)** rồi hiển thị một bản xem trước. Trong bộ dữ liệu này, Diamond có 120 hàng.

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

#### Tên biến

| Tên | Giải thích |
|---|---|
| **fast8_mau_cao** | Hàng vừa dùng Fast 8 vừa có máu ít nhất 50. |
| **reroll_hoac_fast8** | Hàng dùng Reroll hoặc Fast 8. |
| **and** | Cả hai điều kiện phải đúng. |
| **or** | Ít nhất một điều kiện đúng. |

#### Các hành động và đầu ra

Hai lệnh **query** dùng từ khóa and/or trong chuỗi biểu thức. Tập giao Fast 8 và máu ≥ 50 có 126 hàng; tập hợp Reroll hoặc Fast 8 có 573 hàng.

Tập and thường nhỏ hơn từng điều kiện riêng. Tập or thường lớn hơn vì nhận hàng từ cả hai nhóm. Với hai nhóm chiến thuật loại trừ nhau, số hàng or bằng tổng số hàng hai nhóm.

### Cell 40 — Logic lọc và lựa chọn ngưỡng

- **Loại:** Markdown
- **ID:** tft-041-filter-logic

Cell tổng kết cú pháp query, phép **isin** và toán tử so sánh. Cảnh báo quan trọng là không nên thử rất nhiều ngưỡng rồi chỉ báo cáo ngưỡng cho kết quả đẹp nhất; hành vi đó làm tăng nguy cơ “khám phá” một mẫu ngẫu nhiên. Q04 yêu cầu người học dịch một câu điều kiện tự nhiên thành mã.

### Cell 41 — Tạo biến Boolean

- **Loại:** Code
- **ID:** tft-042-boolean-vars

#### Mục đích

Biến một điều kiện thành cột True/False để có thể hiển thị, nhóm hoặc tính tỷ lệ.

#### Tên biến và hành động

| Tên | Giải thích |
|---|---|
| **mau_tu_50** | True nếu mau_linh_thu lớn hơn hoặc bằng 50. |
| **top4** | True nếu xep_hang nhỏ hơn hoặc bằng 4. |
| **assign(...)** | Trả về một DataFrame có thêm hoặc thay cột. |

**tran_tft = tran_tft.assign(...)** gán bảng mới trở lại cùng tên tran_tft. Biểu thức so sánh trên một Series được áp dụng theo từng hàng và tạo ra một Series Boolean tương ứng.

Cell hiển thị máu, biến mau_tu_50, hạng và top4 để người học kiểm tra logic. Ví dụ máu 50 phải được xếp vào nhóm True vì toán tử là **>=**, không phải **>**.

### Cell 42 — Trung bình của Boolean là tỷ lệ

- **Loại:** Code
- **ID:** tft-043-boolean-mean

#### Mục đích

Cho thấy cách tính tỷ lệ trực tiếp từ một cột True/False.

#### Tên và hành động

- **tran_tft["mau_tu_50"].mean()** đổi True thành 1, False thành 0 rồi lấy trung bình.
- **tran_tft["top4"].mean()** thực hiện tương tự cho kết quả top 4.
- **:.1%** là định dạng f-string hiển thị số thập phân dưới dạng phần trăm với một chữ số sau dấu phẩy.

Đầu ra cho thấy khoảng 57.0% hàng có máu ít nhất 50 và đúng 50.0% hàng là top 4. Tỷ lệ top 4 toàn bảng luôn là một nửa do cấu trúc mỗi lobby.

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

#### Tên và hành động

| Tên | Giải thích |
|---|---|
| **sat_thuong** | Tổng sát thương trên thang gốc. |
| **sat_thuong_log10** | Logarit cơ số 10 của sát thương, đã tạo ở Cell 02. |
| **bins=24** | Chia miền giá trị thành 24 khoảng trong histogram. |

Biểu đồ trái dùng thang gốc; biểu đồ phải dùng log10. Trên thang log, tăng 1 đơn vị nghĩa là sát thương gấp 10 lần. Ví dụ log10 bằng 4 tương ứng khoảng 10.000 sát thương.

#### Lưu ý

Logarit chỉ xác định trực tiếp cho giá trị dương. Cell tạo dữ liệu đã bảo đảm sát thương dương bằng cách cắt cận dưới. Với dữ liệu có 0, cần một quyết định rõ ràng như dùng log1p hoặc xử lý 0 theo ý nghĩa thực tế.

**Đọc code vẽ bằng Matplotlib.** `plt.subplots` tạo `Figure` chứa một hoặc nhiều `Axes`; từng lệnh trên `ax`/`axes` vẽ vào hệ trục tương ứng. `axes[0].hist` chia quan sát theo `bins`; đọc `density` để phân biệt số đếm và mật độ. `axes[1].hist` chia quan sát theo `bins`; đọc `density` để phân biệt số đếm và mật độ. Thử đổi một thuộc tính hiển thị đang có, như màu, kích thước hoặc nhãn, rồi chạy lại ô; giữ dữ liệu để so sánh.

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

#### Tên biến

| Tên | Giải thích |
|---|---|
| **tom_tat_nhanh** | Bảng kết quả sau toàn bộ pipeline cho lobby nhanh. |
| **n** | Số lượt người chơi-trận trong nhóm chiến thuật. |
| **xep_hang_tb** | Xếp hạng trung bình. Giá trị nhỏ hơn là tốt hơn. |
| **ty_le_top4** | Trung bình của cột top4, tức tỷ lệ top 4. |
| **ty_le_mau_cao** | Trung bình của mau_tu_50 trong nhóm. |

#### Từng hành động

1. **query("nhip_lobby == 'Nhanh'")** chỉ giữ các hàng thuộc lobby nhanh. Từ đây, mọi kết quả đều có điều kiện “trong lobby nhanh”.
2. **assign(mau_tu_50=lambda d: ...)** tạo cột Boolean trên bảng đang đi qua pipeline. Tên **d** trong lambda đại diện cho DataFrame ở đúng bước đó.
3. **groupby("chien_thuat", observed=True)** chia dữ liệu đã lọc thành ba nhóm chiến thuật.
4. **agg(...)** tạo các cột tóm tắt có tên rõ ràng. Cú pháp cặp **("cột", "hàm")** chỉ cột nguồn và phép tính.
5. **reset_index()** biến chien_thuat từ nhãn index nhóm trở lại thành một cột thường.
6. **sort_values("ty_le_top4", ascending=False)** xếp tỷ lệ top 4 từ cao xuống thấp.
7. **round(3)** làm tròn bảng hiển thị đến ba chữ số; dữ liệu gốc không bị làm tròn.

#### Cách đọc đầu ra

Trong dữ liệu mô phỏng, Fast 8 có tỷ lệ top 4 cao nhất trong lobby nhanh, tiếp theo là Tempo rồi Reroll. Tuy nhiên, đây là so sánh mô tả trong một điều kiện; chưa phải bằng chứng rằng chọn Fast 8 gây ra top 4.

### Cell 49 — Câu hỏi về đơn vị và mẫu số

- **Loại:** Markdown
- **ID:** tft-050-pipeline-question

Cell yêu cầu xác định một hàng trong bảng kết quả đại diện cho gì: một **nhóm chiến thuật trong các lobby nhanh**, không còn là một người chơi-trận. Mẫu số của ty_le_top4 là n của từng dòng.

### Cell 50 — Lọc và nhóm trả lời hai câu hỏi khác nhau

- **Loại:** Code
- **ID:** tft-051-filter-vs-group

#### Mục đích

Đối chiếu “chỉ xem Fast 8” với “giữ tất cả và so sánh theo chiến thuật”.

#### Tên biến

| Tên | Giải thích |
|---|---|
| **fast8_only** | Bảng chỉ gồm các hàng có chiến thuật Fast 8. |
| **all_by_strategy** | Bảng tóm tắt ba chiến thuật trên toàn dữ liệu. |

#### Các hành động

**fast8_only.agg(...)** tính một bản tóm tắt duy nhất cho tập Fast 8: số hàng, hạng trung bình và tỷ lệ top 4. Vì DataFrame.agg áp dụng các hàm theo cột, cách hiển thị có thể có một số ô trống; điều quan trọng là đọc đúng giao giữa đại lượng và cột nguồn.

**groupby(...).agg(...)** tạo một hàng cho mỗi chiến thuật. Đây là cấu trúc phù hợp hơn khi mục tiêu là so sánh nhóm.

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

#### Tên biến

| Tên | Giải thích |
|---|---|
| **dung** | Tỷ lệ top 4 của từng chiến thuật tính trên tất cả hàng của chiến thuật. |
| **sai** | Tỷ lệ top 4 sau khi đã lọc chỉ các hàng top4. |

#### Các hành động

- **dung:** nhóm toàn bộ dữ liệu rồi lấy mean của top4. Mẫu số gồm cả top 4 và không top 4.
- **sai:** query top4 trước, nên mọi giá trị còn lại đều là True. Trung bình của toàn 1 luôn bằng 1 hay 100%.

#### Bài học

Tên biến **sai** không nói Python đã báo lỗi; mã vẫn chạy chính xác. Sai ở đây là câu hỏi phân tích và mẫu số. Đây là lý do phải mô tả tập dữ liệu sau mỗi bước lọc.

### Cell 53 — Mở đầu tóm tắt theo nhóm

- **Loại:** Markdown
- **ID:** tft-054-group-summary-heading

Cell chuẩn bị mở rộng từ một tỷ lệ sang nhiều đại lượng cho mỗi chiến thuật: cỡ mẫu, hạng trung bình, tỷ lệ top 4, tỷ lệ thắng và trung bình tài nguyên.

### Cell 54 — Bảng tóm tắt nhiều đại lượng

- **Loại:** Code
- **ID:** tft-055-group-table

#### Mục đích

Tạo một bảng mô tả đầy đủ hơn cho ba chiến thuật trên toàn bộ dữ liệu.

#### Tên biến

| Tên | Giải thích |
|---|---|
| **tom_tat_chien_thuat** | Bảng một hàng cho mỗi chiến thuật. |
| **n** | Số lượt người chơi-trận. |
| **xep_hang_tb** | Hạng trung bình. |
| **ty_le_top4** | Tỷ lệ hạng 1–4. |
| **ty_le_thang** | Tỷ lệ hạng 1, được tính bằng lambda. |
| **mau_tb** | Máu trung bình. |
| **vang_tb** | Vàng trung bình. |

#### Các hành động

**lambda s: (s == 1).mean()** nhận Series hạng của một nhóm, đổi điều kiện hạng bằng 1 thành Boolean rồi tính trung bình. Đây là cách tạo tỷ lệ chiến thắng mà không cần tạo cột riêng trước.

**reset_index** đưa nhãn chiến thuật vào cột; **round(3)** chỉ phục vụ hiển thị.

#### Cách đọc

Không nên chỉ nhìn một cột. Ví dụ một chiến thuật có tỷ lệ top 4 tốt hơn có thể đồng thời có phân phối bậc hoặc nhịp lobby khác. **n** luôn cần được báo cáo cùng tỷ lệ để đánh giá độ ổn định.

### Cell 55 — Vẽ tỷ lệ top 4 từ bảng đã tóm tắt

- **Loại:** Code
- **ID:** tft-056-group-plot

#### Mục đích

Chuyển cột ty_le_top4 của bảng tóm tắt thành biểu đồ cột phần trăm.

#### Tên và hành động

**set_index("chien_thuat")["ty_le_top4"]** đặt nhãn chiến thuật trên trục x và chọn đúng Series cần vẽ. **plot(kind="bar")** vẽ cột. Danh sách **color=[...]** lấy màu theo thứ tự CHIEN_THUAT.

**ax.yaxis.set_major_formatter(PercentFormatter(1.0))** cho biết dữ liệu tỷ lệ đang nằm trong thang 0–1; formatter đổi 0.5 thành 50%. **set_ylim(0, 0.7)** đặt gốc trục ở 0 và chừa khoảng phía trên.

#### Cách đọc

Chiều cao cột là tỷ lệ, không phải số lượng. Biểu đồ dựa trên bảng đã tóm tắt nên mỗi cột đại diện một nhóm, không phải một quan sát cá nhân.

**Đọc code vẽ bằng Matplotlib.** `plt.subplots` tạo `Figure` chứa một hoặc nhiều `Axes`; từng lệnh trên `ax`/`axes` vẽ vào hệ trục tương ứng. `ax.bar` dùng vị trí và độ dài cột đã tính để vẽ biểu đồ cột. `ax.axhline` thêm đường ngang làm giá trị đối chiếu. Thử đổi một thuộc tính hiển thị đang có, như màu, kích thước hoặc nhãn, rồi chạy lại ô; giữ dữ liệu để so sánh.

### Cell 56 — Bài tập nhóm theo hai biến

- **Loại:** Markdown
- **ID:** tft-057-group-exercise

Cell đặt yêu cầu phân tầng kết quả theo cả nhịp lobby và chiến thuật. Mục tiêu là kiểm tra liệu thứ hạng chung giữa chiến thuật có còn giữ nguyên trong từng loại lobby hay không.

### Cell 57 — Tóm tắt theo nhịp lobby và chiến thuật

- **Loại:** Code
- **ID:** tft-058-group-two-vars

#### Mục đích

Tạo sáu nhóm từ tích của 2 mức nhịp lobby và 3 chiến thuật.

#### Tên biến và hành động

| Tên | Giải thích |
|---|---|
| **tom_tat_nhip** | Bảng kết quả theo hai biến phân nhóm. |
| **groupby(["nhip_lobby", "chien_thuat"])** | Chia dữ liệu theo mọi tổ hợp thực sự xuất hiện. |
| **n** | Cỡ mẫu của từng tổ hợp. |
| **ty_le_top4** | Tỷ lệ top 4 trong đúng tổ hợp đó. |

**sort_values(["nhip_lobby", "chien_thuat"])** sắp bảng để các hàng cùng nhịp nằm gần nhau. Vì chien_thuat là categorical có thứ tự, thứ tự chiến thuật được giữ như đã khai báo.

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

#### Tên biến

| Tên | Giải thích |
|---|---|
| **simpson** | DataFrame bốn hàng chứa số top 4 và tổng số trận theo nhịp × chiến thuật. |
| **so_top4** | Số lượt đạt top 4. |
| **so_tran** | Tổng lượt người chơi-trận, là mẫu số. |
| **ty_le_top4** | so_top4 chia so_tran. |
| **trong_nhom** | Bảng pivot tỷ lệ trong từng nhịp. |
| **gop** | Tỷ lệ sau khi cộng tử số và mẫu số qua hai nhịp. |

#### Các hành động

1. **pd.DataFrame({...})** tạo dữ liệu đếm, không tạo từng quan sát riêng.
2. Tỷ lệ được tính trực tiếp bằng phép chia hai cột.
3. **pivot** chuyển dữ liệu dài thành bảng có hàng là nhịp và cột là chiến thuật.
4. **groupby("chien_thuat")[[...]].sum()** cộng số top 4 và số trận trước khi chia. Đây là cách gộp tỷ lệ đúng, có trọng số theo mẫu số.

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

#### Tên biến

| Tên | Giải thích |
|---|---|
| **x** | Vị trí số của hai nhịp trên trục x. |
| **width** | Độ rộng mỗi cột trong một cặp. |
| **trong_nhom.loc[..., ...]** | Lấy tỷ lệ của một chiến thuật theo từng nhịp. |

#### Các hành động

Biểu đồ trái dịch cột Reroll sang trái **x - width/2** và Fast 8 sang phải **x + width/2**, tạo các cặp có thể so sánh. Biểu đồ phải dùng Series **gop["ty_le_top4"]** để vẽ kết quả gộp.

Cả hai trục dùng **PercentFormatter(1.0)**. Trục trái giới hạn 0–1 để hiển thị đầy đủ xác suất; trục phải dùng cùng ngữ nghĩa phần trăm.

#### Bài học

Biểu đồ không tự giải quyết nhiễu. Điều quan trọng là chọn đúng mức tổng hợp và hiển thị biến phân tầng có liên quan.

**Đọc code vẽ bằng Matplotlib.** `plt.subplots` tạo `Figure` chứa một hoặc nhiều `Axes`; từng lệnh trên `ax`/`axes` vẽ vào hệ trục tương ứng. `axes[1].bar` dùng vị trí và độ dài cột đã tính để vẽ biểu đồ cột. `theo_nhip.plot(kind='bar')` dùng bảng pandas để vẽ qua Matplotlib trên hệ trục truyền bằng `ax`; kiểm tra `stacked` để phân biệt cột chồng và cột nhóm. Thử đổi một thuộc tính hiển thị đang có, như màu, kích thước hoặc nhãn, rồi chạy lại ô; giữ dữ liệu để so sánh.

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

#### Tên biến

| Tên | Giải thích |
|---|---|
| **dem** | Bảng chéo số lượng tuyệt đối. |
| **ty_le** | Bảng chéo tỷ lệ trong từng hàng. |
| **pd.crosstab** | Hàm lập bảng chéo giữa hai biến phân loại. |
| **margins=True** | Thêm hàng/cột tổng có nhãn Tổng. |
| **normalize="index"** | Chia mỗi ô cho tổng của chính hàng đó. |

#### Các hành động

**dem** đếm số quan sát trong từng tổ hợp lõi × top4. **ty_le** chuẩn hóa theo hàng, nên hai cột False và True của mỗi loại lõi cộng thành 1. Sau đó chỉ cột **True** được chọn để hiển thị tỷ lệ top 4.

#### Cách đọc

Bảng đếm trả lời “có bao nhiêu lượt top 4?”. Bảng tỷ lệ trả lời “trong các lượt dùng lõi này, bao nhiêu phần đạt top 4?”. Một nhóm lớn có thể có nhiều ca top 4 nhưng tỷ lệ thấp hơn nhóm nhỏ.

**Đọc code vẽ bằng Matplotlib.** `plt.subplots` tạo `Figure` chứa một hoặc nhiều `Axes`; từng lệnh trên `ax`/`axes` vẽ vào hệ trục tương ứng. `bang_loi.rename(columns={False: 'Ngoài top 4', True: 'Top 4'}).plot(kind='bar')` dùng bảng pandas để vẽ qua Matplotlib trên hệ trục truyền bằng `ax`; kiểm tra `stacked` để phân biệt cột chồng và cột nhóm. `ti_le_loi.rename(columns={False: 'Ngoài top 4', True: 'Top 4'}).plot(kind='bar')` dùng bảng pandas để vẽ qua Matplotlib trên hệ trục truyền bằng `ax`; kiểm tra `stacked` để phân biệt cột chồng và cột nhóm. Thử đổi một thuộc tính hiển thị đang có, như màu, kích thước hoặc nhãn, rồi chạy lại ô; giữ dữ liệu để so sánh.

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

#### Tên biến

| Tên | Giải thích |
|---|---|
| **rate** | Series tỷ lệ top 4, lấy từ tom_tat_chien_thuat và đánh index bằng chiến thuật. |
| **axes[0]** | Biểu đồ dùng trục đầy đủ từ 0 đến 1. |
| **axes[1]** | Biểu đồ dùng trục hẹp từ 0.4 đến 0.6. |

#### Các hành động

Cả hai ô vẽ cùng dữ liệu, cùng màu, cùng loại cột. Chỉ **set_ylim** khác nhau. Vòng lặp cuối gắn định dạng phần trăm cho cả hai trục.

#### Cách đọc

Biểu đồ phải phóng đại chênh lệch vì bỏ phần 0–40% của trục. Với biểu đồ cột, chiều dài cột thường được so từ gốc 0, nên cắt trục đặc biệt dễ gây ấn tượng sai. Nếu cần phóng to khác biệt, nên báo rõ và cân nhắc dùng điểm với khoảng tin cậy.

**Đọc code vẽ bằng Matplotlib.** `plt.subplots` tạo `Figure` chứa một hoặc nhiều `Axes`; từng lệnh trên `ax`/`axes` vẽ vào hệ trục tương ứng. `ax.bar` dùng vị trí và độ dài cột đã tính để vẽ biểu đồ cột. Thử đổi một thuộc tính hiển thị đang có, như màu, kích thước hoặc nhãn, rồi chạy lại ô; giữ dữ liệu để so sánh.

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

#### Tên biến

| Tên | Giải thích |
|---|---|
| **nhom_mau** | Nhãn văn bản tạo từ điều kiện mau_tu_50. |
| **pooled** | Bảng tóm tắt gộp theo nhóm máu. |
| **np.where** | Chọn một trong hai nhãn cho mỗi hàng dựa trên điều kiện Boolean. |
| **n** | Số lượt người chơi-trận trong nhóm. |
| **ty_le_top4** | Tỷ lệ top 4 của nhóm. |
| **xep_hang_tb** | Hạng trung bình của nhóm. |

#### Các hành động

**assign(nhom_mau=np.where(...))** thêm nhãn dễ đọc mà vẫn giữ cột Boolean gốc. Sau đó groupby và agg tính ba đại lượng cho hai nhóm.

#### Cách đọc

Trong dữ liệu mô phỏng, nhóm máu ≥ 50 có tỷ lệ top 4 cao hơn và hạng trung bình tốt hơn. Đây là một mối liên hệ mô tả mạnh, nhưng máu được đo trong quá trình trận đấu và có thể vừa phản ánh vừa chịu ảnh hưởng của tình trạng thắng thế.

### Cell 69 — Điều kiện hóa thêm theo bậc

- **Loại:** Code
- **ID:** tft-070-challenge-conditioned

#### Mục đích

Kiểm tra mối liên hệ máu–top 4 riêng trong Silver, Gold, Platinum và Diamond.

#### Tên biến và hành động

| Tên | Giải thích |
|---|---|
| **conditioned** | Bảng có một hàng cho mỗi tổ hợp bậc × nhóm máu. |
| **groupby(["bac", "nhom_mau"])** | Phân tầng đồng thời theo hai biến. |
| **observed=True** | Không tạo các tổ hợp phân loại không xuất hiện. |

**agg** tính n, tỷ lệ top 4 và hạng trung bình trong mỗi tổ hợp. **reset_index** đưa cả hai biến phân nhóm về cột thường.

#### Cách đọc

So hai nhóm máu trong cùng một bậc. Nếu mối liên hệ vẫn cùng chiều ở cả bốn bậc, nó không chỉ là hệ quả của việc các bậc có phân bố máu khác nhau. Dù vậy, vẫn chưa thể gọi là tác động nhân quả vì còn nhiều biến chưa điều kiện hóa và thứ tự thời gian cần xem xét.

### Cell 70 — Vẽ tỷ lệ có điều kiện theo bậc

- **Loại:** Code
- **ID:** tft-071-challenge-plot

#### Mục đích

Biến bảng conditioned thành biểu đồ cột ghép để so sánh hai nhóm máu trong từng bậc.

#### Tên biến

| Tên | Giải thích |
|---|---|
| **cond_plot** | Bảng pivot có hàng là bậc, cột là nhóm máu và ô là tỷ lệ top 4. |
| **pivot** | Đổi dữ liệu từ dạng dài sang dạng rộng để vẽ cột ghép. |

#### Các hành động

**pivot(index="bac", columns="nhom_mau", values="ty_le_top4")** tạo hai Series tỷ lệ đặt cạnh nhau cho mỗi bậc. **reindex(BAC)** giữ thứ tự bậc đã quy ước. **plot(kind="bar")** vẽ cột ghép; trục y được hiển thị dạng phần trăm và bắt đầu ở 0.

#### Cách đọc

So sánh chiều cao hai cột trong mỗi cụm bậc. Không chỉ nhìn các cột cùng màu qua các bậc, vì câu hỏi chính là chênh lệch nhóm máu trong cùng điều kiện bậc.

**Đọc code vẽ bằng Matplotlib.** `plt.subplots` tạo `Figure` chứa một hoặc nhiều `Axes`; từng lệnh trên `ax`/`axes` vẽ vào hệ trục tương ứng. `ax.bar` dùng vị trí và độ dài cột đã tính để vẽ biểu đồ cột. Thử đổi một thuộc tính hiển thị đang có, như màu, kích thước hoặc nhãn, rồi chạy lại ô; giữ dữ liệu để so sánh.

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

#### Tên biến

| Tên | Giải thích |
|---|---|
| **case** | Bảng dùng cho case study, đã loại hàng thiếu scouting. |
| **nhom_scout** | Nhóm số lần scout: 0–1, 2–3 hoặc ≥4. |
| **bins** | Các mốc chia khoảng: từ âm vô cùng đến 1, 3 và dương vô cùng. |
| **labels** | Nhãn tương ứng cho ba khoảng. |
| **include_lowest=True** | Bảo đảm giá trị ở cận thấp nhất được đưa vào khoảng đầu. |
| **right=True** | Mỗi khoảng đóng ở bên phải; ví dụ khoảng đầu nhận giá trị ≤1. |
| **case_summary** | Bảng n, tỷ lệ top 4 và hạng trung bình theo nhóm scout. |

#### Các hành động

1. **dropna(subset=["so_lan_scout"])** chỉ loại hàng không quan sát được scouting.
2. **copy()** tạo bản sao độc lập, tránh cảnh báo và tránh sửa một lát cắt của DataFrame gốc.
3. **pd.cut** phân loại biến số theo các ngưỡng đã định trước.
4. **groupby("nhom_scout", observed=True)** chia ba nhóm.
5. **agg** tính cỡ mẫu và kết quả.

#### Cách đọc

Trong dữ liệu mô phỏng, nhóm scout ≥4 có tỷ lệ top 4 cao nhất. Tuy nhiên, việc chia 0–1, 2–3, ≥4 là một quyết định phân tích; đổi ngưỡng có thể đổi kết quả. Cần báo rõ các ngưỡng và không thử nhiều cách rồi chỉ chọn cách đẹp nhất.

### Cell 74 — Vẽ kết quả case study

- **Loại:** Code
- **ID:** tft-075-case-plot

#### Mục đích

Trình bày tỷ lệ top 4 theo ba nhóm scouting và ghi trực tiếp cỡ mẫu lên cột.

#### Tên biến

| Tên | Giải thích |
|---|---|
| **bars** | Tập hợp ba hình chữ nhật do ax.bar trả lại. |
| **bar** | Một cột riêng lẻ trong vòng lặp. |
| **n** | Cỡ mẫu ứng với cột đang xét. |
| **get_x(), get_width(), get_height()** | Lấy vị trí, độ rộng và chiều cao của cột để đặt nhãn. |

#### Các hành động

**ax.bar** nhận nhãn nhóm ở trục x và tỷ lệ ở trục y. Vòng lặp **zip(bars, case_summary["n"])** ghép mỗi cột với đúng cỡ mẫu. **ax.text** đặt chuỗi “n=...” hơi cao hơn đỉnh cột.

**ha="center"** căn ngang giữa; **va="bottom"** đặt đáy văn bản tại vị trí y. Trục y dùng định dạng phần trăm và bắt đầu từ 0.

#### Cách đọc

Đọc đồng thời chiều cao cột và n. Một tỷ lệ từ nhóm rất nhỏ thường bất định hơn tỷ lệ từ nhóm lớn, dù notebook chưa vẽ khoảng tin cậy.

**Đọc code vẽ bằng Matplotlib.** `plt.subplots` tạo `Figure` chứa một hoặc nhiều `Axes`; từng lệnh trên `ax`/`axes` vẽ vào hệ trục tương ứng. `ax.bar` dùng vị trí và độ dài cột đã tính để vẽ biểu đồ cột. `ax.text` đặt chữ tại tọa độ trong hệ trục. Thử đổi một thuộc tính hiển thị đang có, như màu, kích thước hoặc nhãn, rồi chạy lại ô; giữ dữ liệu để so sánh.

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

## Bảng tra nhanh các hành động pandas/matplotlib trong notebook

| Hành động | Cách hiểu ngắn gọn | Cell tiêu biểu |
|---|---|---|
| **head** | Xem một số hàng đầu để kiểm tra cấu trúc. | 02, 19, 37 |
| **query** | Giữ các hàng thỏa điều kiện. | 28, 37, 39, 48, 50, 52 |
| **dropna** | Loại hàng thiếu ở các cột được chỉ định. | 33, 73 |
| **assign** | Tạo cột mới trong một pipeline. | 41, 48, 68 |
| **groupby** | Chia dữ liệu thành nhóm để tính riêng. | 48, 50, 54, 57, 69, 73 |
| **agg** | Tạo một hay nhiều thống kê tóm tắt. | 48, 50, 54, 57, 68, 69, 73 |
| **reset_index** | Đưa biến nhóm từ index trở lại cột. | 48, 54, 57, 69, 73 |
| **pivot** | Chuyển bảng dài thành bảng rộng. | 59, 70 |
| **crosstab** | Lập bảng chéo đếm hoặc tỷ lệ. | 62 |
| **rolling** | Tính thống kê trên cửa sổ các quan sát liên tiếp. | 20, 25 |
| **scatter** | Vẽ từng quan sát của hai biến số. | 06, 08, 12, 14, 28, 33 |
| **plot** | Vẽ đường khi các điểm có thứ tự có nghĩa. | 16, 20, 22, 25 |
| **boxplot** | So sánh phân phối một biến số giữa các nhóm. | 06, 10, 30 |
| **bar** | So sánh số lượng hoặc tỷ lệ đã tóm tắt. | 06, 55, 60, 65, 70, 74 |
| **invert_yaxis** | Đưa hạng 1 lên phía trên. | Nhiều cell có trục xếp hạng |
| **PercentFormatter** | Hiển thị tỷ lệ 0–1 thành phần trăm. | 55, 60, 65, 70, 74 |

## Cách tự kiểm tra sau khi học

Trước khi chấp nhận một biểu đồ hoặc bảng kết quả, hãy trả lời được sáu câu hỏi:

1. Một hàng dữ liệu đại diện cho đối tượng nào?
2. Những hàng nào đã bị lọc hoặc bị loại do thiếu dữ liệu?
3. Mỗi biến và mỗi tên viết tắt có ý nghĩa gì?
4. Nếu có tỷ lệ, tử số và mẫu số là gì?
5. Biểu đồ đang thể hiện quan sát thô, phân phối hay số liệu đã tóm tắt?
6. Kết luận là mô tả mối liên hệ hay đang vô tình khẳng định nhân quả?

Nếu chưa trả lời được một trong sáu câu, nên quay lại cell tạo dữ liệu hoặc pipeline trước khi diễn giải kết quả.
