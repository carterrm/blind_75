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