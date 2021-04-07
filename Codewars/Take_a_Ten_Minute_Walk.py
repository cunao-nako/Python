from collections import Counter


def is_valid_walk(walk):
    if len(walk) > 10 or len(walk) < 10:
        return False
    else:
        n = Counter(walk)['n']
        s = Counter(walk)['s']
        w = Counter(walk)['w']
        e = Counter(walk)['e']
        if n == s and w == e:
            return True
        return False

# nsnsnsnsns True
# nnnsnsnsns False


print(is_valid_walk(input()))
