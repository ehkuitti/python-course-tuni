KIVI = "R"
PAPERI = "P"
SAKSET = "S"

def main():

    pelaajan_1_valinta = input("Player 1, enter your choice (R/P/S): ")
    pelaajan_2_valinta = input("Player 2, enter your choice (R/P/S): ")

    # Paperi voittaa kiven, kivi voittaa sakset ja sakset voittavat paperin

    # TAPAUKSET KIVI JA PAPERI
    if pelaajan_1_valinta == PAPERI and pelaajan_2_valinta == KIVI:
        print("Player 1 won!")

    elif pelaajan_1_valinta == KIVI and pelaajan_2_valinta == PAPERI:
        print("Player 2 won!")

    # TAPAUKSET KIVI JA SAKSET
    elif pelaajan_1_valinta == KIVI and pelaajan_2_valinta == SAKSET:
        print("Player 1 won!")

    elif pelaajan_1_valinta == SAKSET and pelaajan_2_valinta == KIVI:
        print("Player 2 won!")

    # TAPAUKSET SAKSET JA PAPERI
    elif pelaajan_1_valinta == SAKSET and pelaajan_2_valinta == PAPERI:
        print("Player 1 won!")

    elif pelaajan_1_valinta == PAPERI and pelaajan_2_valinta == SAKSET:
        print("Player 2 won!")

    else:
        print("It's a tie!")


if __name__ == "__main__":
    main()
