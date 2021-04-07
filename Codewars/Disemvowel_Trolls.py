def disemvowel(string):
    banned = ('a', 'e', 'i', 'o', 'u')
    string = list(string)
    for i in banned:
        for item in string:
            if i == item:
                string.remove(item)
    string = ''.join(string)
    return string
