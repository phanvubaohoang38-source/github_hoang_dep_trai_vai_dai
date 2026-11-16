#E10
import os
os.system("cls" if os.name == "nt" else "clear")

n = list(map(int, input("Nhập list: ").split()))

k = int(input("Nhập k: "))

if not n:
    print("Danh sách rỗng.")
else:
    cong = [x + k for x in n]
    print("list sau khi cộng k:", cong)
    trung_binh = sum(n) / len(n)
    print("trung bình cộng:", trung_binh)
    cao_hon = [x for x in cong if x > trung_binh]
    print("Các phần tử lớn hơn trung bình:", cao_hon)

# in list gồm các phần tử lớn hơn trung bình cộng. 
# Mày tính trung bình của list gốc n, nhưng lại lọc trên list đã cộng k ("cong"). 
# Hai list lệch nhau k nên kết quả sai.

# Ví dụ 1 2 3, k = 10, trung bình gốc = (1 + 2 + 3) / 3 = 2, sau do cong = [11, 12, 13], 
# tất cả đều > 2 nên in cả 3 số, 
# trong khi chỉ 13 = 3(lúc chưa cộng k) mới thực sự lớn hơn trung bình.