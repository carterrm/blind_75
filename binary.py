import sys


def number_of_1_bits(n):
    #Neetcode's faster solution
    result = 0
    while n > 0:
        n = n & (n-1)
        result += 1
    return result
    #Needcode's slower solution
    # result = 0
    # while n > 0:
    #     if n % 2 == 1:
    #         result += 1
    #     n = n >> 1
    # return result

def counting_bits(n):
    #neetcode full DP solution
    result_array = []
    result_array.append(0)
    if n == 0:
        return result_array

    offset = 1
    counter = 0
    for i in range(1, n + 1):
        result_array.append(1 + result_array[i - offset])
        if result_array[i] == 1:
            offset *= 2
    return result_array

    #My solution, using partial Dynamic Programming & partial reuse of number_of_1_bits code
    # result_array = []
    # for i in range (0, n + 1):
    #     iteration_result = 0
    #     j = i
    #     while j > 0:
    #         if len(result_array) > j:
    #             iteration_result =  (result_array[j] + iteration_result)
    #             break
    #         j = j & (j - 1)
    #         iteration_result += 1
    #     result_array.append(iteration_result)
    #
    # return result_array