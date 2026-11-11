#C5
import os
os.system("cls" if os.name == "nt" else "clear")
n = int(input("nhập số nguyên dương n:"))

so_chu_so = 0
tong = 0

while n > 0:
    chu_so = n % 10
    tong += chu_so
    so_chu_so += 1
    n //= 10

print(f"số chữ số của n là: {so_chu_so}")
print(f"tổng các chữ số của n là: {tong}")

# OK