word = ''

coffee = 0

while word != "END":
    word = input()
    lower_word = word.lower()

    if lower_word == "coding":
        if word.isupper():
            coffee += 2
        else:
            coffee += 1

    elif lower_word == "dog":
        if word.isupper():
            coffee += 2
        else:
            coffee += 1

    elif lower_word == "cat":
        if word.isupper():
            coffee += 2
        else:
            coffee += 1

    elif lower_word == "movie":
        if word.isupper():
            coffee += 2
        else:
            coffee += 1
    else:
        continue

if coffee <= 5:
    print(coffee)
else:
    print('You need extra sleep')

