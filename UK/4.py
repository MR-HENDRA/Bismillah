# array = []
# a = int(input("nilai: "))
# for i in range(1, a+1):
#     if i % 3 ==0:
#         array.append(i)
# if not array:
#     print("kosong")
# print(array)

# a = int(input("nilai: "))
# if a < 3:
#     print("kosong")
# for i in range(1, a + 1):
#     if i % 3 == 0 and i % 7 == 0:
#         print(i, end=" ")

a = int(input("nilai: "))
if a < 21:
    print("kosong")
for i in range(1, a + 1):
    if i % 3 == 0 and i % 7 == 0:
        print(i, end=" ")


