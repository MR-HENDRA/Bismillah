a = int(input("a: "))
b = int(input("b: "))

c = a + b

if c % 2 != 0 and c % 3 != 0:
    c += 1
    print("hasil: ", c)
else:
    c += 2
    print("hasil: ", c)
