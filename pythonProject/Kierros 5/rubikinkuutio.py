"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Ohjelma laskee Rubiikin kuution mestaruuskilpailuihin osallistuvien suoritusten
keskiarvoja.
"""


def main():

    i = 1
    lista = []
    arvo = 0.00

    while i < 6:
        arvo = float(input("Enter the time for performance", i, ": "))
        lista.append(arvo)
        i += 1




if __name__ == "__main__":
    main()
