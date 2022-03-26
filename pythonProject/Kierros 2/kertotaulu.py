"""
COMP.CS.100 Tehtävä onko_tylsaa_2
Tekijä: Eetu Kuittinen
Opiskelijanumero: 150541820
"""

def main():
    syote = input("Choose a number: ")

    numero = int(syote)

    i = 1;

    while True:
        tulos = i * numero
        print(i, "*", numero, "=", tulos)
        if tulos > 100:
            break
        else:
            i += 1


if __name__ == "__main__":
    main()
