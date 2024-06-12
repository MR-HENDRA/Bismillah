diskon = 20 / 100

barang = 200_000
barang2 = barang - (barang * diskon)
selisih = abs(barang - barang2)
print(barang)
print(barang2)

if barang > barang2:
    print(
        "barang awal lebih besar daripada barang setelah diskon dengan selisih: ",
        selisih,
    )
elif barang < barang2:
    print(
        "barang setelah diskon lebih besar daripada barang awal dengan selisih: ",
        selisih,
    )
else:
    print("samaharga")
