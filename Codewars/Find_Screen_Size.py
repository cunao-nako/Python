def find_screen_height(width, ratio):
    resolution = ''
    resolution += str(width) + 'x'
    a = list(ratio.split(':'))
    height = (width / int(a[0])) * int(a[1])
    height = int(height)
    return resolution + str(height)
    # return resolution + [' '.join((width*(int(i))).split()) for i in ratio if not i == ':']


print(find_screen_height(1024, "4:3"))
