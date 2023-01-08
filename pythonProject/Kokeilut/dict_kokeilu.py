"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""

# toyta {
#     malli: yaris
#     vuosi: 2009
#     moottori: bensiini
# }


def count_amount_of_a_word():

    minun_syote = ""
    minun_splitattu_syote = ""
    minun_splitattu_lista = []
    minun_sanakirja = {}
    onko_syote_kelvollinen = True

    print("Enter rows of text for word counting. Empty row to quit.")

    # Syötteen keräämistä jatketaan niin kauan, kunnes syötetään pelkkä enter
    while onko_syote_kelvollinen:

        # Kerätään syöte talteen ja splitataan välilyönnin kohdalta
        minun_syote = input()
        minun_syote_pienilla_kirjaimilla = minun_syote.lower()
        minun_splitattu_syote = minun_syote_pienilla_kirjaimilla.split()

        # Jos syötetään
        if minun_syote == "":
            onko_syote_kelvollinen = False

        # Pidentää listaa splitatuilla soluilla
        for i in range(0, len(minun_splitattu_syote), 1):
            minun_i_maara = minun_splitattu_syote.count(
                minun_splitattu_syote[i])
            minun_sanakirja[minun_splitattu_syote[i]] = minun_i_maara
            # minun_splitattu_lista.append(minun_splitattu_syote[i])

    print("My Dict", minun_sanakirja)

    print("My list", minun_splitattu_lista)


def main():

    count_amount_of_a_word()

    # my_input = ""
    # my_input_splitted = ""
    # my_list = []
    # my_dict = {}
    # amount_of_sassia = 0
    #
    # # Kerätään sanat talteen
    # my_input = input("Enter some words: ")
    #
    # # Splitatan syöte soluihin välilyönnin kohdalta
    # my_input_splitted = my_input.split()
    #
    # # Listaa pidennetään splitatuilla soluilla
    # for i in range(0, len(my_input_splitted), 1):
    #     my_list.append(my_input_splitted[i])
    #
    # # Tulostetaan lista
    # print("My list: ", my_list)
    #
    # # Lasketaan sassin määrä
    # amount_of_sassia = my_list.count("sassia")
    # print("Amount of sassia: ", amount_of_sassia)
    #
    # # Indeksi 0
    # i = 0
    #
    # # Etsitään "sassia" indeksistä i
    # my_dict[my_list[i]] = amount_of_sassia
    # print(my_dict)


if __name__ == "__main__":
    main()
