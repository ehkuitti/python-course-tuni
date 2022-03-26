"""
COMP.CS.100 Tehtävä onko_tylsaa_2
Tekijä: Eetu Kuittinen
Opiskelijanumero: 150541820
"""

def main():

    syote = ""
    buul = True

    while buul:
        syote = input("Answer Y or N: ")

        if syote == "Y":
            buul = False

        elif syote == "y":
            buul = False

        elif syote == "N":
            buul = False

        elif syote == "n":
            buul = False

        else:
            print("Incorrect entry.")
            continue

    print("You answered", syote)


if __name__ == "__main__":
    main()