# Задание 11: Sets
# Создайте множество при помощи функции set() из текста,
# чтобы получить уникальные символы, содержащиеся в тексте.
# Присвойте результат переменной. Выведите переменную на экран.
# Выведите тип значения переменной на экран.
# При необходимости найдите информацию в интернете

text = 'Apple Inc. is an American multinational technology company \
headquartered in Cupertino, California, that designs, develops \
and sells electronics, computer software, and online services. \
It is considered one of the Big Tech technology companies, alongside \
Amazon, Google, Microsoft, and Facebook.'
text = set(text)
print(type(text), '\n', text)
