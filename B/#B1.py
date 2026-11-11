#B1
import os
os.system("cls" if os.name == "nt" else "clear")
n = int(input("nhập n:"))

if n % 2 == 0:
    print(f"{n} là số chẵn")
else:
    print(f"{n} là số lẽ")