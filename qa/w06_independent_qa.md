> Báo cáo đối chiếu nội dung độc lập. Các finding của bản đầu (nếu có) đã được xử lý; kết quả chạy và kiểm tra bản phát hành cuối ngày 07/10/2026 nằm trong `W05_W07_VALIDATION.json` và `../REVIEW_W05_W07.md`.

# QA độc lập W6 — 2026-10-06

Snapshot: `06_distributions_random_variables/notebook.ipynb`, 110 cell, 30 code. Đã đọc toàn bộ Markdown/code (data URI được lược base64 khi in source), toàn bộ 80 trang week06.txt và mục Buổi 6 của đề cương, §3.4–3.5/LLO6.1. Không sửa nguồn, không thay Git. Root thực hiện execution và visual QA.

Không tìm thấy thiếu nội dung hoặc sai thống kê có ảnh hưởng. Một điểm làm tròn nhỏ tại đáp án Ví dụ 13: viết `0,3413 + 0,5404 = 0,8816` gây lệch số học của các số đã làm tròn (tổng là 0,8817). Kết quả đúng từ giá trị chưa làm tròn là 0,88164014. Có thể bỏ hai số trung gian và giữ `P(X=11)+P(X=12)≈0,8816`.

## Coverage nguồn

Set tên Ví dụ nguồn và notebook bằng nhau: 1 đến 21, không thiếu, không thêm tên gốc. Slide không có mã W06/mức độ; notebook không invent các ID này. Các đề và lời giải được giữ trong khối details, giải thích thao tác trước và đọc kết quả sau.

| Ví dụ | Nội dung đã kiểm tra | Kết luận |
|---:|---|---|
| 1 | 5 lá [1,2,2,3,4]; PMF .2/.4/.2/.2; mẫu 50 gốc 10/24/10/6; mô phỏng 50/500/5000 và seed nguồn | Đầy đủ, phân biệt mẫu minh họa với output seed |
| 2 | 36 cặp xúc xắc, tổng 2–12, số cặp 1/2/3/4/5/6/5/4/3/2/1; simulation | Đúng |
| 3 | X là hàm Ω→R; HHT→2, TTT→0, biến cố X=2 | Đúng |
| 4 | PMF số ngửa 3 lần, 1/8,3/8,3/8,1/8 | Đúng |
| 5 | Ngửa trừ sấp 2N−3; support −3,−1,1,3; X=0 không thể | Đúng, đủ chuỗi tương ứng |
| 6 | 2 sản phẩm p=.8; PMF .04/.32/.64; CDF từng khoảng; P(0<X≤2)=.96 | Đúng |
| 7 | P(X<2)=F(1)=.36; jump tại1 .32 | Đúng, điều kiện support nguyên rõ |
| 8 | 6 đường điện thoại; PMF .10/.15/.20/.25/.20/.06/.04; ≤3 .70; <3 .45; chưa dùng2–4 .65; full CDF | Đúng |
| 9 | Đều rời rạc m giá trị; fair die; P≥5=1/3 | Đúng |
| 10 | Bernoulli p=1/2,3/4,2/3; 3 hình; 0/1 convention | Đúng |
| 11 | Uniform 1–1000; 333/200/66 bội; Y Bernoulli(.333) | Đúng |
| 12 | Binomial20,.25; P8=.06088669; P>2=.90873957 | Đúng |
| 13 | Binomial12,.95; P11=.34128006; P≥11=.88164014 | Đúng kết quả, lưu ý làm tròn trên |
| 14 | HG10,6,3; PMF1/30,3/10,1/2,1/6; mô phỏng không hoàn lại trong mỗi mẫu | Đúng |
| 15 | HG50,30,15; P10=.20695388; X≥10 hoặc X≤5=.39380392 | Đúng cả hai miền của “cùng một lớp” |
| 16 | 2 đỏ/2 xanh; 3 lượt có hoàn lại Bin3,.5; không hoàn lại HG4,2,3 | Đúng PMF, support và P3/P2 |
| 17 | Poisson1; P1=.36787944; P≤1=.73575888; hiển thị0–8 và đuôi còn lại | Đúng |
| 18 | Tốc độ4/giây; P0=.01831564; P>6=.11067398; 3giây→Poisson12 | Đúng đơn vị |
| 19 | Ghép Bernoulli/Binomial/Poisson/HG; n180/20 chưa đủ K | Đúng điều kiện mô hình |
| 20 | Binomial8,.04; ít nhất1=1−.96^8=.27861042 | Đúng |
| 21 | Binomial15,.75; đủ tồn kho xích/trục tương đương7≤X≤10=.30932104 | Đúng; không nhầm cầu độc lập với rút kho |

Bốn lệnh SciPy của nguồn được giữ, kể cả HG30,6,5 cho P2=.21304366, được phân biệt với hộp10/6/3.

Theory: phân phối lý thuyết vs tần suất; PMF nonnegative/sum1; discrete countable vs continuous; CDF mọi số thực, nondecreasing, limits, right continuity, jump và endpoint rules; đều rời rạc, Bernoulli, Binomial 4 điều kiện/edge p0,p1; Hypergeom 3 tham số, support max/min, combinatorial reasoning; Poisson support không giới hạn, λ theo cả khoảng, ổn định/độc lập/lumpy-arrivals caveat. Không dạy kỳ vọng/phương sai trước W7.

Đề cương có counting và roulette chưa được PDF nói đầy đủ: notebook bổ sung product rule, permutation/combination, CRATE/poker, net winnings ±1 chứ không +2/0. So sánh Binomial–Hypergeom hộp lớn, Poisson xấp xỉ rare-event Binomial đều ghi bổ sung STAT20, không giả mạo thành ví dụ gốc mới. Grammar giữ data/mapping/geometry và cảnh báo PMF column height khác histogram area khi support không cách1.

## Hình và asset

Các hình dữ liệu nguồn đều có code tương ứng: box PMF; ba panel empirical; dice PMF+simulation; PMF số ngửa; CDF sản phẩm; CDF điện thoại; uniform die; ba panel Bernoulli; HG10/6/3 PMF và simulation (gộp trong một hình giữ cả hai); Poisson1. Hình bổ sung roulette, slider nhị thức, comparison replacement và garage được ghi có mục đích.

Bốn ảnh STAT20 được giữ: hộp5lá, cây Geni3áo×2quần, ánh xạ Ω→số ngửa, roulette. Đã xem trực tiếp cả4, caption khớp. Decode4data URI có hash bằng4file local trong figures; không thiếu/unused. Nhúng ảnh nên copy riêng notebook vẫn đọc được; thư mục figures lưu bản nguồn phục vụ review.

Slide57–58 ghi “Ví dụ15” nhưng code hộp10/6/3 của Ví dụ14: notebook đặt lại đúng ví dụ và công bố đính chính, vẫn giữ đề/lời giải bài dự án Ví dụ15. Không silently bỏ code nguồn này.

## Kiểm chứng thực hiện

`check_w06_independent.py` parse AST 30 code cell, check set21Ví dụ, decode/hash4asset, tính độc lập bằng math.comb/exp cho các xác suất trọng yếu. Tất cả pass. `w06_independent_numbers.json` lưu số độc lập. Đây không phải execution toàn notebook; root đang kiểm nbclient/output/PNG/Plotly để hoàn tất QA hành vi và hiển thị.
