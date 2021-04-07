mylist = []
mylist.append('item')
print(repr(mylist))
print(eval(repr(mylist)))
print(eval(repr(mylist)) == mylist)
