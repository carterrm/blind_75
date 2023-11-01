def two_sum(input_array, target):
    check_dict = dict()
    for i in range(len(input_array)):
        if target - input_array[i] in check_dict:
            return check_dict[target-input_array[i]], i
        else:
            check_dict[input_array[i]] = i

def buy_sell_stock(prices):
    high_price = 0
    low_price = 100000
    max_profit = 0
    for price in prices:
        if price < low_price:
            low_price = price
            high_price = price
        elif price > high_price:
            high_price = price
        if high_price - low_price > max_profit:
            max_profit = high_price - low_price
    return max_profit

def contains_duplicate(nums):
    check_set = set()
    for number in nums:
        if number in check_set:
            return True
        else:
            check_set.add(number)
    return False

def product_except_self(nums):
    results = []
    #First, set prefixes
    for i in range (0, len(nums)):
        if i == 0:
            results.append(1)
        else:
            results.append(results[i - 1] * nums[i - 1])
    #define initial postfix & iterate through prefixes to calculate final values
    current_postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        results[i] *= current_postfix
        current_postfix *= nums[i]
    return results
    three = 3

def three_sum(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    solution_set = set()
    for i in range(0, len(nums) - 2):
        j = i + 1
        k = len(nums) - 1
        while(j < k):
            num_i = nums[i]
            num_j = nums[j]
            num_k = nums[k]
            sum = nums[i]+nums[j]+nums[k]
            if sum < 0:
                j += 1
            elif sum > 0:
                k -= 1
            elif sum == 0:
                solution_set.add((nums[i], nums[j], nums[k]))
                j += 1
                k -= 1

    three = 3
    results = []
    for tuple in solution_set:
        results.append(list(tuple))
    return results

        #returns a list of lists of integeres

def two_sum_II(input_array, target):
    front_pointer = 0
    rear_pointer = len(input_array) - 1
    finished = False
    while not finished:
        sum = input_array[front_pointer] + input_array[rear_pointer]
        if sum == target:
            finished = True
            break
        elif sum < target:
            front_pointer += 1
        elif sum > target:
            rear_pointer -= 1
    return [front_pointer, rear_pointer]