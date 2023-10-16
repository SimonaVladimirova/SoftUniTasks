import string
number = int(input())
x = ",._"

for i in range(0, number):
    word = input()
    if any(char in word for char in x):
        print(f"{word} is not pure!")
    else:
        print(f"{word} is pure.")
