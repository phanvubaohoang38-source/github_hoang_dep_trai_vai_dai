#C2
import os
os.system("cls" if os.name == "nt" else "clear")
n = int(input("nhập n:"))

tong = 0

for i in range(1, n + 1):
    tong += i

# Cách 2: n*(n+1)//2 = tổng từ 1 đến n
print(f"tổng các số từ 1 đến {n} là: {tong}")
print(f"tổng các số từ 1 đến {n} là: {n*(n+1)//2}")

# OK
