def array_diff(a, b):
    first = set(a)
    second = set(b)
    third = [x for x in first if x not in second]
    print(third)


array_diff([1,2,2], [2])

# ~~~~~~~~~~~~~~~~~~~~~~~~ BEST ~~~~~~~~~~~~~~~~~~~~~~~~~


def array_diff(a, b):
    return [x for x in a if x not in b]