a = int(input("angka: "))
b = int(input("angka: "))

c = a*b
if c % 2 == 0 and c - 3 != 0:
    d = c*2
else:
    d = c+2
print(d)