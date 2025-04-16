def concat_elements(slist, startpos, stoppos):
    concat_string = ""
    if startpos < 0:
        for x in range(len(slist)):
            concat_string += x
    elif startpos >= len(list):
        for i in range(startpos, len(slist)):
            concat_string += slist[i]
    else:
        for i in range(startpos, stoppos + 1):
            concat_string += str(slist[i])
    return concat_string
                    