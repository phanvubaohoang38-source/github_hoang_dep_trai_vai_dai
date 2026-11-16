import os
os.system("cls" if os.name == "nt" else "clear")

n = list(map(int, input("Nhập các phần tử: ").split()))

if not n:
    print("Danh sách rỗng.")
else:
    print("Slicing:", n[::-1])

# OK
# English only
# Missing remain methods