f = open('files.txt', 'w')
f.write('Hello, World!\n')
f.close()

f = open('files.txt')
text = f.read()
f.close()
print(text)

with open('files.txt', 'w') as f:
    f.write('Hello, my name is Igor!\n')

text = ''
for line in open('files.txt'):
    text += line

print(text)
