"""
COMP.CS.100 Tehtävä opintopistelaskuri
Tekijä: Eetu Kuittinen
Opiskelijanumero: 150541820
"""


# Ohjelmassa käyttämäni lyhenne str tulee sanasta String eli merkkijono


def main():
    # Flag-tyyliset muuttujat
    kierrosluku = 1
    onko_opintoja_liian_vahan = False

    # Arvojen säilyttäjät
    edellisen_kuukauden_pisteet = 0.0
    pisteet_yhteensa = 0.0
    nykyisen_kuukauden_pisteet = 0.0
    opintopisteiden_maara_tassa_kuussa = 0.0
    keskiarvo = 0.0

    str_kuukaudet = input("Enter the number of months: ")
    kuukausien_maara = int(str_kuukaudet)

    for i in range(1, kuukausien_maara+1):

        print("Enter the number of credits in month ", kierrosluku, ":", sep="", end=' ')
        str_opintopisteet = input("")
        opintopisteiden_maara_tassa_kuussa = int(str_opintopisteet)
        pisteet_yhteensa += opintopisteiden_maara_tassa_kuussa

        if kierrosluku == 1:
            edellisen_kuukauden_pisteet = opintopisteiden_maara_tassa_kuussa
            nykyisen_kuukauden_pisteet = opintopisteiden_maara_tassa_kuussa

        elif kierrosluku == 2:
            nykyisen_kuukauden_pisteet = opintopisteiden_maara_tassa_kuussa

        else:
            edellisen_kuukauden_pisteet = nykyisen_kuukauden_pisteet
            nykyisen_kuukauden_pisteet = opintopisteiden_maara_tassa_kuussa

        if kierrosluku != 1 and edellisen_kuukauden_pisteet + nykyisen_kuukauden_pisteet == 0:
            print("You did have too many study breaks!")
            break

        i += 1
        kierrosluku += 1

    keskiarvo = pisteet_yhteensa / kuukausien_maara

    if keskiarvo < 5.0:
        print("\n")
        print(f'Your monthly credit point average {keskiarvo:.1f} does not classify you as a full time '
              f'student.')

    else:
        print("\n")
        print(f'\nYou are a full time student and your monthly credit point average is {keskiarvo:.1f}.')


if __name__ == "__main__":
    main()
