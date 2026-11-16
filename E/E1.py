import os
os.system("cls" if os.name == "nt" else "clear")

n = list(map(int, input("nhập các số nguyên (cách nhau bằng dấu cách): ").split()))

if not n:
    print("Danh sách rỗng.")
else:
    print("độ dài: ", len(n))
    print("Tổng:", sum(n))
    print("Lớn nhất:", max(n))
    print("Nhỏ nhất:", min(n))
    print("Trung bình cộng:", round(sum(n) / len(n), 2))

# OK 
# English only