#E9
import os
import random
os.system("cls" if os.name == "nt" else "clear")
try:
    n = int(input("nhập n: "))
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")
    exit()
if n <= 0:
    print("n không hợp lệ.")
else:
    list =[random.randint(1, 100) for _ in range(n)]
    print("list ban đầu :", list)

    squared = [x ** 2 for x in list]
    print("list bình phương :", squared)