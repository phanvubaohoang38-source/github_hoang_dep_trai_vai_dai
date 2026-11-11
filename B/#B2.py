#B2
import os
os.system("cls" if os.name == "nt" else "clear")

g = float(input("nhập số thứ nhất (g):"))
j = float(input("nhập số thứ hai (j):"))
h = float(input("nhập số thứ ba (h):"))

so_lon_nhat = g

if h > so_lon_nhat:
    so_lon_nhat = h

if j > so_lon_nhat:
    so_lon_nhat = j


print(f"Số lớn nhất là: {so_lon_nhat}")
