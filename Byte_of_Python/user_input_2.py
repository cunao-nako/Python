def reverse(text):
    return text[::-1]

def isPalindrom(text):
    return text == reverse(text)

inp = input('Введите строку: ')
string = (inp.upper())
symbols = ['.', ',', '?', '!', ':', ' ', '\n']
for symbol in symbols:
    if symbol in string:
        string = string.replace(' ', '')
if (isPalindrom(string)):
    print('Палиндром')
else:
    print('Не палиндом')