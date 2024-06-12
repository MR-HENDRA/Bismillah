a = int(input("nilai: "))
for i in range(1, a + 1):
    print("*" * i)

# output:
# nilai: 5
# *
# **
# ***
# ****
# *****

b = int(input("nilai: "))
for i in range(b, 0, -1):
    print("*" * i)

# output:
# nilai: 5
# *****
# ****
# ***
# **
# *

c = int(input("nilai: "))
for i in range(1, c + 1):
    for j in range(c):
        print("*", end=" ")
    print()

# output:
# nilai: 5
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

d = int(input("nilai: "))
for i in range(1, d + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

# output:
# nilai: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

e = int(input("nilai: "))
for i in range(e, 0, -1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

# output:
# nilai: 5
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

f = int(input("nilai: "))
for i in range(1, f + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# output:
# nilai: 5
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

g = int(input("nilai: "))
for i in range(g, 0, -1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

# output:
# nilai: 5
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

h = int(input("nilai: "))
for i in range(1, h + 1):
    for j in range(h):
        print(i, end=" ")
    print()

# output:
# nilai: 5
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5

z = int(input("nilai: "))
for i in range(1, z + 1):
    for j in range(1, z + 1):
        print(j, end=" ")
    print()

# output:
# nilai: 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
