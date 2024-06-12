arrayA = []
b = int(input("mau berapa: "))
for i in range(1, b+1):
    a = int(input("nilai: "))
    if a % 2 == 0:
        break
    else:
        arrayA.append(a)
print(arrayA)