"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def main():
    filename = input("Enter the name of the file: ")

    # Koodirivit, joiden suorituksessa saattaa tapahtua virhe, sijoitetaan
    # try-lohkon sisään:
    try:

        # Yritetään avata tiedosto luettavaksi, ja mikäli se onnistuu,
        # open palauttaa tietovirran (tiedostoa kuvaavan arvon), jonka avulla
        # tiedostoa voidaan käysittellä myöhemmin ohjelmassa.
        file = open(filename, mode="r")

    # Jos edeltävän try lohkon sisällä tapahtui virhe, se voidaan käsitellä
    # except-lohkon avulla. OSError on Pythonissa virhetilanne, joka johtuu
    # siitä,m että Python pyysi käyttöjärjestelmältä jotain operaatiota,
    # joka epäonnistui. Esimerkiksi tiedoston avaaminen open-funktiolla
    # saattaa epäonnistuia käyttöjärjestelmätasolla -> OSError.

    except OSError:
        print("There was an error in reading the file.")

    i = 1
    for file_line in file:

        # Kun tiedostosta luetaan rivi, se sisältää myös tiedostossa rivin
        # perässä olleen rivinvaihtomerkin. Jos ei haluta seuraavaan
        # print-kutsun tulostavan ylimääräisiä tyhjiä rivejö, turha rivi
        # voidaan poistaa merkkijonon lopusta rstrip-metodilla.
        file_line = file_line.rstrip()

        print(i, " ", sep="", end="")
        print(file_line)

        i += 1

    # Kun tiedosto on käsitelty loppuun, se kannattaa sulkea close-metodilla.
    file.close()


if __name__ == "__main__":
    main()
