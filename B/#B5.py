#B5
import os
os.system("cls" if os.name == "nt" else "clear")

a = float(input("a(a)"))
b = float(input("b(b)"))
c = float(input("c(c)"))

if a == 0:
    
    if b != 0:
       x = - c / b
       print(f"phương trình có nghiệm x = {x}")
    elif c == 0:
        print(f"phương trình có vô số nghiệm")
    else:
        print(f"phương trình vô nghiệm")


else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print("phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"phương trình có nghiệm kép x = {x}")
    else:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print(f"phương trình có 2 nghiệm phân biệt x1 = {x1} và x2 = {x2}")
        