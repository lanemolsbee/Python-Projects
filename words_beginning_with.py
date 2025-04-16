def words_beginning_with(wordlist, head):
    if len(head) == 0:
        return wordlist
    head_length = len(head)
    words = []
    for x in wordlist:
        if x[0:head_length] == head:
            words.append(x)
    return words
