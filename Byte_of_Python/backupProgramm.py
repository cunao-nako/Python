#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
import os
import sys
import time
print('_' * 90, '\n')
print('\nДобро пожаловать в backup-программу!\n')
print('_' * 90, '\n')
print('_' * 90, '\n')
print('Для выхода нажмите Ctrl + C!')
print('_' * 90, '\n')
print('_' * 90, '\n')
print('Для справки введите "help"!')
print('_' * 90, '\n')
print('\n')
os.system('ls')
print('\n')
while True:
    path = ['/Users']
    path.append('/igor')
    while True:
        print('_' * 90, '\n')
        inp = input('Выберите путь к объекту для его сохранения --> ')
        print('_' * 90, '\n')
        if inp == '':
            break
        if 'help' in inp:
            print('\n', '~' * 90)
            print('\nls - показать содержимое текущей директории' \
                  '\n<Имя_директории> - перекод к <Имя_директории>' \
                  '\n.. - перекод к предыдущей директории'
                 )
            print('\n', '~' * 90, '\n')
            continue
        if 'ls' in inp:
            print('\n')
            os.system(inp)
            print('\n')
        elif '..' in inp:
            os.chdir(inp)
            del(path[-1])
            print('\n')
            os.system('ls')
            print('\n')
        else:
            os.chdir(inp)
            path.append(inp)
            print('\n')
            os.system('ls')
            print('\n')
    source = path[0] + '/'
    for item in path[1:]:
        source += item + '/'
    target_dir = '/Users/igor/Documents/Backup/'
    today = target_dir + os.sep + time.strftime('%d:%m:%y',)
    now = time.strftime('%H:%M:%S')
    print('_' * 90, '\n')
    comment = input('Введите коментарий --> ')
    print('_' * 90, '\n')
    if len(comment) == 0:
        target = today + os.sep + now + '.zip'
    else:
        target = today + os.sep + now + '_' + \
            comment.replace(' ', '_') + '.zip'
    if not os.path.exists(today):
        os.mkdir(today)
        print('Каталог успешно создан!')
    zip_command = "zip -qr {0} {1}" .format(target, source)
    if os.system(zip_command) == 0:
        print('_' * 90, '\n')
        print('Резервная копия создана в', target)
        print('_' * 90, '\n')
        break
    else:
        print('_' * 90, '\n')
        print('Создание резервной копии не удалось')
        print('_' * 90, '\n')