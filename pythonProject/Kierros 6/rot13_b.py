"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Ohjelma lukee syötettä ja lisää sitä taulukon jatkoksi niin kauan, kunnes syöte
on tyhjä merkkijono.
"""


def read_message():
    """Tämä funktio lukee käyttäjän syötettä ja lisää sitä taulukon jatkeeksi.
    Funktiosta palaudutaan tyhjällä merkkijonolla tai välilyönnillä."""
    inputti = ""
    msg = []

    while True:
        inputti = input()
        if inputti == "" or inputti == " ":
            return msg
        msg.append(inputti)


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    i = 0
    msg_text = ""
    msg_shouting = ""
    msg_lenght = 0

    msg_lenght = len(msg)

    print("The same, shouting:")

    while i < msg_lenght:
        msg_text = msg[i]
        msg_shouting = msg_text.upper()
        print(msg_shouting)
        i += 1


if __name__ == "__main__":
    main()
