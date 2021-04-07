addressbook = { 
    'Swaroop' : 'swaroop@swaroopch.com',
    'Larry' : 'larry@wall.org',
    'Matsumoto' : 'matz@ruby-lang.org',
    'Spammer' : 'spamer@hotmail.com'
}
print("Адресс Swaroop'a:", addressbook['Swaroop'])
del addressbook['Swaroop']
print('\nВ адресной книге', len(addressbook), 'контакта\n')
for name, address in addressbook.items():
    print('Контакт', name, 'с адресом', address)
addressbook['Guido'] = 'guido@python.org'
if 'Guido' in addressbook:
    print('\nАдресс Guido:', addressbook['Guido'])