#C4
import os
os.system("cls" if os.name == "nt" else "clear")
n = int(input("nhập n:"))

giai_thua = 1

for i in range(1, n + 1):
    giai_thua *= i
print(f"tổng các số từ 1 đến {n} là: {giai_thua}")
# Tổng???

print(f"giai thừa của {n} là: {giai_thua}")

# OK