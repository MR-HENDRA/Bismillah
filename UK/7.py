# def KJM(SKS):
#     gajiperSKS = 500000
#     standar = 4
#     pajak = 10/100
#     gajiKotor = gajiperSKS*SKS
#     tp = 0
#     if SKS > standar:
#         tp = pajak*gajiKotor
#     gajiBersih = gajiKotor - tp
#     print(tp)
#     print(gajiBersih)
# SKS = int(input("nilai: "))
# KJM(SKS)


def KJM(posisi, SKS):
    gajiperSKS = 500000
    standarPajak = 4
    pajak = 11 / 100
    SKSStandar = 0
    # SKSLebih = SKS - SKSStandar
    gajiKotor = gajiperSKS * SKS
    tp = 0
    if posisi == "lektor":
        SKSStandar = 6
        SKSLebih = SKS - SKSStandar
        if SKSLebih >= standarPajak:
            tp = pajak * gajiKotor
    elif posisi == "ahli":
        SKSStandar = 8
        SKSLebih = SKS - SKSStandar
        if SKSLebih >= standarPajak:
            tp = pajak * gajiKotor
    gajiBersih = gajiKotor - tp
    # print(gajiKotor)
    # print(SKSLebih)
    # print(tp)
    print(gajiBersih)


SKS = int(input("SKS: "))
posisi = input("Posisi: ")
KJM(posisi, SKS)
