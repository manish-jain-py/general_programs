def find_max_price(prices, rod_len):
    if rod_len == 0:
        return 0
    q = 0
    for i in range(1, rod_len+1):
        q = max(q, prices[i] + find_max_price(prices, rod_len-i))
    return q


def find_max_price_iter(prices, rod_len):

    opt_prices = [0]

    if rod_len == 0:
        return 0

    for rod in range(1, rod_len + 1):
        price = -1

        for cut in range(1, rod + 1):
            rem = rod - cut
            price = max(price, prices[cut] + opt_prices[rem])

        opt_prices.append(price)
    return opt_prices


prices = [0, 4, 9, 8, 9, 10, 13, 17, 20, 24, 30]
print find_max_price_iter(prices, 10)
