"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

TÄHÄN TULEE KUVAUS SIITÄ, MITÄ KOODITIEDOSTON OLISI TARKOITUS TEHDÄ.
"""

def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
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

    len_encr = len(encrypted_chars)

    if text in regular_chars:
        char_index = regular_chars.index(text)
        print("Char index: ", char_index)

    # Jos taulukon koko ei ole suurempi kuin merkin indeksi
    if char_index <= len_encr:
        encr_char = encrypted_chars[char_index]

    print("Salattu merkki: ", encr_char)

    # return ...the result of encryption...


def main():

    text = ""
    text = input("Input text: ")

    encrypt(text)


if __name__ == "__main__":
    main()
