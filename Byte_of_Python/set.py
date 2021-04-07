bri = set(['Бразилия', 'Россия', 'Индия'])
if 'Индия' in bri:
    print('1', True)
if 'USA' in bri:
    print('2', True)
bric = bri.copy()
bric.add('Китай')
if bric.issuperset(bri):
    print('3', True)
bri.remove('Россия')
print(bri & bric)