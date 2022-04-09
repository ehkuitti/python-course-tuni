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
    indeksi_arvolla_0 = 0
    indeksi_arvolla_miinus1 = 0
    keskiarvo = 0

    while i < 6:
        print("Enter the time for performance ", i, ": ", sep="", end="")
        arvo = float(input(""))
        lista.append(arvo)
        i += 1

    # Poistaa duplikaattiarvot listalta
    lista = list(set(lista))

    # Järjestää arvot nousevaan järjestykseen
    lista.sort()

    # print("Lista ennen alkioiden poistoa: ", lista)

    # Määritellään muuttujat arvoiltaan nimiään vastaaviksi
    del lista[0]
    del lista[-1]

    # print("Lista alkioiden poiston jäljeen: ", lista)

    # Lasketaan keskiarvo listan alkioille
    keskiarvo = sum(lista) / len(lista)

    print(f"The official competition score is {keskiarvo:.2f} seconds.")


if __name__ == "__main__":
    main()
