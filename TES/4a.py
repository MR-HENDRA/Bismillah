a = int(input("nilai: "))
if a < 3:
    print("kosong")
for i in range(1,a+1):
    if i%3==0:
        print(i, end=" ")