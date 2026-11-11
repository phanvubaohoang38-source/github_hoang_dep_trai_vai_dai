#C6 
import os
os.system("cls" if os.name == "nt" else "clear")
def cac_so_nguyen_to(n):
    if n <= 2:
        return []
    la_nguyen_to = [True] * n
    la_nguyen_to[0] = la_nguyen_to[1] = False

    i = 2
    while i * i < n:
        if la_nguyen_to[i]:
            for j in range(i * i, n, i):
                la_nguyen_to[j] = False
        i += 1

    return [k for k in range(n) if la_nguyen_to[k]]


n = int(input("Nhập n: "))
print(*cac_so_nguyen_to(n))

# OK