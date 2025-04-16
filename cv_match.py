def cv_match(sentence, pattern):
    words = sentence.split(" ")
    valid_words = []
    for i in range(len(words)):
        lower = words[i].lower()
        pattern_matcher = ""
        for letter in lower:
            if lower[letter] in "abcdefghijklmnopqrstuvwxyz":
                pattern_matcher += "v"
            else:
                pattern_matcher += "c"
        if pattern_matcher == pattern:
            valid_words.append(words[i])
    return valid_words
