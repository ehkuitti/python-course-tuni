"""
COMP.CS.100 Tulosteen leveyden asettaminen
Tekijä: Eetu Kuittinen
Opiskelijanumero: 150541820
"""


def main():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i * j:4}", end="")

        # Pelkkä rivinvaihto
        print()


if __name__ == "__main__":
    main()
