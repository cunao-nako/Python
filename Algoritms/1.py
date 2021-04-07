# session = {}
# session['cart'] = {
#     'pen': 1,
#     'pencil': 2,
#     'notebook': 3,
#     }

# print(session['cart']['pen'])

# for keys in session['cart']:
#     print(session['cart'][keys])
#     session['cart'][keys] += 1
#     session['cart'] = session['cart']
# print(session['cart'])

menu = ['pen', 'pencil', 'notebook']
session = {}
session['cart'] = {menu[i]: i for i in range(3)}
print(session['cart'])

for i in range(len(session['cart'])):
    a = {i: session['cart'][i] for i in session['cart']}
print(a)
# [{'name': 'pen'}, {'name': 'pencil'}, {'name': 'notebook'}]
