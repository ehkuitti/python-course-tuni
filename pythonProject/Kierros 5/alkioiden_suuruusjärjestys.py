"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Ohjelma käy läpi arvoja ja palauttaa boolean-tyyppisen arvon sen perusteella,
ovatko kaikki listan alkiot samoja vaiko eivät. Tyhjällä arvolla palautetaan
True.
"""


def is_the_list_in_order(lista=[]):
    """Tutkii, ovatko kaikki lista-alkiot samoja vertaamalla alkiota i
    indeksin 0 alkioon."""

    are_items_in_ascending_order = False

    # Tyhjän- tai yksialkioisen listan erikoistapaus
    if len(lista) == 0 or len(lista) == 1:
        are_items_in_ascending_order = True
        return are_items_in_ascending_order

    else:
        one_greater_than_index = lista[1]
        lenght_of_the_list = len(lista)

        for item in range (0, lenght_of_the_list, 1):
            if one_greater_than_index > lenght_of_the_list:
                break
            elif lista[item] < lista[one_greater_than_index] \
                    and item == lenght_of_the_list-1:
                one_greater_than_index += 1
                are_items_in_ascending_order = True
            else:
                pass

    return are_items_in_ascending_order


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

    return_value = is_the_list_in_order(lista)
    # print(return_value)


if __name__ == "__main__":
    main()
