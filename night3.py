a = int(input("nilai: "))

ganjil = 0
genap = 0

for i in range(a+1):
    if i%2 ==0:
        genap+=i
    else:
        ganjil+=i
print(genap)
print(ganjil)