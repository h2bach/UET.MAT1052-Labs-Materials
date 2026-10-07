> Báo cáo đối chiếu nội dung độc lập. Các finding của bản đầu (nếu có) đã được xử lý; kết quả chạy và kiểm tra bản phát hành cuối ngày 07/10/2026 nằm trong `W05_W07_VALIDATION.json` và `../REVIEW_W05_W07.md`.

# QA độc lập W5 — 2026-10-06

Snapshot: `05_probability/notebook.ipynb`, 91cell, 19code, 18exercise, 20asset. Đọc toàn bộ source mọi cell, toàn bộ93trang week05.txt (gộp dòng lặp), phần Buổi5/3.1–3.3/LLO5.1–5.2 của đề cương. Không edit builder/notebook và không chạy kernel vì root thực hiện nbclient.

## Findings cần sửa

1. **Công thức không gian mẫu mất escape ở w05-007.** Đang hiện `$Omega$`, `$Omega={1,2,3,4,5,6}$`, `$Omega={mathrm{ĐĐ,ĐK,KĐ,KK}}$`, `$Omega=[0,infty)$`, `$C={6}$`. Phải phục hồi `\Omega`, `\{...\}`, `\mathrm`, `\infty`. Đây là lỗi Markdown/render và mất ký hiệu tập hợp, không phải lỗi Python.
2. **Bỏ các ví dụ mở đầu nguồn dù yêu cầu nội dung gốc đầy đủ.** Câu hỏi điểmA≈32% dựa lớp trước, bóngđáVN–TháiLan, Cờtỷphú mặtgiốngnhau1/6, mưa ngàymai; ví dụ nhà máy lấy mẫu linh kiện và tỷlệlỗi khác giữa mẫu. Cell0 còn ý chung nhưng thiếu ví dụ cụ thể. Thêm Markdown ngắn, 32% ghi số minh họa nguồn không là dữ liệu lớp hiện tại, bóngđá/mưa giữ dạng câu hỏi chứ không dự báo thực tế.
3. **Caption hình5.S3 nói hai mặt nhưng ảnh chỉ một mặt.** Dùng “ảnh một đồng xu; mô hình phân biệt H và T”.
4. **w05-046 hướng dẫn đổi số ở ô trước sẽ đổi cả cây không đúng.** Prevalence slidercell45 chỉ đổi5.4, treecell43 dùng group_probs/positive_probs. Hướng dẫn sửa tạicell43 rồi rerun hoặc nói slider chỉ đổi biểuđồ5.4.

Root đã nhận các finding và xác nhận sẽ sửa source + regenerate + rerun. Báo cáo snapshot này chưa tự chứng nhận các sửa đã hoàn tất.

## Coverage đã kiểm chứng

18/18mã nguồn có trong notebook; setdifference cả hai chiều rỗng. Không invent BT03/BT06/TH02.

| Mã | Cell snapshot | Kết quả/ý nghĩa đã kiểm tra |
|---|---:|---|
| Q01 | 6 | B: các sự kiện6ởcác lần không xung khắc |
| BT01 | 11 | 8lá;HH/HT1/4,Tj1/12;không đồng khả năng |
| Q02 | 13 | B:xung khắc nhưng không đối |
| EX01 | 14 | union,complementunion,complementintersection,onlyA |
| BT02 | 15 | ít nhất/cảba/chỉA1/đúng1 biểu diễn đúng |
| EX02 | 21 | 69/86 và69/107 đúngmẫu số |
| BT04 | 25 | 10/30=1/3,loại66 |
| BT05 | 30 | 207/625=.3312 |
| EX03 | 31 | 1/6≠5/36,phụ thuộc |
| EX04 | 35 | .02*.6+.05*.4=.032;B|L=.625 |
| BT07 | 36 | .016 với trọng số70/20/10 |
| BT08 | 37 | .4375,.25,.3125;tổng1;source1cao nhất |
| EX05 | 41 | .234;I|+=.099/.234=11/26 |
| Q03 | 48 | C:xung khắc/Ppositive→phụ thuộc |
| CH01 | 54 | 1−(1−p)^n;n35;npđếm lặp |
| CASE01 | 58 | .874,.996,.004;độc lập khi đãcháy |
| TH01 | 59 | 5/21,4/5;cây2bước |
| TH03 | 62 | 389/450,59/450;post225/389,108/389,56/389và0,27/59,32/59 |

Theory coverage: phép thử/3loại không gian mẫu/biến cố/bao hàm/hợp/giao/phầnbù/hiệu/xungkhắc/đối/DeMorgan;3tiênđề+cộngđếmđược+hệquả;đồngkhảnăng+cảnhbáo nhầm vé/giátrị;tầnsuấtdàihạn;additiongeneral;conditionalP(B)>0;chain3events;replacementmechanism;independenceproduct/conditionalpositive;Sallyhai sai lầm;partition/totalprobability/Bayes;DeMéréexact/MonteCarlo;sourceexercises/misconceptions/transitions. Bao hàm–loại trừ3biến được ghi bổ sungSTAT20. Grammar trongcell40 giữdata/mapping/geometry theo nguyên lý.

Venn nguồntrang21, SIRtrang68, DeMéréplottrang78 đều dựnglạibằng code; không mất plot gốc. Notebook còn các hình bổ sung Bayesian accountbar, prevalenceSlider, runningRate, atLeastOneFailure và treechuyểnbi, ghi bổ sung rõ. Mô phỏng và tham số giả định được phân biệt với tính đúng/exact và dữ liệu thực.

20/20imagefile được tham chiếu local đúng,0missing/0unused. Đã xem trực tiếp cả20ảnh: các boxcounts,rankofcolors/two-numbers/conditionalfilter/Venn khớp caption ngoại trừ findingcaptionS3. Sourceimages dùng nguyêný, không đưa ảnhRcode/screenshot như demoPython.

Beginner readability nhìn chung tốt: code nhỏ; shape/axis Boolean/conditionaldenominator giải thích trước; output diễn giải sau; dựđoántrước;3code exactenumeration; môphỏnggiữseed42; lời giải details; sourcepagecrosswalk. Bản đầu cần fix4findings trên trước khi coi đầyđủ gốc và sẵnreview. QAexecution và rendereroffline do root phụ trách.
