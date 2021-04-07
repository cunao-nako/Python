dict = {'apple': {'quantity': 5, 'color': 'green'}, 'lemon': {'quantity': 3, 'color': 'yellow'}}
dict['grape'] = {'quantity': 25, 'color': 'purple'}
print(dict)

dict2 = dict(zip(['name', 'job', 'age'], ['Harry', 'developer', '23']))
print(dict2)

dict3 = {'name': {'first': 'Harry', 'last': 'Nikonov'},
         'job': ['backend-developer', 'python-developer'],
         'age': 23.5}
print(dict3)

dict4 = {'b': 'b', 'a': 'a', 'd': 'd', 'c': 'c'}

for key in sorted(dict4):
    print(key, '->', dict4[key])
