def reverse(text):
    return text[::-1]

def is_palindrom(text):
    return text == reverse(text)

something = input('Введите текст: ')
if (is_palindrom(something)):
    print('Это палиндром')
else:
    print('Не палиндром')