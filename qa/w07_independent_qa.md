> Báo cáo đối chiếu nội dung độc lập. Các finding của bản đầu (nếu có) đã được xử lý; kết quả chạy và kiểm tra bản phát hành cuối ngày 07/10/2026 nằm trong `W05_W07_VALIDATION.json` và `../KIEM_TRA_NOTEBOOKS.md`.

# QA độc lập notebook buổi 7

Ngày kiểm tra: 2026-10-06. Phạm vi chỉ đọc: `E:\Teaching\XSTK\07_expectation_variance_normal\notebook.ipynb`; không sửa notebook/builder hoặc Git.

## Kết luận

Không phát hiện lỗi nội dung, công thức, đáp án hay thiếu phần so với 94 trang `Slides/week07.pdf` và mục 3.6/3.7 của đề cương. Bản đã kiểm có **79 cell: 47 Markdown + 32 code**. Đã đọc tất cả cell, toàn bộ nội dung văn bản 94 trang slide, các điều kiện mô hình và từng lời giải. Đủ **15/15 Ví dụ và 10/10 Bài tập**, giữ các số liệu/câu hỏi gốc. Không dùng riêng metadata để kết luận coverage: metadata 94/94 là phép kiểm bổ sung sau đọc nội dung.

## Đối chiếu nội dung nguồn

| Nguồn slide | Cell (zero-based) | Kiểm tra |
|---|---|---|
| Trang 1–3: dẫn nhập, mục tiêu | 0 | Đúng buổi, giảng viên, LLO7.1/CLO2; dẫn từ phân phối buổi 6 sang E/Var và tổng/trung bình |
| 4–6, Ví dụ 1 | 2–4 | Hai sản phẩm iid, p=0,8; pmf 0,04/0,32/0,64; E=1,6; kỳ vọng không nhất thiết khả dĩ |
| 7–9, Ví dụ 2 | 5–6 | Tính tuyến tính hữu hạn, không đòi độc lập; C=50+20X nghìn đồng; E(C)=82 |
| 10–12, Bài tập 1 | 7–8 | E[g(X)], xác suất theo biến gốc; hai bạn tung xu; phần bánh 1/(N+1); E=7/12 ≠ 1/2 |
| 13: E các phân phối | 9 | Bernoulli p, nhị thức np, siêu bội nK/N, Poisson λ; tách K tổng thể với n mẫu |
| 14–16, Ví dụ 3 | 10–11 | Định nghĩa Var/SD và rút gọn; Var=0,32, E(X²)=2,88, SD=0,565685; đơn vị đúng |
| 17–19, Bài tập 2 | 12–13 | Var(aX+b)=a²Var, SD=abs(a)SD; Fahrenheit E=77, Var=29,16, SD=5,4; độc lập khi cộng Var, Cov khi phụ thuộc |
| 20: Var phân phối | 14 | Bernoulli, Binomial, Poisson, Hypergeometric đúng; finite population correction và N>1 |
| 21–24, Ví dụ 4 | 18–20 | Độc lập chung/cùng phân phối qua cdf; hộp 1..6 và hai lần rút hoàn lại; tổng không đều |
| 27–28, Ví dụ 5 | 21–23 | Đúng hộp 10 lá 0,0,1,1,1,2,3,3,4,4; E=1,9, E²=5,7, Var=2,09; ddof=0 |
| 25–26, 29–32, Ví dụ 6 | 24–26 | Công thức tổng/trung bình đúng mọi n; n25/n100; mô phỏng 5.000 mẫu, axis=1; seed42 được giải thích khác seed2026 |
| 33–36, Bài tập 3 | 34–35 | Chebyshev ε>0/phương sai hữu hạn; cận sai lệch trung bình; 2.500 là sufficient theo cận |
| 37–40, Bài tập 4 | 36–38 | WLLN iid Eabs finite; không cần phương sai hữu hạn; hội tụ xác suất không đơn điệu; ngửa lần11 vẫn0,5 |
| 41–47, Bài tập 5/Ví dụ 7 | 39–40 | PDF không âm/area1, density có thể>1, Ppoint0; CDF mọi RV và tích phân nếu PDF; f=2x/F=x² theo3miền, P=.32 |
| 48–49, Ví dụ 8 | 41–42 | E từ tích phân=2/3; E²=1/2; Var=1/18; mô phỏng sqrt(U) đúngCDF |
| 50–53, Ví dụ 9 | 43–44 | Uniform pdf/cdf/E/Var đầy đủ; U0,10, P2..5=.3, E5phút, SciPy scale=b−a |
| 54–57, Ví dụ 10 | 45–46 | Normal μ,σ²/pdf; σ>0; Z=(X−μ)/σ; z86=2; chuẩn hóa không tự tạo normal; slider SD |
| 58–59, Ví dụ 11 | 47–48 | Quy tắc68/95/99,7 riêng normal; model500,SD2; giới hạn chính xác và đuôi504=.02275 |
| 60–62, Ví dụ 12 | 49–50 | CDF503=.9331928, SF=.0668072, interval=.6826895, q95=503.289707; scaleSD2, ppf trả giá trị |
| 63–65, Ví dụ 13 | 51–52 | Exp rateλ=.5/phút, SciPy scale2, E2, Var4, SF3=.2231302; tô đuôi hữu hạn được nêu rõ |
| 66–67: χ²/t | 53–54 | PDFs và Gamma đúng; ν>0; χ²≥0/lệch phải, t đối xứng/đuôi dày; chỉ nhận diện, chưa kiểm định/CI |
| 68–73, Ví dụ 14 | 55–56 | CLT iid meanfinite, 0<Var<∞; chuẩn hóa đúng; sumSD√n/meanSD1/√n; 25/100 khác5.000; hộp vẫn rời rạc |
| 74–75: mô phỏng CLT | 57–61 | Exp meanSD5phút, bốn n1/5/30/100, 5.000mẫu; chuẩn hóa theoSDmean; histogramvsnormal; slider tái dùng dữ liệu |
| 76–77, Ví dụ 15 | 62–63 | Mean12/SD6/rightskew, n64; SDmean.75, SF13.5=.0227501; assumptions/approx explicit |
| 78–81, Bài tập 6 | 67–68 | USB x1/2/4/8/16, p.05/.10/.35/.40/.10; E6.45GB, E²57.25GB², Var15.6475GB², SD3.955692GB |
| 82–83, Bài tập 7 | 69–70 | F=x²/9 trên0..b, liên tụccho b3; pdf2x/9 trên0..3; 0outside; endpoints đúng |
| 84–85, Bài tập 8 | 71–72 | 10iidNormal65,5²; sumexactNormal650,250; CDF700=.9992173; nguồn được đóngkhungmodelgiảđịnh |
| 86–88, Bài tập 9 | 73–74 | Đủ5câu: individualSF10, sum100CDF300, mean100interval, individualinterval, mean36interval; giữtailCLTcaution |
| 89–91, Bài tập 10 | 75–76 | mean100h/SD30h, total2000h, >=95%; n22=.922391/n23=.981472; 23bao1banđầu+22dựphòng; chỉước tínhCLT |
| 92–94: tóm tắt và học tiếp | 77–78 | Ôn1..7, buổi8giữa kỳ/giải đáp, buổi9sampling/CI; mốc tính tay và nguồn/errata explicit |

## Lý thuyết và tính dễ đọc

Các điều kiện hữu hạn/độc lập, đơn vị, biến quan sát so với phân phối và tổng so với trung bình đều được nêu. Các thay đổi so với nguồn bổ sung sửa lỗi hoặc làm giả định rõ hơn: iid qua cdf; hộp STAT20 11 lá được sửa về 10 lá đúng slide; sai số chuẩn không bị đồng nhất với SD của cá thể; xe buýt/khối lượng/tuổi thọ có nhãn mô hình giả định. CLT không có quy tắc n30 tự bảo đảm và BT10 không hứa bảo đảm chỉ từ hai moment.

Mỗi code cell có đoạn giới thiệu nhiệm vụ ngay trước hoặc phần đọc/diễn giải ngay sau; code ngắn, biến/đơn vị/axis=1/n-vs-lặp/loc-scale có giải thích ở nơi sử dụng. Bài tập có đáp án đóng/mở dưới đề. Grammar of Graphics buổi3 được giữ và nhắc lại; không sửa W1–4 trong phạm vi audit.

## Kiểm chứng độc lập

Chạy `check_w07_independent.py` ngoài repo, dùng `math.erf`, `exp`, `sqrt`, `comb` và phép cộng có trọng số, không sao chép phép tính SciPy của notebook để tạo expected values. Kết quả lưu ở `w07_independent_numbers.json`.

- Nhãn nguồn regex từ text slide và nội dung Markdown cùng có Ví dụ1..15, BT1..10; AST32code valid; union cell source_pages=1..94.
- Các mốc số của toàn bộ Ví dụ/Bài tập khớp đáp án notebook. BT9 lần lượt: **0.1353352832; 0.0000316712 (CLT); 0.2346814510 (CLT); 0.0218564169; 0.1425932977 (CLT)**.
- 5/5 ảnh attachment, file local `figures`, và ảnh gốc giải mã từ STAT20 có byte/hash giống nhau; mỗi ảnh dùng đúng 1cell và đúngsource index124/123/120/125/126. Tất cả ảnh local được sử dụng, không có ảnh sót.
- Snapshot sau tác giả execute có execution_count1..32 đầy đủ, không stored output error. Đây là kiểm tra kết quả lưu, **không thay thế việc root chạy nbclient clean-kernel lần cuối** sau mọi sửa đổi.
- Đã đối chiếu code dựng các biểu đồ gốc: WLLN, Uniform, Normal±SD, hai tổng/hai mean hộp, 4panelCLTExp; χ²/t thêm hình đúng công thức; supplementarySTAT20 dice/Bernoulli/randomwalk/roulette giữ trực giác. Root chịu trách nhiệm render/ảnh/Plotly interaction QA; chưa khẳng định đã kiểm toàn bộ layoutpixel trong báo cáo này.

## Finding cần sửa

**Không có finding cần sửa** trong snapshot đã kiểm. Cần giữ thông tin CLT là xấp xỉ và tránh đổi BT10 từ total23 thành23dựphòng ở bước đóng gói.

## Recheck sau gián đoạn — 2026-10-07

Đã đọc lại source toàn bộ 79cell và chạy lại phép kiểm độc lập: kết quả vẫn 15VD/10BT, 94trang source metadata, 32code AST hợp lệ, 5ảnh original/local/attachment giống byte, execution_count1..32 và không stored error. Không thấy thay đổi nội dung so với review ngày06; không có finding mới. Không thực hiện kernel execution hoặc sửa notebook.

Lưu baseline mới `w07_reviewed_source_snapshot_20261007.json` gồm id/type/source/cellmetadata (loại execution timestamps). SHA256 baseline: `917dac16d9d52231ca39dd8638a7c0484692c4d5fff3777e410697eee5d38b7d`. SHA256 toàn notebook hiện tại: `6be3bb506182007d12e37fe6fb8138e3f78a8a1f50a4be958ae5e53948e53da6`. Không có hash toàn file trước gián đoạn nên nhận xét không đổi là đối chiếu nội dung đã đọc, không là chứng minh byte-identity trước/sau.

Xác nhận audit W1–4 chỉ đọc JSON/source và dữ liệu: **không execute W4**, không nbclient/kernel/nbconvert với W1–4, không sửa file W1–4. Không có Git mutation trong task này.
