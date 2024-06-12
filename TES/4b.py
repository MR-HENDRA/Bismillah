a = int(input("nilai: "))
if a < 21:
    print("kosong")
for i in range(1, a+1):
    if i%3 == 0 and i%7 == 0:
        print(i, end=" ")