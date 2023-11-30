import sys


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

def maximum_subarray(nums):
    max_sum = -100000
    current_sum = 0
    for num in nums:
        if current_sum < 0:
            current_sum = 0
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

def maximum_product_subarray(nums):
    #Gonna be honest, I do not know how this works. This is from Neetcode's solution video, and even after watching that
    #and stepping through the list it's still a little nebulous to me. This one does work, though- all my thoughts
    #and my (almost) correct solution can be found below "return res"
    res = max(nums)
    curMin, curMax = 1, 1

    for n in nums:
        if n == 0:
            curMax, curMin = 1, 1
            continue
        temp = n * curMax
        curMax = max(n * curMin, temp, n)
        curMin = min(n * curMin, temp, n)
        res = max(res, curMax)
    return res

    # as you go through the array, keep track of where the first negative is. If you find a second negative to cancel it out, erase that marker.
    # also keep track of zeroes
    # If there's a marker on the board at the end, calculate the product of its prefix & its postfix. Take whichever is larger.
    # If there's no marker on the board at the end, the entire array is the answer
    if len(nums) == 1:
        return nums[0]
    #If there's an odd number of negatives, do you have to pivot around all of them? Just the first & last one?
    max_product = -15
    current_product = 1
    first_negative_index = -1
    last_negative_index = -1
    negative_flag = -1
    for i in range(0, len(nums)):

        if nums[i] < 0:
            last_negative_index = i
            if negative_flag == -1:
                negative_flag = i
            else: negative_flag = -1
            if first_negative_index == -1:
                first_negative_index = i

        current_product *= nums[i]
        if current_product > max_product:
            max_product = current_product
        if current_product == 0:
            current_product = 1
    if negative_flag > -1:
        front_product = maximum_product_subarray(nums[0:negative_flag])
        rear_product = maximum_product_subarray(nums[negative_flag + 1:len(nums)])
        return front_product if front_product > rear_product else rear_product
    return max_product


    negative_index = -1
    for i in range(0, len(nums)):
        if nums[i] < 0:
            if negative_index == -1:
                negative_index = i
            else:
                negative_index = -1
    if negative_index != -1:
        front_product = 1
        for i in range(0, negative_index):
            front_product *= nums[i]
        rear_product = 1
        for i in range(negative_index + 1, len(nums)):
            rear_product *= nums[i]
        if front_product >= rear_product:
            return front_product
        else: return rear_product

def search_rotated_array(nums:list[int], target:int) -> int:
    #Beats 82.84% on runtime, 74.05% on memory
    left = 0
    right = len(nums) - 1
    center = 0
    #While number is not found:
    while left <= right:
        center = (right + left) // 2
        if nums[center] == target:
            return center

        if nums[left] <= nums[center]:
            if target < nums[left] or target > nums[center]:
                left = center + 1
            else:
                right = center - 1
        else:
            if target > nums[right] or target < nums[center]:
                right = center - 1
            else:
                left = center + 1
    return -1

    #example = [11,12,13,0,1,2,3,4,5,6,7,8,9]


def find_minimum_in_rotated_sorted_array(nums: list[int]) -> int:
    #Beats 89.68% on runtime, 58.21% on memory
    if len(nums) == 1:
        return nums[0]
    left = 0
    right = len(nums) - 1
    if nums[left] < nums[right]:
        return nums[left]

    while left < right:
        center = (right + left) // 2
        if nums[center] > nums[right]:
            #You're in the left-hand half of the array
            left = center + 1
        elif nums[center] < nums[right]:
            #you're in the right-hand half
            if nums[center - 1] < nums[center]:
                #you're in the right-hand half of the right-hand half
                right = center
            else:
                return nums[center]
    if left == right:
        return nums[left]


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

    # Chat GPT's solution- much faster:
    # if len(nums) < 3:
    #         return []
    #
    #     nums.sort()
    #     results = []
    #
    #     for i in range(len(nums) - 2):
    #         if i > 0 and nums[i] == nums[i - 1]:
    #             continue
    #
    #         j = i + 1
    #         k = len(nums) - 1
    #
    #         while j < k:
    #             total = nums[i] + nums[j] + nums[k]
    #             if total < 0:
    #                 j += 1
    #             elif total > 0:
    #                 k -= 1
    #             else:
    #                 results.append([nums[i], nums[j], nums[k]])
    #
    #                 # To avoid duplicates
    #                 while j < k and nums[j] == nums[j + 1]:
    #                     j += 1
    #                 while j < k and nums[k] == nums[k - 1]:
    #                     k -= 1
    #
    #                 j += 1
    #                 k -= 1
    #
    #     return results


def container_with_most_water(height: list[int]) -> int:
    #Beats 98.79% on runtime, 19.17% on memory
    if len(height) == 2:
        return min(height[0], height[1])
    def calculate_area():
            return min(height[right], height[left]) * (right - left)

    left = 0
    right = len(height) - 1
    max_area = calculate_area()
    while left < right:
        if height[left] <= height[right]:
            #move left
            interim_left = left
            while height[left] >= height[interim_left] and interim_left < right:
                interim_left += 1
                #Update left when you've found a higher left boundary
            left = interim_left
            max_area = max(max_area, calculate_area())
        else:
            #move right
            interim_right = right
            while height[right] >= height[interim_right] and left < interim_right:
                interim_right -= 1
            right = interim_right
            max_area = max(max_area, calculate_area())
    return max_area



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

