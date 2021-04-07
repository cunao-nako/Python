import random

random_number = random.randint(1, 100000)
print('\nСлучайное число (от 1 до 100000) =', random_number)

movie_list = ['Lord of the rings', 'Hobbit',
              'Star Wars', 'Witch', 'Samurai Jack',
              'Avatar: The Legend of Aang']
print('\nСписок фильмов на вечер до shuffle\'a:')
for movie in movie_list:
    print(movie)
print('\nСлучайный выбор фильма на вечер:', random.choice(movie_list))
random.shuffle(movie_list)
print('\nПосле shuffle\'a:')
for movie in movie_list:
    print(movie)
