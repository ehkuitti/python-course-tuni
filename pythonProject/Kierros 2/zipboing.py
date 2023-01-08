"""
COMP.CS.100 Tehtävä onko_tylsaa_2
Tekijä: Eetu Kuittinen
Opiskelijanumero: 150541820
"""
def main():
    syote = input("How many numbers would you like to have? ")
    maara = int(syote)
    luku = 1

    for luku in range (luku, maara+1):
        if (luku % 7 == 0) and (luku % 3 == 0):
            print("zip boing")
            luku+=1
        elif luku % 7 == 0:
            print("boing")
            luku+=1
        elif luku % 3 == 0:
            print("zip")
            luku+=1
        else:
            print(luku)
            luku+=1

if __name__ == "__main__":
    main()