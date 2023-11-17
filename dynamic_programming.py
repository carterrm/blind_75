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

def longest_increasing_subsequence(nums:list[int]) -> int:
    #Beats 69.27% on runtime, 36.72% on memory
    result_array = [0] * (len(nums))
    result_array[len(nums) - 1] = 1
    for i in range(len(nums) - 2,-1, -1):
        intermediate_set = []
        intermediate_set.append(1)
        for j in range(i + 1, len(nums)):
            if(nums[j] > nums[i]):
                intermediate_set.append(result_array[j] + 1)
        result_array[i] = max(intermediate_set)
    return max(result_array)

