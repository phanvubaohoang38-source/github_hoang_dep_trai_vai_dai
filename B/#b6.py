#b6
import os
os.system("cls" if os.name == "nt" else "clear") 

a = float(input("nhập a: "))
b = float(input("nhập b: "))
c = float(input("nhập c: "))


if a > 0 and b > 0 and c > 0:
    if c * c == a * a + b * b:
        print(f"tam giác vuông")

    elif a == b or b == c or a == c:
        print(f"tam giác cân")
    else:
        print(f"tam giác thường")