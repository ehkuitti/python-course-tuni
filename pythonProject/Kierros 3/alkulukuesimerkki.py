"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 0123456
Name:   Olli Opiskelija
Email:  olli.opiskelija@tuni.fi

Tämä ohjelma tulostaa näytölle alkulukuja
haluttuun lukuun saakka.
"""

def main():
    maksimi_luku = int(input("Syötä suurin tutkittava arvo: ")) # Muuttaa syötteen suoraan kokonaisluvuksi
    print("Syötit:", maksimi_luku)

    for tutkittava_luku in range(2, maksimi_luku+1):
        onko_alkuluku = True

        for jakaja in range(2, tutkittava_luku):
            if tutkittava_luku % jakaja == 0:
                onko_alkuluku = False

        print()


if __name__ == "__main__":
    main()

