filename = "a.bin"
data = 12
with open(filename, "wb") as f:
    f.write(bytearray([data]))