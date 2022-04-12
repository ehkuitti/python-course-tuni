"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Ohjelma ideana on laskea käyttäjän syöttämille arvoille keskiarvoja ja medi-
aaneja. Käyttäjä syöttää haluamansa päivien määrän ja antaa jokaisen päivän
kohdalla jonkin kokonaislukuarvon (myös negatiiviset arvot sallittu, kuten läm-
pötiloissa yleensä). Ohjelma laittaa luvut taulukkoon ja tekee niillä em. las-
kuoperaatiot omissa funktioissaan. Kaikki funktiot palauttavat aina arvot mai-
nille, joka huolehtii ohjelman viemisestä eteenpäin. Main tallentaa aina paluu-
arvot muuttujiin, jotta niiden arvoja voitaisiin käyttää myös muissa funktiois-
sa tarpeen niin vaatiessa. Jokainen funktio, joka palauttaa arvon (poislukien
Pythonin automaattinen None returnin puuttuessa), otetaan talteen mainissa.
"""


def laske_mediaanin_alittavat_arvot(paivalista,
                                    paivien_maara,
                                    mediaani,
                                    keskiarvo):
    """Funktio ottaa parametreina listan, johon päivät on tallennettu; päi-
    vien määrän; mediaanin; sekä keskiarvon. Käy läpi arvoja listan arvoja
     for-loopissa, tarkistaa onko arvo indeksissä pienempi kuin mediaani.
     Tulostaa eron keskiarvoon sekä päivän järjestysnumeron (indeksi + 1). For-
     loop pyörii niin (listan koko - 1) asti, sillä indeksointi alkaa 0:sta."""

    # MUUTTUJIEN ALUSTUKSET (AAKKOSJÄRJESTYKSESSÄ)
    pienempi_kuin_mediaani = 0
    ero_keskiarvoon = 0

    print("")
    print("Under median were: ")
    for paiva in range(0, paivien_maara, 1):
        if paivalista[paiva] < mediaani:
            pienempi_kuin_mediaani += 1
            ero_keskiarvoon = mediaani - keskiarvo
            print("Day  ", paiva + 1, ".  ", paivalista[paiva],
                  "C difference to mean:  ",
                  paivalista[paiva], "C", sep="")


def laske_mediaanin_ylittavat_ja_yhtasuuret_arvot(paivalista,
                                                  paivien_maara,
                                                  mediaani,
                                                  keskiarvo):
    """Funktio ottaa parametreina listan, johon päivät on tallennettu; päi-
    vien määrän; mediaanin; sekä keskiarvon. Käy läpi arvoja listan arvoja
     for-loopissa, tarkistaa onko arvo indeksissä suurempi tai yhtäsuuri
     kuin mediaani. Tulostaa eron keskiarvoon sekä päivän järjestysnumeron
     (indeksi + 1). For-loop pyörii niin (listan koko - 1) asti, sillä
     indeksointi alkaa 0:sta."""

    # MUUTTUJIEN ALUSTUKSET (AAKKOSJÄRJESTYKSESSÄ)
    yli_tai_yhtasuuri_kuin_mediaani = 0
    ero_keskiarvoon = 0

    print("Keskiarvo: ", keskiarvo)

    print("")
    for paiva in range(0, paivien_maara, 1):
        if paivalista[paiva] >= mediaani:
            yli_tai_yhtasuuri_kuin_mediaani += 1
            ero_keskiarvoon = mediaani - keskiarvo
            print("Day  ", paiva + 1, ".  ", paivalista[paiva],
                  "C difference to "
                  "mean:   ",
                  paivalista[paiva], "C", sep="")


def onko_arvo_pariton(arvo):
    """Funktion tarkoituksena on tarkistaa, onko annettu arvo pariton. Tämä
    tehdään jakamalla arvo kahdella ja tutkimalla jääkö jakojäännöstä, ts.
    meneekö jako tasan. Mikäli jako ei mene tasan, palauttaa Truen, jolloin lu-
    ku on pariton. Muussa tapauksessa polauttaa Falsen, jolloin luku
    on parillinen. """

    return arvo % 2 > 0


def laske_mediaani(paivalista, paivien_maara):
    """Funktio laskee mediaanin annetuista arvoista. Ottaa parametreina vastaan
    paivalistan (jossa arvot tallessa) sekä päivien määrän (kokonaisluku).
    Funktiossa käytetään listan käsittelyyn nousevaan järjestykseen sortattua
    listan kopiota, jotta mediaanilaskut menevät oikein. Tähän EI käytetä
    .sort():tiam, jotta voidaan laskea keskiarvon ero mediaanin myöhemmin
    ohjelmassa. Palauttaa lasketun mediaanin.

    Mediaanin laskeminen:
    - Jos alkioita on pariton määrä, mediaani on paivat_pienimmasta_suurimpaan
      listan keskimmäinen alkio
    - Jos parillinen, se on kahden keskimmäisen arvon keskiarvo.
    """

    # MUUTTUJIEN ALUSTUKSET (AAKKOSJÄRJESTYKSESSÄ)
    paivat_pienimmasta_suurimpaan = sorted(paivalista)
    keskimmaisten_keskiarvo = 0
    mediaani = 0
    parillinen_keskimmainen_arvo_1 = 0
    parillinen_keskimmainen_arvo_2 = 0
    pariton_keskimmainen_arvo = 0

    # Pariton määrä arvoja
    if onko_arvo_pariton(paivien_maara):

        # Keskimmainen sijaitsee taulukon puolivälissä
        pariton_keskimmainen_arvo = (paivien_maara // 2)
        mediaani = paivat_pienimmasta_suurimpaan[pariton_keskimmainen_arvo]

    # Parillinen määrä arvoja
    else:

        # Otetaan muuttujiin talteen kaksi keskimmäistä arvoa sekä niiden
        # keskiarvo
        parillinen_keskimmainen_arvo_1 = (paivien_maara // 2) - 1
        parillinen_keskimmainen_arvo_2 = (paivien_maara // 2)
        keskimmaisten_keskiarvo = (paivat_pienimmasta_suurimpaan
                                   [parillinen_keskimmainen_arvo_1] +
                                   paivat_pienimmasta_suurimpaan
                                   [parillinen_keskimmainen_arvo_2]) / 2
        mediaani = keskimmaisten_keskiarvo

    return mediaani


def laske_keskiarvo(paivalista, paivien_maara):
    """Funktio ottaa parametrinä listan, jossa käsiteltävät arvot ovat, sekä
    päivien määrän. Keskiarvo lasketaan jakamalla alkioiden summa niiden mää-
    rällä. Palauttaa keskiarvot mainille. """

    # MUUTTUJIEN ALUSTUKSET (AAKKOSJÄRJESTYKSESSÄ)
    lista_alkioiden_summa = 0
    keskiarvo = 0
    paivataulukon_pituus = len(paivalista)

    for indeksi in range(0, paivataulukon_pituus, 1):
        lista_alkioiden_summa += paivalista[indeksi]

    keskiarvo = lista_alkioiden_summa / paivien_maara
    return keskiarvo


def onko_arvo_negatiivinen_tai_nolla(arvo):
    """Funktio tutkii, onko käyttäjän syöttämä arvo negatiivinen tai nolla.
    Mikäli on, palauttaa arvon True, ts. on negatiivinen tai nolla;
    muuten palauttaa arvon False, ts. ei ole."""
    return arvo <= 0


def kay_paivat_lapi(paivien_maara):
    """Funktio ottaa parametrinä vastaan käyttäjän mainissa syöttämän päivien
    määrän. Funktio tallentaa käyttäjän i:nnen päivän lämpötilan (liukuluku)
    listalle, joka alustetaan tyhjänä. Palauttaa valmiin listan sekä päivien
    määrän. Poikkeustilanteessa, jossa käyttäjä on syöttänyt nollan tai
    pienemmän arvon, palauttaa kaksi nollaa."""

    # MUUTTUJIEN ALUSTUKSET (AAKKOSJÄRJESTYKSESSÄ)
    nykyinen_paiva = 0
    paivalista = []
    tyhja_taulukko = []

    # Jos käyttäjä syöttää 0 tai vähemmän päiviä, ohjelman suoritus keskeytyy
    # mainissa.
    if onko_arvo_negatiivinen_tai_nolla(paivien_maara):
        return 0, 0

    for paiva in range(1, paivien_maara + 1, 1):
        print("Enter day ", paiva, ". temperature in Celsius: ",
              sep="", end="")
        nykyinen_paiva = float(input())
        paivalista.append(nykyinen_paiva)

    return paivalista, paivien_maara

    # print("Päästiin tänne for-loopin jälkeen")
    # print("Listan arvot", paivalista)


def main():
    """Mainin tehtävänä on huolehtia kaikkien muiden funktioiden kutsumisesta.
    Jokainen yksittäinen toiminto on oma funktionsa ohjelman rakenteen
    selkeyttämiseksi. Main myös tallentaa käy_päivät_läpi -funktion paluuarvot
    taulukkoon, jonka indekseistä 0 ja 1 ne otetaan käyttöön. Käy_päivät_läpi
    -funktion palauttaessa arvot 0 ja 0 (käyttäjän syötettyä nollan tai
    sitä pienemmän luvun, ohjelman suoritus keskeytetään)."""

    # MUUTTUJIEN ALUSTUKSET (AAKKOSJÄRJESTYKSESSÄ)
    keskiarvo = 0
    mediaani = 0
    paivalista = []
    paivien_maara = 0
    tiedot_paivista = []

    paivien_maara = int(input("Enter amount of days: "))

    # Funktion paluuarvot otetaan talteen taulukkoon
    tiedot_paivista = kay_paivat_lapi(paivien_maara)

    # Jos taulukon 1. ja 2. indeksi ovat nollia, ohjelma suljetaan
    if tiedot_paivista[0] == 0 and tiedot_paivista[1] == 0:
        return

    # Mainin muuttujat päivitetään ajan tasalle käy_päivät_läpi funktion pa-
    # lauttamien arvojen perusteella
    paivalista = tiedot_paivista[0]
    paivien_maara = tiedot_paivista[1]

    keskiarvo = laske_keskiarvo(paivalista, paivien_maara)
    print("")
    print(f"Temperature mean: {keskiarvo:.1f}C")
    mediaani = laske_mediaani(paivalista, paivien_maara)
    print(f"Temperature median: {mediaani:.1f}C")
    laske_mediaanin_ylittavat_ja_yhtasuuret_arvot(paivalista,
                                                  paivien_maara,
                                                  mediaani,
                                                  keskiarvo)
    laske_mediaanin_alittavat_arvot(paivalista,
                                    paivien_maara,
                                    mediaani,
                                    keskiarvo)


if __name__ == "__main__":
    main()
