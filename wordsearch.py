def text_to_dictionary(file_name):
    file = open(file_name, "r")
    values = {}
    for line in file:
        words = line.strip("\n")
        for x in words:
            if x not in values:
                backwards_string = ""
                i = len(x) - 1
                while i >= 0:
                    backwards_string += x[i]
                    i -= 1
                values[x] = backwards_string
    return values
