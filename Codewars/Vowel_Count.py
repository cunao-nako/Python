def get_count(input_str):
    num_vowels = 0
    input_str = list(input_str.lower())
    for i in 'aeiou':
        for symbols in input_str:
            if symbols == i:
                num_vowels += 1
    return num_vowels


a = input('')
print(get_count(a))
