"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Ohjelma lukee syötettä ja lisää sitä taulukon jatkoksi niin kauan, kunnes syöte
on tyhjä merkkijono.
"""


def row_encryption(viestilista):
    """Tämä funktio käy läpi käyttäjän syöttämää tekstiä ja salaa sitä
    käyttäen omatekemää encrypt-funktiota. Palauttaa salatun tekstin."""
    substr = ""
    tekstin_pituus = 0
    sisalto_indeksissa_i = ""
    salattu_taulukko = []
    splitattu_pilkun_kohdalta = ""
    splitattu_valilyonnin_kohdalta = ""
    i = 0

    while i < len(viestilista):
        substr += viestilista[i]
        print("Substr:", substr)
        i += 1

    tekstin_pituus = len(viestilista)

    for i in range(0, tekstin_pituus, 1):
        sisalto_indeksissa_i = encrypt(viestilista[i])
        substr += sisalto_indeksissa_i
        salattu_taulukko.append(substr)

        # print("Terveiset row_encryptionista", i, ":n kerran")
        # substr += encrypt(viestilista[i])

    return salattu_taulukko


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
    msg = []
    salatun_tekstin_taulukko = []

    while True:
        inputti = input()
        if inputti == "" or inputti == " ":
            # row_encryption() ottaa vastaan viestiLISTAN
            salatun_tekstin_taulukko = row_encryption(msg)
            return salatun_tekstin_taulukko
        msg.append(inputti)
    # return msg


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    i = 0
    msg_sisalto_indeksissa = ""
    msg_rot13 = ""
    msg_pituus = 0

    msg_pituus = len(msg)

    print("ROT13: ")

    while i < msg_pituus:
        msg_sisalto_indeksissa = msg[i]
        msg_rot13 = msg_sisalto_indeksissa.upper()
        print(msg_rot13)
        i += 1


if __name__ == "__main__":
    main()
