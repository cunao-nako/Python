from collections import Counter


def find_uniq(arr):
    for key, value in Counter(arr).items():
        if value == min(Counter(arr).values()):
            return key
