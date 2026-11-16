#E8

import os
os.system("cls" if os.name == "nt" else "clear")

n = list(map(int, input("Nhập: ").split()))

if not n:
    print("Danh sách rỗng.")
else:
    tang_dan = True
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            tang_dan = False
            break

    print("có" if tang_dan else "không")