def square_digits(number):
    mylist = []
    mylist1 = []
    a = number % 10
    mylist.append(a)
    print(mylist)
    a = number // 10 % 10
    mylist.append(a)
    print(mylist)
    a = number // 100 % 10
    mylist.append(a)
    print(mylist)
    a = number // 1000 % 100
    mylist.append(a)
    print(mylist)
    print(mylist)
    mylist = mylist[::-1]
    print(mylist)
    for i in mylist:
        c = i ** 2
        c = str(c)
        mylist1.append(c)
    print(mylist1)
    a = (''.join(mylist1))
    a = int(a)
    return a


print(square_digits(9119))
