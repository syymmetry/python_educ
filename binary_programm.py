def binary_from_file(filename):
    with open(filename, "rb") as f:
        while byte := f.read(1):
            yield format(ord(byte), '08b')



filename = "example.exe"
for binary in binary_from_file(filename):
    print(binary, end=" ");
