"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Käy merkkijonoa läpi ja tarkistaa löytyykö käyttäjän syöttämästä sanasta
isoja kirjaimia.
"""


def main():
    konsonanttien_maara = 0
    syote = ""
    merkki = 0
    vokaali = 0
    vokaalien_maara = 0
    vokaalit = ["a", "e", "i", "o", "u", "y"]

    syote = input("Enter a word: ")

    for merkki in syote:
        if merkki in vokaalit:
            vokaalien_maara += 1
        else:
            konsonanttien_maara += 1

    print("The word \"", syote, "\" contains ", vokaalien_maara, " vowels and ",
          konsonanttien_maara, " consonants.", sep="")


if __name__ == "__main__":
    main()
