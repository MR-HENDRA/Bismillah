def gajian (SKS):
    SKSStandar = 4
    pajak = 10/100
    hargaSKS = 500000
    gajiKotor= SKS*hargaSKS
    tPajak = 0

    selisih = SKS - SKSStandar

    if selisih >= SKSStandar:
        tPajak = gajiKotor*pajak

    penghasilan = gajiKotor-tPajak
    print(pajak)
    print(selisih)
    print(tPajak)
    print(penghasilan)

SKS = int(input("nilai: "))
gajian(SKS)
