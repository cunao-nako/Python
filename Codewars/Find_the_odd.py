def find_it(s):
    return max(int(i) for i in s if s.count(i) % 2)


s = input().split(',')
for i in s:
    i = int(i)
print(find_it(s))
