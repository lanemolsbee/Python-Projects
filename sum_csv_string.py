def sum_csv_string(csv_string):
    num_characters = csv_string.split(",")
    nums = []
    total = 0
    for x in num_characters:
        nums.append(int(x))
    for x in nums:
        total += x
    return total