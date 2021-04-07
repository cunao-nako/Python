import struct

packed_data = struct.pack('>i4sh', 7, b'spam', 8)

with open('byte_files.bin', 'w+b') as f:
    f.write(packed_data)
    text = f.read()
print(text)

with open('byte_files.bin', 'r+b') as f:
    text = f.read()
print(text)

text = struct.unpack('>i4sh', text)
print(text)
