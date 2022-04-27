"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""

# Globaalit muuttujat
LIIAN_LYHYT_KOMENTO = 2
LOPETUSKOMENTO = "q"
LOPETUSPALUUARVO = 1
VAADITTU_MAARA_PUOLIPISTEITA_RIVILLA = 2


def avaa_tiedosto():
    """Funktio kysyy käyttäjältä tiedostonimeä ja yrittää avata sen nimistä
    tiedostoa samasta kansiosta, jossa tämä tiedosto sijaitsee. Avauksen
    epäonnistuessa tulostetaan virhe ja ohjelma sammutetaan. Funktio ei ota
    parametrejä vastaan ja palauttaa tiedosto-olion."""

    tiedostonimi = ""

    tiedostonimi = input("Enter file name: ")

    try:
        tiedosto = open(tiedostonimi, mode="r")
        return tiedosto

    except OSError:
        print("Error opening file!")
        return LOPETUSPALUUARVO


def onko_rivilla_tarpeeksi_puolipisteita(syote):
    """Funktio tarkistaa, onko annetulla tiedostorivillä tarpeeksi
    puolipisteitä. Ottaa parametrina tiedoston yksittäisen rivin ja palauttaa
    True eli kyllä, mikäli rivillä on tarpeeksi monta puolipistettä. Muuten
    false eli ei ole."""

    puolipisteiden_maara = 0

    puolipisteiden_maara = syote.count(";")

    return puolipisteiden_maara >= VAADITTU_MAARA_PUOLIPISTEITA_RIVILLA


def poista_rivilta_ylimaaraiset_valilyonnit(rivi):
    """Funktio poistaa riviltä kaikki ylimääräiset välilyönnit (engl.
    whitespace) ja palauttaa merkkijonon, josta ne on poistettu. Parametrina
    yksittäinen tiedoston rivi."""

    rivi_ilman_valilyonteja = ""

    rivi_ilman_valilyonteja = rivi.strip()

    return rivi_ilman_valilyonteja


def pilko_listaksi(syote, erotinmerkki=" "):
    """
    Funktio ottaa parametrina jonkin käyttäjän antaman syötteen sekä
    halutun erotinmerkin. Pilkkoo syotteen Pythonin standardikirjaston
    str.split() funktiolla ja palauttaa pilkotun listan. Mikäli
    funktiokutsussa ei anneta erotinmerkkiä, käyttää erotinmerkkinä yhden
    merkin levyistä välilyöntiä.
    """

    listana = syote.split(erotinmerkki)

    return listana


def aseta_lista_alkioiden_arvot_muuttujien_arvoiksi(pilkottu_rivi,
                                                    alkiojarjestys=""):
    """Funktio ottaa parametrina vastaan toisaalla taulukoksi pilkotun rivin.
    Funktiossa luodaan muuttujat, jotka vastaavat nimiltään pilkotun rivin
    alkioista löytyviä arvoja. Nämä muuttujat alustetaan tyhjiksi
    merkkijonoiksi ja sen jälkeen päivitetään ajan tasalle listan alkioiden
    arvoilla.

    Kutsutapauksia:

    - 2 arvoa: Pilkotun rivin taulukosta löytyy vain 2 arvoa (eli sen
    pituus on 2), käytetty parametri sisältää käyttäjän syöttämän
    komentomerkin sekä laitoksen.
    - Yli 2 arvoa: Pilkottu rivi sisältää kurssin,
    laajuuden, ja laitoksen, jolloin puolestaan nämä arvot asetetaan ja
    palautetaan
    - Yli 2 arvoa, alkiojärjestys \"poikkeuksellinen\": Tässä
    poikkeustapauksessa
    kutsuja on lisäysfunktion pilkottu lista, jolloin pituus on kyllä 3,
    mutta halutut tiedot (merkki, laitos, laajuus) löytyvät eri indekseistä.
    Arvot asetetaan ajan tasalle
    ja palautetaan."""

    # MUUTTUJIEN ALUSTUKSET (MUUTTUJATYYPPEINEEN AAKKOSJÄRJESTYKSESSÄ)

    # Kokonaisluvut
    pilkotun_rivin_pituus = 0

    # Merkkijonot
    kurssi = ""
    laajuus = ""
    laitos = ""
    merkki = ""

    pilkotun_rivin_pituus = len(pilkottu_rivi)

    if pilkotun_rivin_pituus == 2:

        merkki = pilkottu_rivi[0]
        laitos = pilkottu_rivi[1]

        return merkki, laitos

    elif pilkotun_rivin_pituus > 2 and alkiojarjestys == "poikkeuksellinen":
        merkki = pilkottu_rivi[0]
        laitos = pilkottu_rivi[1]
        laajuus = pilkottu_rivi[-1]

        return merkki, laitos, laajuus

    else:

        laitos = pilkottu_rivi[0]
        kurssi = pilkottu_rivi[1]
        laajuus = pilkottu_rivi[2]

        return laitos, kurssi, laajuus


def lue_tiedosto_sanakirjaan(tiedosto):
    """Funktio ajetaan käyttäjän syötettyä tiedostonimen. Funktio käy
    annettua tiedostoa läpi ja lisää yksittäisiä rivejä sanakirjaan.
    Tiedostorivin ensimmäinen alkio on käytetty laitos, joka toimii
    hakuavaimena ko. sanakirjassa. Sen pariksi tallennetaan sanakirja,
    jonka pariksi puolestaan tallennetaan kurssin nimi (avain) sekä kurssin
    laajuus (arvo). Tilanteessa, jossa joko tiedostoa ei löydy, tai sen rivi
    on formatoitu väärin / sisältää liian vähän tietoja, funktiosta palataan
    ja ohjelma sammutetaan. Ottaa vastaan tiedosto-olion jalauttaa sanakirjan,
    jossa sanakirjan rivit. """

    # MUUTTUJIEN ALUSTUKSET (MUUTTUJATYYPEITTÄIN AAKKOSJÄRJESTYKSESSÄ)

    # Listat
    pilkottu_rivi = []

    # Merkkijonot
    erotinmerkki = ";"
    kurssi = ""
    laajuus = ""
    laitos = ""
    valilyonniton_rivi = ""

    # Sanakirjat
    opintotietokanta = {}

    # Totuusarvot
    onko_rivilla_tarpeeksi_tietoja = False

    for rivi in tiedosto:

        valilyonniton_rivi = poista_rivilta_ylimaaraiset_valilyonnit(rivi)
        onko_rivilla_tarpeeksi_tietoja = \
            onko_rivilla_tarpeeksi_puolipisteita(valilyonniton_rivi)

        if not onko_rivilla_tarpeeksi_tietoja:
            print("Error in file!")
            return LOPETUSPALUUARVO

        # Arvot on syötetiedostossa eritelty puolipisteellä, joten käytetään
        # sitä erotinmerkkiparametrina
        pilkottu_rivi = pilko_listaksi(valilyonniton_rivi, erotinmerkki)

        laitos, kurssi, laajuus = \
            aseta_lista_alkioiden_arvot_muuttujien_arvoiksi(pilkottu_rivi)

        if laitos in opintotietokanta:
            opintotietokanta[laitos][kurssi] = laajuus
        else:
            opintotietokanta[laitos] = {kurssi: laajuus}

    return opintotietokanta


def komento_tulosta_kaikki(opintotietokanta):
    """Funktio ajetaan, kun käyttäjä syöttää p-komennon mainissa. Funktio
    ottaa parametrina opintotietokannan (sanakirja, johon luettu arvot
    tiedostosta) ja käy sitä läpi. Tulostaa tekstin formatoituna ohjeistuksen
    mukaisesti. Funktio ei palauta arvoa."""

    print()

    for laitoksen_nimi, kurssin_tiedot in sorted(opintotietokanta.items()):
        print(f"*{laitoksen_nimi}*")
        for kurssin_nimi, opintopisteet in sorted(kurssin_tiedot.items()):
            print(f"{kurssin_nimi} : {opintopisteet} cr")


def komento_tulosta_laitos(komento, opintotietokanta):
    """Funktio ajetaan, kun käyttäjä syöttää r-komennon mainissa. Komennon
    mukana käyttäjä syöttää laitoksen, jonka hän haluaa tulostaa. Jos laitos
    löytyy (= ei puutu), käydään sanakirjaa läpi ja etsitään sieltä haluttu
    annettu laitos. Kun se löytyy, tulostetaan sen nimi, sekä laitoksen
    järjestämän kurssit laajuuksineen. Ottaa vastaan käyttäjän syöttämän
    komennon, sekä opintotietokannan (sanakirja, joka sisältää tiedostosta
    luetut tiedot), eikä palauta arvoa."""

    # MUUTTUJIEN ALUSTUKSET (TYYPEITTÄIN AAKKOSJÄRJESTYKSESSÄ)

    # Listat
    pilkottu_komento = []

    # Merkkijonot
    komento_laitos = ""
    komento_merkki = ""

    pilkottu_komento = pilko_listaksi(komento)

    komento_merkki, komento_laitos = \
        aseta_lista_alkioiden_arvot_muuttujien_arvoiksi(pilkottu_komento)

    if komento_laitos not in opintotietokanta:
        print("Department not found!")
        return

    print()
    for laitoksen_nimi, kurssin_tiedot in sorted(opintotietokanta.items()):
        if laitoksen_nimi == komento_laitos:
            print(f"*{laitoksen_nimi}*")
            for kurssin_nimi, kurssin_laajuus in sorted(kurssin_tiedot.items()):
                print(f"{kurssin_nimi} : {kurssin_laajuus} cr")


def komento_tulosta_opintopisteiden_maara(komento, opintotietokanta):
    """Funktiota kutsutaan mainista komennolla c. Funktio käy läpi
    opintotietokantaa, mikäli haluttu laitos löytyy, ja tulostaa halutun
    kurssin opintopisteet. Mikäli kurssia ei löydy, funktion suorittaminen
    keskeytetään. Ei palauta arvoa. """

    # MUUTTUJIEN ALUSTUKSET (MUUTTUJATYYPPEINEEN AAKKOSJÄRJESTYKSESSÄ)

    # Kokonaisluvut
    opintopisteiden_kokonaismaara = 0

    # Listat
    pilkottu_komento = []

    # Merkkijonot
    komento_laitos = ""
    komento_merkki = ""

    pilkottu_komento = pilko_listaksi(komento)

    komento_merkki, komento_laitos = \
        aseta_lista_alkioiden_arvot_muuttujien_arvoiksi(pilkottu_komento)

    if komento_laitos not in opintotietokanta:
        print("Department not found!")
        return

    for laitoksen_nimi, kurssin_tiedot in sorted(opintotietokanta.items()):
        if laitoksen_nimi == komento_laitos:
            for kurssin_nimi, opintopisteet in sorted(kurssin_tiedot.items()):
                opintopisteiden_kokonaismaara += int(opintopisteet)

    print(f"Department {komento_laitos} has to offer "
          f"{opintopisteiden_kokonaismaara} cr.")


def lisaa_arvot_listalle(laitos, tiedot_merkkijonona, laajuus):
    """Funktion lisää parametriarvot uudelle listalle ja palauttaa listan.
    Parametreinä 3 merkkijonoa: laitos, kurssin tiedot merkkijonona,
    sekä kurssin laajuus. """

    # MUUTTUJIEN ALUSTUKSET (MUUTTUJATYYPPEINEN AAKKOSJÄRJESTYKSESSÄ)

    # Listat
    lista_ilman_komentomerkkia = [laitos, tiedot_merkkijonona, laajuus]

    return lista_ilman_komentomerkkia


def komento_lisaa_laitos_tai_kurssi(komento, opintotietokanta):
    """Funktiolla voi lisätä sanakirjaan kurssin tai laitoksen. Funktio ottaa
    vastaan käyttäjän syöttämän laitoksen nimen sekä opintotietokannan (
    sanakirja), ja käy sitä läpi. Tämän lisäksi funktiosta löytyy
    alkiojärjestys-muuttuja, jolla viestitään arvojenasetusfunktiolle
    alkioiden sisällön olevan poikkeuksellissa järjestyksessä."""

    # MUUTTUJIEN ALUSTUKSET (MUUTTUJATYYPPEINEEN AAKKOSJÄRJESTYKSESSÄ)

    # Kokonaisluvut
    komennon_pituus = 0
    pilkotun_komennon_pituus = 0

    # Listat
    lista_ilman_komentomerkkia = []
    lista_kurssin_tiedoista = []

    # Merkkijonot
    alkiojarjestys = "poikkeuksellinen"
    komento_laitos = ""
    komento_merkki = ""

    pilkottu_komento = pilko_listaksi(komento)
    pilkotun_komennon_pituus = len(pilkottu_komento)

    if pilkotun_komennon_pituus == LIIAN_LYHYT_KOMENTO:
        return LOPETUSPALUUARVO

    komento_merkki, komento_laitos, komento_laajuus = \
        aseta_lista_alkioiden_arvot_muuttujien_arvoiksi(pilkottu_komento,
                                                        alkiojarjestys)

    lista_kurssin_tiedoista = pilkottu_komento[2:pilkotun_komennon_pituus]
    listan_pituus = len(lista_kurssin_tiedoista)
    kurssitiedot_merkkijonona = " ".join(lista_kurssin_tiedoista[
                                         0:listan_pituus - 1])

    lista_ilman_komentomerkkia = lisaa_arvot_listalle(komento_laitos,
                                                      kurssitiedot_merkkijonona,
                                                      komento_laajuus)

    laitos, kurssi, laajuus = \
        aseta_lista_alkioiden_arvot_muuttujien_arvoiksi \
            (lista_ilman_komentomerkkia)

    if komento_laitos in opintotietokanta:

        for laitoksen_nimi, kurssin_tiedot in sorted(opintotietokanta.items()):
            if komento_laitos == laitoksen_nimi:
                opintotietokanta[laitoksen_nimi][kurssi] = laajuus

        print(f"Added course {kurssi} to department {laitos}")

    # Jos laitos puuttuu
    else:
        opintotietokanta[laitos] = {kurssi: laajuus}
        print(f"Added department {laitos} with course {kurssi}")


def listaa_kurssin_tiedot(pilkottu_komento):
    """Funktio tekee parametrinaan saamasta listasta uuden listan,
    josta puuttuu itse komennon kirjain. Ottaa vastaan halutun komennon
    parametrina ja palauttaa listan. """

    # MUUTTUJIEN ALUSTUKSET (MUUTTUJATYYPPINEEN AAKKOSJÄRJESTYKSESSÄ)

    # Kokonaisluvut
    pilkotun_komennon_pituus = 0

    # Merkkijonot
    lista_kurssin_tiedoista = []

    pilkotun_komennon_pituus = len(pilkottu_komento)
    lista_kurssin_tiedoista = pilkottu_komento[2:pilkotun_komennon_pituus]

    return lista_kurssin_tiedoista


def komento_poista_laitos_tai_kurssi(komento, opintotietokanta):
    """Funktio poistaa käyttäjän haluaman laitoksen tai kurssin
    opintotitetokannasta. Tämä tapahtuu mainissa syöttämällä d + laitos tai
    d + laitos + kurssi. Käy opintotietokantaa (sanakirja) läpi ja
    löytäessään sieltä halutun laitoksen tai kurssin poistaa sen
    sanakirjasta. Ei palauta arvoa. """

    # MUUTTUJIEN ALUSTUKSET (MUUTTUJATYYPEITTÄIN AAKKOSJÄRJESTYKSESSÄ)

    # Kokonaisluvut
    pilkotun_komennon_pituus = 0

    # Listat
    pilkottu_komento = []
    laitos_ja_kurssin_tiedot = []

    # Merkkijonot
    alkiojarjestys = "poikkeuksellinen"
    komento_merkki = ""
    komento_laitos = ""

    pilkottu_komento = pilko_listaksi(komento)
    pilkotun_komennon_pituus = len(pilkottu_komento)

    if pilkotun_komennon_pituus == 2:
        komento_merkki = pilkottu_komento[0]
        komento_laitos = pilkottu_komento[1]

    elif pilkotun_komennon_pituus > 2:
        komento_merkki = pilkottu_komento[0]
        komento_laitos = pilkottu_komento[1]
        komento_merkki = pilkottu_komento[2]

    if pilkotun_komennon_pituus == 2:

        # 2 sanan tapaus, jossa haluttua laitosta ei löydy sanakirjasta
        if komento_laitos not in opintotietokanta:
            print(f"Department {komento_laitos} not found!")
            return

        # 2 sanan tapaus, jossa haluttua laitos löytyy sanakirjasta
        else:
            for laitoksen_nimi in opintotietokanta:

                if laitoksen_nimi == komento_laitos:
                    opintotietokanta.pop(komento_laitos)
                    print(f"Department {laitoksen_nimi} removed.")
                    return

    # Kurssin laajuus löytyy viimeisestä indeksistä
    komento_laajuus = pilkottu_komento[-1]

    lista_kurssin_tiedoista = listaa_kurssin_tiedot(pilkottu_komento)
    listan_pituus = len(lista_kurssin_tiedoista)

    aseta_lista_alkioiden_arvot_muuttujien_arvoiksi(pilkottu_komento,
                                                    alkiojarjestys)

    # Tehdään kurssin tiedoista merkkijono, jotta niitä voidaan käsitellä
    # myöhemmin lista-alkioina halutun syotteen mukaisesti
    kurssin_tiedot_merkkijonona = " ".join(lista_kurssin_tiedoista)

    # Lisätään arvot listalle ja päivitetään muuttujat ajan tasalle
    laitos_ja_kurssin_tiedot.append(komento_laitos)
    laitos_ja_kurssin_tiedot.append(kurssin_tiedot_merkkijonona)
    laitos = laitos_ja_kurssin_tiedot[0]
    kurssin_nimi = laitos_ja_kurssin_tiedot[1]

    if komento_laitos not in opintotietokanta:
        print(f"Department {laitos} not found!")

    elif kurssin_nimi in opintotietokanta[laitos]:
        del opintotietokanta[laitos][kurssin_nimi]
        print(f"Department {laitos} course {kurssin_nimi} "
              f"removed.")
        # for laitos_avain, kurssi in opintotietokanta.items():
        #     if kurssi == kurssin_nimi:

    else:

        print(f"Course {kurssin_nimi} from {laitos} not found!")


def main():
    # MUUTTUJIEN ALUSTUKSET (MUUTTUJATYYPPEITTÄIN AAKKOSJÄRJESTYKSESSÄ)

    # Merkkijonot
    komento = ""
    paluuarvo = ""

    # Sanakirjat
    opintotietokanta = {}

    # Totuusarvot
    onko_syotetty_lopetuskomento = False

    tiedosto = avaa_tiedosto()
    if tiedosto == LOPETUSPALUUARVO:
        return

    opintotietokanta = lue_tiedosto_sanakirjaan(tiedosto)
    if opintotietokanta == LOPETUSPALUUARVO:
        return

    komento_splitattuna = komento.split()

    while not onko_syotetty_lopetuskomento:
        print()
        print("[A]dd / [C]redits / [D]elete / [P]rint all / p[R]int "
              "department / [Q]uit")
        komento = input("Enter command: ")

        if komento[0].lower() == "p":
            komento_tulosta_kaikki(opintotietokanta)

        elif komento[0].lower() == "c":
            komento_tulosta_opintopisteiden_maara(komento, opintotietokanta)

        elif komento[0].lower() == "r":
            komento_tulosta_laitos(komento, opintotietokanta)

        elif komento[0].lower() == "a":
            paluuarvo = komento_lisaa_laitos_tai_kurssi(komento,
                                                        opintotietokanta)
            if paluuarvo == LOPETUSPALUUARVO:
                print("Invalid command!")

        elif komento[0].lower() == "d":
            komento_poista_laitos_tai_kurssi(komento, opintotietokanta)

        elif komento == LOPETUSKOMENTO:
            print("Ending program.")
            return

        else:
            print("Invalid command!")
            print()

    return


if __name__ == "__main__":
    main()
