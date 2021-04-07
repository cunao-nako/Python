string = 'sp\xc4m'

with open('unicode_files.txt', 'w', encoding='utf-8') as f:
    f.write(string)

with open('unicode_files.txt', 'r', encoding='utf-8') as f:
    text = f.read()
print('text:', text, '\n', '\tДлина:', len(text))

raw_string = open('unicode_files.txt', 'rb').read()
print('raw_string:', raw_string, '\n', '\tДлина:', len(raw_string))

normal_string = raw_string.decode('utf-8')
print('normal_sting: ', normal_string, '\n', '\tДлина:', len(normal_string))

print('utf-8:', normal_string.encode('utf-8'), '\n', '\tДлина:', len(normal_string.encode('utf-8')))
print('latin-1:', normal_string.encode('latin-1'), '\n', '\tДлина:', len(normal_string.encode('latin-1')))
print('utf-16:', normal_string.encode('utf-16'), '\n', '\tДлина:', len(normal_string.encode('utf-16')))
