number = int(input())

for i in range(0, number):
    num = int(input())

    if num == 88:
        print("Hello")
    elif num == 86:
        print("How are you?")
    elif num <= 87 and num != 86:
        print("GREAT!")
    elif num > 88:
        print("Bye.")

