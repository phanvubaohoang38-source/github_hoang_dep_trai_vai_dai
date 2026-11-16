import os
os.system("cls" if os.name == "nt" else "clear")

a = list(map(int, input("Nhập các phần tử: ").split()))

if not a:
    print("Danh sách rỗng.")
else:


    ket_qua1 = []
    for x in a:
        if x % 3 == 0:
            ket_qua1.append(x)
            print("Vòng lặp thường:", ket_qua1)


    ket_qua2 = [x for x in a if x % 3 == 0]
    print("List comprehension:", ket_qua2)