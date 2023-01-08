"""WHILE ELSE näyttäisi toimivan. En kylläkään ymmärrä, miten tämä eroaa
siitä, että koko elsen poistaisi, koska koodi ei kuitenkaan ohita whilea kuin
vain silloin, kun ehto ei täyty."""


def main():
    luku = 1
    i = 0
    while luku < 3:
        print("Luku on suurempi kuin kolme!")
        luku += 1
        i += 1
    else:
        print("Eipä ollu!")


if __name__ == "__main__":
    main()
