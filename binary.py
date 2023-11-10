import sys


def number_of_1_bits(n):
    #Neetcode's faster solution
    result = 0
    while n > 0:
        n = n & (n-1)
        result += 1
    return result
    #Needcode's slower solution
    result = 0
    while n > 0:
        if n % 2 == 1:
            result += 1
        n = n >> 1
    return result