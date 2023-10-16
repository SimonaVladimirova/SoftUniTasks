from itertools import count

name = input()
char_count = 0

while name != "Welcome!":
    char_count = len(name)

    if name == "Voldemort":
        print("You must not speak of that name!")
        break

    if char_count < 5:
        print(f'{name} goes to Gryffindor.')

    elif char_count == 5:
        print(f'{name} goes to Slytherin.')

    elif char_count == 6:
        print(f'{name} goes to Ravenclaw.')

    elif char_count > 6:
        print(f'{name} goes to Hufflepuff.')

    name = input()

else:
    print('Welcome to Hogwarts.')


