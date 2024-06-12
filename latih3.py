r = 7
s = 10

luas_persegi = s**2
luas_lingkaran = ((r**2)*(22 / 7))
print(luas_persegi)
print(luas_lingkaran)
selisih = abs(luas_persegi - luas_lingkaran)
if luas_persegi > luas_lingkaran:
    print("luas persegi lebih besar daripada luas lingkaran dengan selisih: ", selisih)
elif luas_persegi < luas_lingkaran:
    print("luas persegi lebih kecil daripada luas lingkaran dengan selisih: ", selisih)
else:
    print("luas sama")
