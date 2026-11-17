def coin_change_greedy(amount, coins):
    coins.sort(reverse=True)
    result = {}

    for coin in coins:
        if amount >= coin:
            num_coins = amount // coin
            amount -= num_coins * coin
            result[coin] = num_coins

    return result


# Example usage
coins = [5, 10, 13, 28]
amount =56

result = coin_change_greedy(amount, coins)

# Display result
print(result)   