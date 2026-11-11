#B3
import os
os.system("cls" if os.name == "nt" else "clear")
i = float(input("Nhập điểm (i):"))

if i < 0 or i > 10:
    print(f"điểm không hợp lệ")
elif i >= 8.5:
    print(f"Học sinh giỏi")

elif i >= 7:
    print(f"Học sinh khá")

elif i >= 5:
    print(f"Học sinh trung bình")
else:
    print(f"Học sinh yếu") 