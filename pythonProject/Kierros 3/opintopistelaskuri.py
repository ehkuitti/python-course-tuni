"""
COMP.CS.100 Tehtävä opintopistelaskuri
Tekijä: Eetu Kuittinen
Opiskelijanumero: 150541820
"""


# Ohjelmassa käyttämäni lyhenne str tulee sanasta String eli merkkijono. Tämä on itseäni selkeyttämään, sillä taustani
# on ohjelmointikielissä, joissa muuttujatyyppi on esiteltävä sitä määriteltäessä


def main():
    # Flag
    onko_opintoja_liian_vahan = False

    # Arvojen säilyttäjät, alustetaan liukuluvuiksi
    edellisen_kuukauden_pisteet = 0.0
    pisteet_yhteensa = 0.0
    nykyisen_kuukauden_pisteet = 0.0
    opintopisteiden_maara_tassa_kuussa = 0.0
    keskiarvo = 0.0

    # Kysytään kuukaudet
    str_kuukaudet = input("Enter the number of months: ")
    # Muunetaan kuukaudet kokonaisluvuksi
    kuukausien_maara = int(str_kuukaudet)

    for i in range(1, kuukausien_maara + 1):

        print("Enter the number of credits in month ", i, ":", sep="", end=' ')
        str_opintopisteet = input("")
        opintopisteiden_maara_tassa_kuussa = int(str_opintopisteet)
        pisteet_yhteensa += opintopisteiden_maara_tassa_kuussa

        # Ensimmäisessä kuussa molempien arvoiksi asetetaan nykyiset kysytyt opintopisteet
        if i == 1:
            edellisen_kuukauden_pisteet = opintopisteiden_maara_tassa_kuussa
            nykyisen_kuukauden_pisteet = opintopisteiden_maara_tassa_kuussa

        # Toisella kierroksella ei kosketa edellisiin, vaan vain nykyiset korvataan
        elif i == 2:
            nykyisen_kuukauden_pisteet = opintopisteiden_maara_tassa_kuussa

        # Edellisen kuukauden pisteisiin siirretään se arvo, joka oli edellisellä kierroksella nykyisen kuukauden
        # pisteissä. Tämän jälkeen nykyisen arvo päivitetään ajan tasalle
        else:
            edellisen_kuukauden_pisteet = nykyisen_kuukauden_pisteet
            nykyisen_kuukauden_pisteet = opintopisteiden_maara_tassa_kuussa

        # Erisuuri estää tilanteen, jossa ensimmäisellä kierroksella nollan syöttäminen lopettaisi ohjelman.
        # Muuten kuukaudet lasketaan yhteen, ja jos summa on nolla, niin molemmat arvot olivat nollia. Tällöin ohjelma
        # suljetaan heti returnilla
        if i != 1 and edellisen_kuukauden_pisteet + nykyisen_kuukauden_pisteet == 0:
            print("\nYou did have too many study breaks!")
            return

        i += 1

    keskiarvo = pisteet_yhteensa / kuukausien_maara

    if keskiarvo < 5.0:
        print(f'\nYour monthly credit point average {keskiarvo:.1f} does not classify you as a full time '
              f'student.')

    else:
        print(f'\nYou are a full time student and your monthly credit point average is {keskiarvo:.1f}.')


if __name__ == "__main__":
    main()
