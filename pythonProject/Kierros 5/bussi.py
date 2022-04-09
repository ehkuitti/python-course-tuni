"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def main():
    lahtoaika = 0
    lahtoaikataulu = [630, 1015, 1415, 1620, 1720, 2000]
    lahtoaikataulun_pituus = 0

    lahtoaika = int(input("Enter the time (as an integer): "))
    lahtoaikataulun_pituus = len(lahtoaikataulu)

    lahtoaikataulu.sort()

    print("The next buses leave:")

    for indeksi in range (0, lahtoaikataulun_pituus, 1):

        if 1620 <= lahtoaika < 1720:
            print(lahtoaikataulu[4])
            print(lahtoaikataulu[5])
            print(lahtoaikataulu[0])
            break

        elif 1720 <= lahtoaika < 2000:
            print(lahtoaikataulu[5])
            print(lahtoaikataulu[0])
            print(lahtoaikataulu[1])
            break

        elif lahtoaika >= 2000:
            print(lahtoaikataulu[0])
            print(lahtoaikataulu[1])
            print(lahtoaikataulu[2])
            break

        elif lahtoaika <= lahtoaikataulu[indeksi]:
            print(lahtoaikataulu[indeksi])
            print(lahtoaikataulu[indeksi+1])
            print(lahtoaikataulu[indeksi+2])
            break
        else:
            indeksi += 1


if __name__ == "__main__":
    main()
