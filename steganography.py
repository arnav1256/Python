with open('steganography.jpg', 'ab') as f:
    f.write(b'some text idk')
    f.close()
with open('steganography.jpg', 'rb' ) as f:
    f.seek(f.read().index(bytes.fromhex('FFD9'))+2)
    print(f.read())
    f.close()
