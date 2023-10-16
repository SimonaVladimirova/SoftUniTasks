orders = int(input())

total_price = 0

for i in range(0, orders):
    price = float(input())
    days = int(input())
    capsules = int(input())

    if 0.01 > price or price > 101:
        continue

    if 1 > days or days > 31:
        continue

    if 1 > capsules or capsules > 2000:
        continue

    price_per_order = (price * capsules) * days
    print(f'The price for the coffee is: ${price_per_order:.2f}')

    total_price += price_per_order

print(f'Total: ${total_price:.2f}')
