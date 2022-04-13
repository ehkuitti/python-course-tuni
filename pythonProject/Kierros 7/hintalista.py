"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():

    syote = ""
    stripattu_syote = ""

    while True:
        syote = input("Enter product name: ")

        if syote == "" or syote == " " or syote == "  ":
            print("Bye!")
            break

        elif syote not in PRICES:
            stripattu_syote = syote.strip()
            print("Error:", stripattu_syote, "is unknown.")

        else:
            print("The price of ", syote, " is ", sep="", end="")
            print(PRICES[syote], "e")


if __name__ == "__main__":
    main()
