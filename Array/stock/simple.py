if not prices:
    return 0

min_price = 100000
max_price = 0

for price in prices:
    if price < min_price:
        min_price = price
    elif price - min_price > max_price:
        max_price = price - min_price

return max_price
