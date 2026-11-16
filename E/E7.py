#E7


import os
os.system("cls" if os.name == "nt" else "clear")

n = list(map(int, input("input: ").split()))

if not n:
    print("null List.")
else:
       vi_tri = 0
for i in range(1, len(n)):     # <- outside else syntax 
    if n[i] > n[vi_tri]:  
        vi_tri = i
        
print(vi_tri + 1)