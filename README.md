Sorting Algorithm Benchmark Suite
Dự án này là một bộ công cụ toàn diện được viết bằng Python nhằm mục đích tạo dữ liệu thử nghiệm và đo lường hiệu suất của các thuật toán sắp xếp phổ biến trong Cấu trúc dữ liệu và Giải thuật (DSA).

🚀 Tính năng chính
Dataset Generation: Tự động tạo 10 kịch bản dữ liệu khác nhau (1 triệu phần tử/mỗi file) bao gồm: đã sắp xếp, sắp xếp ngược, số thực ngẫu nhiên và số nguyên ngẫu nhiên.

Algorithm Comparison: So sánh các thuật toán tự cài đặt (Merge Sort, Quick Sort, Heap Sort) với các thư viện chuẩn tối ưu hóa cao (Numpy Sort, Python Timsort).

Performance Analytics: Báo cáo chi tiết thời gian thực thi dưới đơn vị mili giây (ms)

📂 Cấu trúc mã nguồn

1. dataset_manager.py (Bộ tạo dữ liệu)
   Tệp này chịu trách nhiệm tạo ra môi trường thử nghiệm khách quan.

file_01: Mảng đã sắp xếp tăng dần (Kiểm tra trường hợp tốt nhất).

file_02: Mảng sắp xếp giảm dần (Kiểm tra trường hợp tệ nhất).

file_03 - 06: Số thực ngẫu nhiên (Uniform distribution).

file_07 - 10: Số nguyên ngẫu nhiên (Integer distribution).

2. sorting_benchmark.py (Bộ đo lường)
   Tệp thực hiện việc đọc dữ liệu và vận hành các thuật toán:

Hệ thống phân cấp: Sử dụng Class Sorting để quản lý thuật toán và Class Benchmark để quản lý luồng đo lường.

Xử lý đệ quy: Đã được tối ưu hóa bằng sys.setrecursionlimit để không bị tràn ngăn xếp khi xử lý 1.000.000 phần tử.
CÓ THỂ THAM KHẢO FILE ĐƯỢC TẠO VÀ TÔI DÙNG ĐỂ ĐÁNH GIÁ TẠI ĐÂY:https://drive.google.com/drive/folders/1-MBiim7TYbG9aIEoD1roZ_lPZY-R1kCK?usp=sharing
