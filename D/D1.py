#D1
import os
os.system("cls" if os.name == "nt" else "clear")
chuoi = str(input("nhập: "))

if chuoi == "":
    print("vui lòng nhập chuỗi")
else:
    chu_hoa = ""
    chu_thuong = ""
    for c in chuoi:
        if c.isupper():
            chu_hoa += c
        elif c.islower():
            chu_thuong += c

    print("độ dài", len(chuoi))
    if chu_hoa == "":
        print("không có ký tự in hoa")
    else:
        print("các ký tự in hoa", chu_hoa)
    if chu_thuong == "":
        print("không có chữ in thường")
    else:
        print("các ký tự in thường", chu_thuong)
    print("ký tự đầu", chuoi[0])
    print("ký tự cuối", chuoi[-1])

    # OK