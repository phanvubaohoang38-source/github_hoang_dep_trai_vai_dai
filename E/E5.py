import os
os.system("cls" if os.name == "nt" else "clear")

n = list(map(int, input("Nhập các phần tử: ").split()))
x = list(map(int, input("nhập x: ").split()))

vitri = -1
dem = 0

for i in range(len(n)):
    if n [i] == x:
        if vitri == -1:
            vitri = i
        dem += 1

if not n:
    print("Danh sách rỗng.")
if not x:
    print("x rỗng")


else:
        if dem > 0:
            print(f"{x} có trong list")
            print("Vị trí xuất hiện đầu tiên:", vitri)
            print("Số lần xuất hiện:", dem)
        else:
            print(f"{x} không có trong list")