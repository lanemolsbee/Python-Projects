def max_consec_sum(numbers, n):
    sum = 0
    for i in range(0, n):
        sum += numbers[i]
    return sum
