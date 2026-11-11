#C3 
import os
os.system("cls" if os.name == "nt" else "clear")
n = 10

m = int(input("nhập m:"))

bang_cuu_chuong = 0


for i in range(1, n + 1):
    bang_cuu_chuong = m * i
    print(f"{m} * {i} = {bang_cuu_chuong}")

# OK
