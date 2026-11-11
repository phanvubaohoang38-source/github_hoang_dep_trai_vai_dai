#C9
import os
os.system("cls" if os.name == "nt" else "clear")
import random

so_ngau_nhien = random.randint(1, 100)
so_lan = 0 


print("Mình đã chọn một số từ 1 đến 100. Hãy đoán thử!")

while True:
    try:
        doan = int(input("Số của bạn: "))
    except ValueError:
        print("Vui lòng nhập một số nguyên.")
        continue

    so_lan += 1


    if doan < so_ngau_nhien:
        print("Lớn hơn!")
    elif doan > so_ngau_nhien:
        print("Nhỏ hơn!")
    else:
        print(f"Chính xác! Bạn đã đoán đúng sau {so_lan} lần.")
        break

# OK