def climbing_stairs(n):
    if n == 1:
        return 1
    first = 1
    second = 1
    sum = 0
    for i in range (n - 1):
        sum = first + second
        second = first
        first = sum
    return sum

def coin_change(coins, amount):
    table = [amount + 1] * (amount + 1)
    table[0] = 0
    for i in range (1, amount + 1):
        for coin in coins:
            if coin <= i:
                remainder = i - coin
                if table[remainder] != -1:
                    if table[i] > table[remainder] + 1:
                        table[i] = (table[remainder] + 1)
            else:
                continue
        if table[i] == (amount + 1):
            table[i] = -1
    return table[amount]
    # Faster than 97% of users, less memory than 99% of users on Leetcode