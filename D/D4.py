import os
os.system("cls" if os.name == "nt" else "clear")

s = input("nhập chuỗi: ")

def is_palindrome(s):
    cleaned = s.replace(" ", "").lower()
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome(s))

# OK
