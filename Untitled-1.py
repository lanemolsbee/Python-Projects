def squared_list(lst):
    import math
    row_len = int(math.sqrt(len(lst)))
    num_rows = int(len(lst) / row_len)
    twod_list = []
    while num_rows > 0:
        row_list = []
        for i in range(row_len):
            row_list.append(lst[i])
        twod_list.append(row_list)
        num_rows -= 1
    return twod_list

def get_dict(chars_list):
    occurs = {}
    for character in chars_list:
        if character not in occurs:
            occurs[character] = 1
        else:
            occurs[character] += 1
    return occurs

def main():
    print(get_dict(['a','b','c','a']))

main()