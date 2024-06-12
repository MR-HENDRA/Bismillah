a = []
while True:
    b = int(input("nilai: "))
    a.append(b)
    print(a)
    total = 0
    for i in a:
        total+=i
    print(total)