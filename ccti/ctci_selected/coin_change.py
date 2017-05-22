
def find_coins_count(amount, currency_list):

    min_coins_dict = {}

    for i in range(1, amount+1):
        coins_list = []
        for currency in currency_list:
            if i >= currency:
                diff = i - currency
                if diff in min_coins_dict:
                    coins_list.append(min_coins_dict[diff])
                else:
                    coins_list.append(diff)

        min_coins = min(coins_list) + 1
        min_coins_dict[i] = min_coins
    #print min_coins_dict
    return min_coins

amount = 98
currency_list = [1,2,5,10]
print find_coins_count(amount, currency_list)