# for i in range(1, 21):
#     print(i)


# mylist = [i for i in range(1, 1000001)]
# print(min(mylist), max(mylist), sum(mylist))


# for i in range(2, 21, 2):
#     print(i)


# mylist1 = [i for i in range(3, 30) if not i % 3]
# print(mylist1)


# mylist2 = []
# for i in range(1, 10):
#     mylist2.append(i**3)
# print(mylist2)


# mylist3 = [i**3 for i in range(1, 10)]
# print(mylist3)


# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def sit(self):
#         print(self.name.title() + ' is sitting')

#     def roll_over(self):
#         print(self.name.title() + ' rolled over')

# a = Dog('bobik', '10')
# a.sit()
# a.roll_over()


# class Car():

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometr_reading = 0

#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name

#     def read_odometr(self):
#         print('This car has ' + str(self.odometr_reading) + ' miles on it.')

#     def update_odometr(self, miles):
#         if miles >= self.odometr_reading:
#             self.odometr_reading = miles
#         else:
#             print("You can't roll odometr back")

#     def increment_odometer(self, miles):
#         self.odometr_reading += miles

#     def fill_gas_tank(self):
#         print('Топливо заканчивается, нужна заправка!')

# class Battery():

#     def __init__(self, battery_size=70):
#         self.battery_size = battery_size

#     def describe_battery(self):
#         print('This car has a ' + str(self.battery_size) + "-kWh battery.")

#     def get_range(self):
#         if self.battery_size == 70:
#             range = 240
#         elif self.battery_size == 85:
#             range = 270
#         message = 'This car can go approximately ' + str(range)
#         message += ' miles on a full charge.'
#         print(message)

# class ElectricCar(Car):

#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()

#     def describe_battery(self):
#         print('This car has a ' + str(self.battery_size) + "-kWh battery.")

#     def fill_gas_tank(self):
#         print('У электромобиля нет бензобака!')


# import json

# a = ''.join([str(i) for i in range(1, 1000001)])

# filename = 'pi.json'
# with open(filename, 'r+') as f:
#     json.dump(a, f)
#     with open(filename, 'r') as f:
#         text = json.load(f)
# print(len(text))


# file_name = 'pi.txt'
# with open(file_name, 'a') as f:
#     f.write('I also loce finding meaning in large datasets.\n')
#     f.write('I love creating creating apps that can run in a browser.\n')
# with open(file_name, 'r') as f:
#     a = f.read()
# print(a)


# try:
#     print(5/0)
# except ZeroDivisionError as error:
#     print('При делении на 0, возникает ошибка:', error)


# while True:
#     first_number = input('Введите первое число: ')
#     if first_number == 'q':
#         break
#     second_number = input('Введите второе число: ')
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print('Делить на 0 - нельзя!')
#     else:
#         print('Деление', first_number, 'на', second_number, '=', answer)


# filename = '2.txt'

# try:
#     with open(filename, 'r') as f:
#         a = f.read()
# except FileNotFoundError:
#     print('К сожалению файл "' + filename + '" не найден :(')


# import random

# filenames = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']

# print(filenames)

# a = ''
# i = 0
# for i in filenames:
#     for number in range(random.randint(1, 10000000)):
#         a += 'Word '
#     with open(i, 'w') as f:
#         f.write(a)

# def count_words_in_file(filename):
#     """Подсчёт слов в файле."""

#     try:
#         with open(filename, 'r') as f:
#             text = f.read()
#     except Exception as error:
#         # error = 'К сожалению файл: "' + filename + '" не найден.'
#         # print(error)
#         filename = 'log.txt'
#         with open(filename, 'a') as f:
#             f.write(f'{error}\n')
#     else:
#         answer = f'В файле "{filename}" {len(text)} слов'
#         print(answer)

# filenames = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt', '6.txt']

# for f in filenames:
#     count_words_in_file(f)
#     try:
#         os


# import os

# filenames = ['log.txt', '1.txt', '2.txt', '3.txt', '4.txt', '5.txt']

# for i in filenames:
#     try:
#         os.remove(i)
#     except Exception:
#         pass


# import json

# numbers = [2, 3, 4, 5, 6]
# filename = 'numbers.json'

# with open(filename, 'w') as f:
#     json.dump(numbers, f)

# with open(filename, 'r') as f:
#     content = json.load(f)

# print(content)


# import json

# username = input('Введите ваше имя: ')
# filename = 'username.json'

# with open(filename, 'w') as f:
#     json.dump(username, f)
#     print('Мы запомнили вас, "' + username + '"!')


# import json

# filename = 'username.json'

# with open(filename, 'r') as f:
#     username = json.load(f)
#     print('Мы вас заждались, "' + username + '"!')


# import json
# import os

# filename = 'username.json'

# try:
#     with open(filename, 'r') as f:
#         username = json.load(f)
#         print('Мы вас заждались, "' + username + '"!')
# except Exception:
#     username = input('Вы впервые у нас? Пожалуйста введите ваше имя: ')
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#         print('Приятно познакомиться, "' + username + '"!')

# while True:
#     comand = int(input('Выберите действие:\n(1) Назад'
#                        ' | (0) Выйти\n'))
#     if comand:
#         break
#     elif not comand:
#         try:
#             os.remove(filename)
#         except Exception:
#             pass
#         break
#     else:
#         print('Извините не понял вашей команды')


# import json
# import os


# def find_username(filename):
#     try:
#         with open(filename, 'r') as f:
#             username = json.load(f)
#     except Exception:
#         return login(filename)
#     return greetings(username)


# def login(filename):
#     username = input('Вы впервые у нас? Пожалуйста введите ваше имя: ')
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#     print('Приятно познакомиться, "' + username + '"!')


# def greetings(username):
#     print('Мы вас заждались, "' + username + '"!')


# while True:
#     filename = 'username.json'
#     find_username(filename)
#     comand = input('(0) Меню | (1) Логаут\n')
#     if comand == '0':
#         break
#     elif comand == '1':
#         try:
#             os.remove(filename)
#         except Exception:
#             pass
#         break
#     else:
#         print('Извините не понял вашей команды')

# def get_full_name(first, middle, second):
#     full_name = f'{first} {middle} {second}'
#     return full_name.title()

# first = input('Введите ваше имя: ')
# second = input('Введите вашу фамилию: ')
# print(get_full_name(first, second))
