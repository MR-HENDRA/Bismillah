a = int(input("nilai: "))
genap = 0
ganjil = 0
for i in range(1, a+1):
    if i % 2 == 0:
        genap+=i
    else:
        ganjil+=i
print(genap)
print(ganjil)