#C7
import os
os.system("cls" if os.name == "nt" else "clear")

for i in range(1, 101):
    # In thế này khó đọc quá, nên in ra theo format
    print(i, end=": ")
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# In lộn xộn thế này

# OK
