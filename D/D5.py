import os
os.system("cls" if os.name == "nt" else "clear")


s = str(input("Enter : "))

word = s.split()

print("Số từ : ", len(word))
print("từ dài nhất: ", max(word, key=len))

# OK