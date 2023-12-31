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

def longest_common_subsequence(text1:str, text2:str) -> int:
    #Beats 57.70% on runtime, 28.26% on memory usage
    grid = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                grid[i][j] = 1 + grid[i + 1][j + 1]
            else:
                grid[i][j] = max(grid[i + 1][j], grid[i][j + 1])

    return grid[0][0]


def word_break(s:str, wordDict: list[str]) -> bool:
    #Beats 81.15% on runtime, 67.15% on memory

    results = [False] * (len(s) + 1)
    results[len(s)] = True
    for i in range(len(s) - 1, -1, -1):
        for word in wordDict:
            is_match = True
            for j in range(0, len(word)):
                if j + i > len(s) - 1:
                    is_match = False
                    break
                else:
                    if word[j] != s[i + j]:
                        is_match = False
                        break
                    else:
                        continue
            if is_match:
                results[i] = results[i + len(word)]
                if results[i]:
                    break
    return results[0]


