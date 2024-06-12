a = int(input("nilai: "))
b = int(input("nilai: "))
c = int(input("nilai: "))

d = a/c
if a % c !=0:
    d+=2
e = a/b
if a % b ==0:
    e-=2

print(d)
print(e)