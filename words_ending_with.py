def words_ending_with(wordlist, tail):
    words_with_tail = []
    tail_length = len(tail)
    if tail_length == 0:
        return wordlist
    for x in wordlist:
        if x[-tail_length:] == tail:
            words_with_tail.append(x)
    return words_with_tail