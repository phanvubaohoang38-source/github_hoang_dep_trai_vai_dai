#E2

import os
os.system("cls" if os.name == "nt" else "clear")


nums = list(map(int, input("Nhập các số nguyên: ").split()))


if not nums:
    print("Danh sách rỗng.")
else:

    print("Vị trí chẵn (chỉ số 0, 2, 4...):", nums[::2])
    print("Vị trí lẻ (chỉ số 1, 3, 5...):", nums[1::2])

# OK 
# English only