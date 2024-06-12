def gajian(SKS, posisi):
    pajak = 11/100
    hargaSKS = 500000
    SKSStandar = 0
    SKSStandarPajak = 4
    tPajak = 0
    gajiKotor = SKS*hargaSKS

    if posisi == "lektor":
        SKSStandar = 6
        SKSLebih = SKS - SKSStandar
        if SKSLebih >= SKSStandarPajak:
            tPajak = pajak*gajiKotor
    elif posisi == "ahli":
        SKSStandar = 8
        SKSLebih = SKS - SKSStandar
        if SKSLebih >= SKSStandarPajak:
            tPajak = pajak*gajiKotor
    penghasilan = gajiKotor - tPajak
    print(gajiKotor)
    print(SKSLebih)
    print(tPajak)
    print(penghasilan)

SKS = int(input("SKS: "))
posisi = input("posis: ").lower()

gajian(SKS, posisi)
