decorations = int(input())
days_left = int(input())

price = 0
points = 0

for day in range(1, days_left + 1):
    if day % 11 == 0:
        decorations += 2

    if day % 10 == 0:
        price += 23
        points -= 20

        if day == days_left:
            points -= 30

    if day % 2 == 0:
        price += 2 * decorations
        points += 5

    if day % 3 == 0:
        price += 8 * decorations
        points += 13

    if day % 5 == 0:
        price += 15 * decorations
        points += 17

    if day % 15 == 0:
        points += 30

print(f'Total cost: {price}')
print(f'Total spirit: {points}')
