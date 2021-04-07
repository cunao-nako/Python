# Задание 4: Работа со строками
# Создайте переменные, поместите в них значения - имя,
# фамилию и возраст. Выведите на экран следующее предложение:
# "Hi! My name is имя фамилия, I'm возраст years old."
# Используйте конкатенацию переменных и строк.

name = 'Igor'
surname = 'Nikonov'
age = '23'
print('Hi! my name is ' + name + ' ' + surname +
      ', I\'m ' + age + ' years old.')

# Выведите на экран текст детской песенки:
# Baa, baa, black sheep,
# Have you any wool?
# Yes sir, yes sir,
# Three bags full

# One for the master,
# One for the dame,
# And one for the little boy
# Who lives down the lane

# Baa, baa, black sheep,
# Have you any wool?
# Yes sir, yes sir,
# Three bags full
# Отступите от левого края расстояние, равное двум табуляциям.
# Выполните перенос текста на новую строку двумя способами

print("\t\tBaa, baa, black sheep,\n\t\tHave you any wool?\
      \n\t\tYes sir, yes sir,\n\t\tThree bags full"
      '''\n\t\tOne for the master,\n\t\tOne for the dame,\
            \n\t\tAnd one for the little boy Who lives down the lane
\t\tBaa, baa, black sheep,\n\t\tHave you any wool?\
      \n\t\tYes sir, yes sir,\n\t\tThree bags full''')
