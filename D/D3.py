import os
os.system("cls" if os.name == "nt" else "clear")

s = str(input("Enter : "))
vowels = "aeiouAEIOU"
count = 0
for ch in s.lower():
    if ch in vowels:
        count += 1
print(count)

# OK