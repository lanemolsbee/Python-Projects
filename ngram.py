def ngram(arglist, startpos, length):
    ngram_list = []
    for i in range(startpos, length + 1):
        ngram_list.append(arglist[i])
    return ngram_list