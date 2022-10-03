"""
COMP.CS.100 Projekti 1: Inflaatiolaskin
Tekijä: Eetu Kuittinen
Opiskelijanumero: 150541820

Ohjelma laskee inflaatiota kuukausille syötettyjen arvojen perusteella.
Syötettäviä arvoja tallennetaan kahteen muuttujaan, ja tallennuskohde
valitaan käyttämällä jakojäännöstä. Mikäli jakojäännös ei mene tasan,
tallennetaan arvo muuttujmaan 1, muuten muuttujaan 2. Inflaation määrä
lasketaan joka välissä erotuksena, ja mikäli erotus on suurempi, tallennetaan se
muuttujaan, joka pitää kirjaa suurimmasta. Siispä kaikkia käyttäjän syöttämiä
arvoja ei tarvitse pitää tallessa, koska tässä tarkastellaan vain suurinta
inflaatiota eli -erotusta.
"""


def main():

    # MUUTTUJIEN ALUSTUKSET TIETOTYYPPEINEEN AAKKOSJÄRJESTYKSESSÄ

    # Kokonaisluvut
    kuukauden_numero = 1
    suurin_erotus = 0

    # Liukuluvut
    parillinen_kuukausi = 0.0
    pariton_kuukausi = 0.0

    # Merkkijonot
    kuukauden_syote = ""

    # Totuusarvot
    onko_syote_numero = True

    while onko_syote_numero:

        # Kuukausi otetaan talteen aluksi merkkijonona, jotta voidaan
        # tarkastella syöttikö käyttäjä mitään eli onko syöte tyhjä merkkijono
        kuukauden_syote = input(f"Enter inflation rate for month "
                                f"{kuukauden_numero}: ")

        # Poikkeustapaus, jossa käyttäjä ei syöttänyt arvoa ensimmäisen tai
        # toisen kuukauden aikana
        if (kuukauden_numero < 3) and (kuukauden_syote == ""):
            print("Error: at least 2 monthly inflation rates must be entered.")

            # Suljetaan ohjelma suoraan, jottei loopin jälkeinen tulostus
            # maksimi-inflaatiosta tulostuisi
            return 1

        # Arvojen kyseleminen loppuu normaalitapauksessa käyttäjän jättäessä
        # syöttämättä arvoja
        elif kuukauden_numero >= 3 and kuukauden_syote == "":

            # Lopettaa arvojen kyselemisen lopettamalla loopin
            onko_syote_numero = False

        # Joka toinen käyttäjän syöttämä arvo tallennetaan eri muuttujaan,
        # jotta erotuslaskuja voidaan tehdä. Se, kumpoaan muuttujaan arvoja
        # tallennetaan, määrittyy nykyisen kuukauden jakojäännöksestä.
        elif kuukauden_numero % 2 == 0:
            parillinen_kuukausi = float(kuukauden_syote)

            """
            Jos nykyisten kuukausien erotus on suurempi kuin suurin
            inflaatio siihen mennessä, uudesta erotuksesta tehdään suurin
            inflaatio. Poikkeus on kuukausi 2, jolloin on ehditty antaa
            vasta yhden kerran molemmat arvot. Tällöin asetetaan suoraan
            ensimmäinen erotus suurimmaksi, koska muita erotuksia ei vielä
            ole.
            """
            if (parillinen_kuukausi - pariton_kuukausi) > suurin_erotus \
                    or kuukauden_numero == 2:
                suurin_erotus = parillinen_kuukausi - pariton_kuukausi

        elif kuukauden_numero % 2 != 0:
            pariton_kuukausi = float(kuukauden_syote)

            if (pariton_kuukausi - parillinen_kuukausi) > suurin_erotus:
                suurin_erotus = pariton_kuukausi - parillinen_kuukausi

        kuukauden_numero += 1

    # Jos kaikki arvot syötettiin onnistuneesti, tulostetaan lopullinen
    # inflaatio
    print(f"Maximum inflation rate change was {suurin_erotus:.1f} points.")


if __name__ == "__main__":
    main()
