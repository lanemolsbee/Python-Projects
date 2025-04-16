def text_to_list(file_name):
    file = open(file_name, "r")
    words_list = []
    for line in file:
        words = line.strip("\n").split()
        for x in words:
            if x not in words_list:
                words_list.append(x)
    return words_list

def count_words(word_list):
    word_counts = {}
    for x in word_list:
        if x not in word_counts:
            word_counts[x] = 1
        else:
            word_counts[x] += 1
    return word_counts

def most_frequent(word_counts):
    small_words = []
    medium_words = []
    large_words = []
    for key in word_counts:
        if 0 <= len(word_counts[key]) and len(word_counts[key]) <= 4:
            small_words.append(key)
        elif 5 <= len(word_counts[key]) and len(word_counts[key]) <= 7:
            medium_words.append(key)
        elif 8 <= len(word_counts[key]):
            large_words.append(key)
    min_small_count = 0
    min_medium_count = 0
    min_large_count = 0
    most_frequent_small = None
    most_frequent_medium = None
    most_frequent_large = None
    for key in word_counts:
        if word_counts[key] in small_words and word_counts[key] > min_small_count:
            most_frequent_small = key
        elif word_counts[key] in medium_words and word_counts[key] > min_medium_count:
            most_frequent_medium = key
        elif word_counts[key] in large_words and word_counts[key] > min_large_count:
            most_frequent_large = key
    return most_frequent_small, most_frequent_medium, most_frequent_large

def count_capitalized(word_counts):
    keys = word_counts.keys()
    unique_capitalized = 0
    unique_lowercase = 0
    for x in keys:
        if x[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            unique_capitalized += 1
        else:
            unique_lowercase += 1
    return unique_capitalized, unique_lowercase

def count_punctuated(word_counts):
    punctuated = 0
    not_punctuated = 0
    keys = word_counts.keys()
    for x in keys:
        if x[len(x)-1] in "!?\"\';:.,)":
            punctuated += 1
        else:
            not_punctuated += 1
    return punctuated, not_punctuated

def write_results(word_counts, file_name):
    file = open(file_name, "w")
    file.write("Total number of unique words:" + )




