"""
COMP.CS.100 Tehtävä päivämäärät
Tekijä: Eetu Kuittinen
Opiskelijanumero: 150541820
"""


def main():

    kuukausi = 1
    pvm = 3
    i = 1
    kolmejolaskettu = False

    while kuukausi <= 12:

        # Ensimmäisen päivän tapaus (3.1)
        if pvm == 3 and kolmejolaskettu == False:
            print(pvm, ".", kuukausi, sep="")
            kolmejolaskettu = True
            continue

        # Tapaus helmikuu
        if kuukausi == 2:
            while pvm <= 28:
                while i <= 7:
                    pvm += 1
                    i += 1

        # Tapauksissa huhtikuu, kesäkuu, syyskuu, ja marraskuu on vain 30 päivää
        elif (kuukausi == 4) or (kuukausi == 6) or (kuukausi == 9) or (kuukausi == 11):
            while pvm <= 30:
                while i <= 7:
                    pvm += 1
                    i += 1

            print(pvm, ".", kuukausi, sep="")


        # Muissa kuukausissa on 31 päivää
        else:
            while pvm <= 31:
                while i <= 7:
                    pvm += 1
                    i += 1

                print(pvm, ".", kuukausi, sep="")

        i = 1
        kuukausi += 1;


if __name__ == "__main__":
    main()