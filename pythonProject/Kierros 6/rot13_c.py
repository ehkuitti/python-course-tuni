"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Ohjelma lukee syötettä ja lisää sitä taulukon jatkoksi niin kauan, kunnes syöte
on tyhjä merkkijono.
"""

def row_encryption(text):
    """Tämä funktio käy läpi käyttäjän syöttämää tekstiä ja salaa sitä
    käyttäen omatekemää encrypt-funktiota. Palauttaa salatun tekstin."""
    substr = ""
    text_lenght = 0

    text_lenght = len(text)

    for i in range(0, text_lenght, 1):
        substr += encrypt(text[i])

    return substr


def encrypt(char):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param char: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    char_index = 0
    encr_char = ''
    len_encr = 0
    lowercase_text = ""
    was_text_uppercase = False

    len_encr = len(encrypted_chars)

    if char.isupper():
        lowercase_text = char.lower()
        char = lowercase_text
        was_text_uppercase = True

    if char in regular_chars:
        char_index = regular_chars.index(char)
        # print("Char index: ", char_index)

    else:
        return char

    # Jos taulukon koko ei ole suurempi kuin merkin indeksi
    if char_index <= len_encr:
        encr_char = encrypted_chars[char_index]

    if was_text_uppercase:
        encr_char = encr_char.upper()

    # print("Salattu merkki: ", encr_char)
    return encr_char

    # return ...the result of encryption...

def read_message():
    """Tämä funktio lukee käyttäjän syötettä ja lisää sitä taulukon jatkeeksi.
    Funktiosta palaudutaan tyhjällä merkkijonolla tai välilyönnillä."""
    inputti = ""
    msg = ""
    substr = ""

    while True:
        inputti = input()
        if inputti == "" or inputti == " ":
            substr = row_encryption(msg)
            return substr
        msg += inputti
        msg += "\n"


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    i = 0
    msg_text = ""
    msg_shouting = ""
    msg_lenght = 0

    msg_lenght = len(msg)

    print("ROT13: ")
    print(msg, end="")


if __name__ == "__main__":
    main()
