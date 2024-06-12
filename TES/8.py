ab = []
for i in range (10):
    a = input("nilai: ")
    ab.append(a)

print(ab)
print(ab[1])
print(ab[7])
print(ab[-1])
print(ab)
print(ab.pop(4))
print(ab.pop(8))
print(ab)
ab[2] = "update"
print(ab)