"""
COMP.CS.100 Tehtävä opintopistelaskuri
Tekijä: Eetu Kuittinen
Opiskelijanumero: 150541820
"""


# Ohjelmassa käyttämäni lyhenne str tulee sanasta String eli merkkijono


def main():
    # Flag-tyyliset muuttujat
    i = 1
    jarjestysnumero = 1
    onko_kuukausia_vahintaan_kaksi = False
    onko_vastaus_ollut_nolla = False
    onko_kuukausia_liian_vahan = False

    # Arvojen säilyttäjät
    keskiarvo = 0.0
    nykyinen_kuukausi = 0.0
    opintopisteiden_maara_kuussa = 0.0
    opintopisteet_yhteensa = 0
    seuraava_kuukausi = 1.0

    str_kuukaudet = input("Enter the number of months: ")
    kuukausien_maara = int(str_kuukaudet)
    if kuukausien_maara >= 2.0:
        onko_kuukausia_vahintaan_kaksi = True
    else:
        onko_kuukausia_liian_vahan = True

    for i in range(0, kuukausien_maara):

        print("Enter the number of credits in month ", jarjestysnumero, ":", sep="", end=' ')
        str_opintopisteet = input("")
        opintopisteiden_maara_kuussa = int(str_opintopisteet)
        if opintopisteiden_maara_kuussa == 0:
            onko_vastaus_ollut_nolla = True

        if onko_kuukausia_vahintaan_kaksi and (nykyinen_kuukausi >= 1):
            if i % 2 == 0:
                seuraava_kuukausi = opintopisteiden_maara_kuussa
                opintopisteet_yhteensa += seuraava_kuukausi
            else:
                nykyinen_kuukausi = opintopisteiden_maara_kuussa
                opintopisteet_yhteensa += nykyinen_kuukausi

            if nykyinen_kuukausi + seuraava_kuukausi == 0:
                print("You did have too many study breaks!")
                break

        i += 1
        nykyinen_kuukausi += 1
        seuraava_kuukausi += 1
        jarjestysnumero += 1

    keskiarvo = opintopisteet_yhteensa / i

    if onko_kuukausia_liian_vahan:
        print(f'\nYour monthly credit point average {keskiarvo:.1f} does not classify you as a full time student.')

    elif onko_vastaus_ollut_nolla:
        print(f'\nYour monthly credit point average {keskiarvo:.1f} does not classify you as a full time student.')

    else:
        print(f'\nYou are a full time student and your monthly credit point average is {keskiarvo:.1f}')


if __name__ == "__main__":
    main()
