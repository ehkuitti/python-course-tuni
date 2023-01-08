"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Lisää numeroita listalle silloin kun ne ovat positiivisia. Tulostaa arvot
negatiivisilla indekseillä viimeisestä ensimmäiseen.
"""


def main():
    print("Give 5 numbers: ")

    i = 0
    j = 0
    luku = 0
    lista = []

    while i < 5:
        luku = int(input("Next number: "))

        lista.append(luku)
        i += 1

    print("The numbers you entered, in reverse order: ")
    for j in reversed(lista):
        print(j)


if __name__ == "__main__":
    main()
