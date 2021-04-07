import random

list_of_ten_random_ints = [random.randint(1, 100000) for i in range(10)]
for i in list_of_ten_random_ints:
    print(i)

list_of_ten_dictionarys = [{i: random.randint(1, 100)} for i in range(10)]
for i in list_of_ten_dictionarys:
    print(i)
