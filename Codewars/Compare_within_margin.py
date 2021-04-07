def close_compare(a, b, margin=0):
    c = 1
    if a > b:
        c = a - b
        return 1
    elif a < b:
        c = b - a
        return -1
    elif margin >= c:
        return 0


a = int(input('Enter a: '))
b = int(input('Enter b: '))
margin = int(input('Enter margin: '))
print(close_compare(a, b, margin))
