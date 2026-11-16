import os
os.system("cls" if os.name == "nt" else "clear")

n = list(map(int, input("Nhập các phần tử: ").split()))
x = list(map(int, input("nhập x: ").split()))



vitri = -1
dem = 0

for i in range(len(n)):
    if n [i] == x:  # x là một list mà đi so sánh với n[i] là một số nguyên nên sẽ luôn trả về False
        if vitri == -1:
            vitri = i
        dem += 1

if not n:
    print("Danh sách rỗng.")
if not x:
    print("x rỗng")


else:    # else này chỉ đi cùng `if not x   ->  thử nhập rỗng là sai liền
        if dem > 0:
            print(f"{x} có trong list")
            print("Vị trí xuất hiện đầu tiên:", vitri)
            print("Số lần xuất hiện:", dem)
        else:
            print(f"{x} không có trong list")