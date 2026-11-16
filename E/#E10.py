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