budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25
portion_milk_price = milk_price * 0.25

total_price_per_bread = flour_price + eggs_price + portion_milk_price

total_price = 0
loaf_of_bread = 0
coloured_eggs = 0

while budget >= total_price_per_bread:
    loaf_of_bread += 1
    coloured_eggs += 3
    budget -= total_price_per_bread

    if loaf_of_bread % 3 == 0:
        coloured_eggs -= loaf_of_bread - 2

print(f'You made {loaf_of_bread} loaves of Easter bread! Now you have {coloured_eggs} eggs '
      f'and {budget:.2f}BGN left.')
