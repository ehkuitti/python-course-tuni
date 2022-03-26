def main():
    syote = input("How do you feel? (1-10) ")

    luku = int(syote)

    # Jos arvo on alle nollan tai yli kymmenen, on kyseessä laiton input
    if luku <= 0 or luku > 10:
        print("Bad input!")

    # Jos arvo 1
    elif luku == 1:
        print("A suitable smiley would be :'(")

    # Jos arvo on 2-3
    elif luku > 1 and luku < 4:
        print("A suitable smiley would be :-(")

    #Jos arvo on 4-7
    elif luku >= 4 and luku < 8:
        print("A suitable smiley would be :-|")

    #Jos arvo on 8-9
    elif luku >= 8 and luku <= 9:
        print("A suitable smiley would be :-)")

    #Jos arvo on 10
    else:
        print("A suitable smiley would be :-D")

if __name__ == "__main__":
    main()