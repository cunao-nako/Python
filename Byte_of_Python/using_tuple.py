zoo = ('питон', 'слон', 'пингвин')
print('Количество зверей в зоопарке -', len(zoo))
new_zoo = 'обезьяна', 'верблюд', zoo
print('Количество клеток в зоопарке -', len(new_zoo))
print('Все животные в новом зоопарке:', new_zoo)
print('Все животные привезеднные из старого зоопарка:', new_zoo[2])
print('Последнее животное привезенное из старого зоопарка -', new_zoo[2][2])
print('Количество животных в новом зоопарке -', len(new_zoo) - 1 + len(zoo))
