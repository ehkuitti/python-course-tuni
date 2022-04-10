"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Ohjelma muuttaa parametreina annettavien sanojen alkukirjaimet isoiksi
ja muut kirjaimet pieniksi hyödyntäen Pythonin title-valmisfunktiota."""


def capitalize_initial_letters(sana):
    """Funktio muuttaa sanoja otsikoiksi. Ottaa parametrina sanan, paluttaa
    otsikkosanan."""
    sana_otsikkona = ""

    if sana == "":
        return sana

    else:
        sana_otsikkona = str.title(sana)
        return sana_otsikkona


def main():
    inputti = ""
    inputti = input("Anna sana: ")
    paluuarvo = ""
    paluuarvo = capitalize_initial_letters(inputti)

    print("Paluuarvo on: ", paluuarvo)



if __name__ == "__main__":
    main()
