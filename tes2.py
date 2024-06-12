nilaiAwal = int(input("masukkan nilai awal: "))
nilaiAkhir = int(input("masukkan nilai akhir: "))
total=0
for i in range(nilaiAwal, nilaiAkhir):
    if i%2!=0:
        print(i)
        total+=i

print(total) 