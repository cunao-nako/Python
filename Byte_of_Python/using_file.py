poem = '''\
Программировать весело.
Если работа скучна,
Чтобы придать ей весёлый тон -
    используй Python!
'''

f = open('poem.txt', 'w')
f.write(poem)
f.close()

f = open('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end = '')
