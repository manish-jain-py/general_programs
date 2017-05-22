def find_ways(amount, currencies, change = ''):
    if amount == 0:
        print change
        return 1
    elif amount < 0:
        print change
        return 0
    else:
        ways = 0
        for currency in currencies:
            change += str(currency)
            ways += find_ways(amount - currency, currencies, change)
        return ways

print find_ways(5, [1, 2, 3])
