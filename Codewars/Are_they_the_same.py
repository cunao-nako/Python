def comp(a1, a2):
    if isinstance(a2, list) and isinstance(a1, list):
        return set([i * i for i in a1]) == set(a2)
    else:
        return False


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
