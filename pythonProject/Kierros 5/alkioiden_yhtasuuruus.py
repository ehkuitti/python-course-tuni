"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Ohjelma käy läpi arvoja ja palauttaa boolean-tyyppisen arvon sen perusteella,
ovatko kaikki listan alkiot samoja vaiko eivät. Tyhjällä arvolla palautetaan
True.
"""


def are_all_members_same(lista=[1, 3, 2]):
    """Tutkii, ovatko kaikki lista-alkiot samoja vertaamalla alkiota i
    indeksin 0 alkioon."""

    are_all_the_same = True

    if len(lista) == 0 or len(lista) == 1:
        return are_all_the_same

    else:
        item_in_index_0 = lista[0]

        for item in lista:
            if item_in_index_0 != item:
                are_all_the_same = False

    return are_all_the_same


def main():
    value1 = 0
    value2 = 0
    value3 = 0
    value4 = 0
    value5 = 0
    lista = []
    return_value = False

    value1 = int(input("Input value 1: "))
    lista.append(value1)
    value2 = int(input("Input value 2: "))
    lista.append(value2)
    value3 = int(input("Input value 3: "))
    lista.append(value3)
    value4 = int(input("Input value 4: "))
    lista.append(value4)
    value5 = int(input("Input value 5: "))
    lista.append(value5)

    return_value = are_all_members_same(lista)
    # print(return_value)


if __name__ == "__main__":
    main()
