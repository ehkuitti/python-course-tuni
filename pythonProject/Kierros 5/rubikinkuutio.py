"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Ohjelma laskee Rubiikin kuution mestaruuskilpailuihin osallistuvien suoritusten
keskiarvoja.
"""


def main():
    arvo = 0.00
    i = 1
    lista = []
    keskiarvo = 0
    minimiarvo = 0
    maksimiarvo = 0
    minimimaara = 0
    maksimimaara = 0

    while i < 6:
        print("Enter the time for performance ", i, ": ", sep="", end="")
        arvo = float(input(""))
        lista.append(arvo)
        i += 1

    # Järjestää arvot nousevaan järjestykseen
    lista.sort()

    # Minimiarvo ja maksimiarvo talteen omiin muuttujiinsa
    # minimiarvo = min(lista)
    # maksimiarvo = max(lista)

    # minimimaara = lista.count(minimiarvo)
    # maksimimaara = lista.count(maksimiarvo)

    del lista[0]
    del lista[-1]

    # print("Summa: ", sum(lista))
    # print("Pituus: ", len(lista))

    keskiarvo = sum(lista) / 3

    print(f"The official competition score is {keskiarvo:.2f} seconds.")


if __name__ == "__main__":
    main()
