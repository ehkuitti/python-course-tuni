"""
COMP.CS.100 Tehtövö tulosteen_tarkkuus
Tekijä: Eetu Kuittinen
Opiskelijanumero: 150541820
"""


def main():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{(i * j):>4}",
                  end="")  # Kertoo, että normaali leveys on 4 merkkiä. Jos menee yli, lisää välilyöntejä
            # niin kauan, että leveys on sopiva


if __name__ == "__main__":
    main()
