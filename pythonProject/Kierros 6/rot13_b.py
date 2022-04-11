"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Ohjelma lukee syötettä ja lisää sitä taulukon jatkoksi niin kauan, kunnes syöte
on tyhjä merkkijono.
"""


def read_message():

    inputti = ""
    msg = []
    is_input_valid = True

    while is_input_valid:
        inputti = input()
        if inputti == "" or inputti == " ":
            is_input_valid = False
        msg += inputti

    return msg


def main():

    msg_shouting = ""
    msg_lenght = 0

    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    msg_lenght = len(msg)

    for i in range (0, msg_lenght, 1):
        msg_shouting += msg.upper([i])

    print("The same, shouting:")
    print(msg_shouting)


if __name__ == "__main__":
    main()
