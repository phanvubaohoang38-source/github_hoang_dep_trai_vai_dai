import os
os.system("cls" if os.name == "nt" else "clear")

a = list(map(int, input("Nhập: ").split()))

chan = le = am = duong = 0


for x in a:
    if x % 2 == 0:
        chan += 1
    else:
        le += 1
    if x < 0:
        am += 1
    elif x > 0:
        duong += 1

if not a:
    print("Danh sách rỗng.")
else:
    print("Số phần tử chẵn:", chan)
    print("Số phần tử lẻ:", le)
    print("Số phần tử âm:", am)
    print("Số phần tử dương:", duong)