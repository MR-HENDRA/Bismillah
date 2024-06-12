arrayA = []
a = int(input("angka: "))
for i in range(1, a):
    if i % 3 == 0 and i % 7 == 0:
        arrayA.append(i)
if not arrayA:
    print("kosong")
else:
    print(arrayA)
