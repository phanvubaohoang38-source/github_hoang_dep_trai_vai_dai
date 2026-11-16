#E7


import os
os.system("cls" if os.name == "nt" else "clear")

n = list(map(int, input("nhập: ").split()))

if not n:
    print("Danh sách rỗng.")
else:
       vi_tri = 0
for i in range(1, len(n)):
    if n[i] > n[vi_tri]:  
        vi_tri = i
        
        print(vi_tri + 1)