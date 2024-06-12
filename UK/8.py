a = []
for i in range(10):
    b = input("input: ")
    a.append(b)
print(a)

print(a[1])
print(a[7])
print(a[-1])

print(a)
a.pop(4)
a.pop(8)
print(a)

a[2]="finish"
print(a)