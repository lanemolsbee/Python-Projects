def times_k(L, k):
    return [L[i] * k for i in range(len(L))]

def kth_elements(L, k):
    return [L[i] for i in range(len(L)) if i % k == 0]
def times_i(L):
    return [L[i] * i for i in range(len(L))]
def first_matches_last(L):
    return [L[i] for i in range(len(L)) if\
    (len(L[i])) != 0 and (L[i][0] == L[i][-1])\
    or L[i] == ""]