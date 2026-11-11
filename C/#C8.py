import os
os.system("cls" if os.name == "nt" else "clear")

n = int(input("Nhập n: "))


print("Tam giác vuông:")
for i in range(1, n + 1):
    print("*" * i)

print("Tam giác cân:")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))