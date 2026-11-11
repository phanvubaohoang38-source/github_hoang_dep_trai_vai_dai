#B4
import os
os.system("cls" if os.name == "nt" else "clear")

a = int(input("nhập điểm (a):"))

if a % 4 == 0 and a % 100 != 0 and a % 400 == 0:
    print(f"Năm nhuận")

else:
    print(f"năm không nhuận")