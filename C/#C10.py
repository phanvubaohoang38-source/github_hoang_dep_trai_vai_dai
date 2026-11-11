import os
os.system("cls" if os.name == "nt" else "clear")

total = 0
count = 0
so_lon_nhat = 0

while True:
    n = int(input("Nhập số nguyên dương (nhập 0 để kết thúc): "))
    if n == 0:
        break
    total += n
    count += 1
    if n > so_lon_nhat:
        so_lon_nhat = n

if count > 0:
    print(f"Tổng các số đã nhập: {total}")
    print(f"Trung bình cộng: {total / count}")
    print(f"Số lớn nhất: {so_lon_nhat}")
else:
    print("Không có số nào được nhập.")