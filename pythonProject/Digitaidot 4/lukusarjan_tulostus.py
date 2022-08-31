print("Anna luku:")
luku = int(input())

if luku == 0:
    print(0)

elif luku == 1:
    print("1")

elif luku > 0:
    pienempi_luku = luku
    i = 0
    while i < luku:
        if pienempi_luku == 0:
            break
        print(pienempi_luku)
        pienempi_luku -= 1
        i += 1
    print(0)

elif luku < 0:
    suurempi_luku = luku
    i = 0
    while i < (luku*(-1)):
        print(suurempi_luku)
        suurempi_luku += 1
        i += 1
    print(0)
