a = int(input("nilai a: "))
b = int(input("nilai b: "))
c = int(input("nilai c: "))

d = a / c
if d.is_integer() == False:
    d += 2
    print(d)
else:
    print(d)

e = a / b
if e.is_integer() == True:
    e -= 2
    print(e)
else:
    print(e)
