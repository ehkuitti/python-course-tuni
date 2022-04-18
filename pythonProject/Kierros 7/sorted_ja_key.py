"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Template for sorting by price assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15, "pizza": 4.15,
}


def main():
    sortattu_lista = []
    sortattu_dict = {}

    # LAMBDA-SORTTI SELITETTY

    # Järjestää nousevaan järjestykseen sanakirjan yksittäisen parin arvon
    # mukaan. Tämä vastaa parin indeksiä 1. Jos siis suluissa olisi 0,
    # järjestäisi parin avaimen mukaan nousevaan järjestykseen.
    #
    # Merkit ennen kaksoispistettä ovat funktiolle annettavat parametrit.
    # Funktio on lambda-funktio eli anonyymi funktio; sillä ei ole nimeä. Sen
    # nimi EI MYÖSKÄÄN OLE "LAMBDA", vaan tämä avainsana vain kertoo,
    # että seuraava funktio on anonyymi. Kaksoispisteen jälkeen tulee
    # paluuarvo sekä suluissa indeksi tässä tapauksessa. Järjestys on sama,
    # mutta sulut riippuvat siitä, minkälaista tietorakennetta käsitellään.
    sortattu_lista = sorted(PRICES.items(), key=lambda x: x[1])

    sortattu_dict = dict(sortattu_lista)

    sortatun_dictin_pituus = len(sortattu_dict)

    for avain, arvo in sortattu_dict.items():
        print(f"{avain} {arvo:.2f}")

    # print(sortattu_dict)

if __name__ == "__main__":
    main()
