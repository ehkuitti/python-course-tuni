"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""


def read_message():
    """Funktio lukee käyttäjän syöttämää tekstiä ja kirjoittaa sitä
    käyttäjän antamaan tiedostonimeen."""
    filename = input("Enter the name of the file: ")
    write_file = ""
    msg = []
    msg_input = ""
    msg_lenght = 0

    try:
        write_file = open(filename, mode="w")

    except OSError:
        print(f"Writing the file {filename} was not successful.")
        return

    print("Enter rows of text. Quit by entering an empty row.")

    while True:
        msg_input = input()
        if msg_input == "" or msg_input == " ":
            break
        msg.append(msg_input)

    msg_lenght = len(msg)

    for i in range(0, msg_lenght, 1):
        print(i+1, " ", sep="", end="", file=write_file)
        print(msg[i], sep="", end="", file=write_file)
        print("\n", sep="", end="", file=write_file)

    print(f"File {filename} has been written.")


def main():
    read_message()


if __name__ == "__main__":
    main()
