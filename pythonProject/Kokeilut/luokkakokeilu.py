

class Person:

    def __init__(self, name="Person", phone_number="404",
                 address="Kuusikkotie 1, Narnia"):

        self.__name = name
        self.__phone_number = phone_number
        self.__address = address

    def printout(self):
        print("Nimi: ", self.__name)
        print("Puhelinnumero: ", self.__phone_number)
        print("Osoite: ", self.__address)


def main():

    eetu = Person()
    eetu.printout()


if __name__ == "__main__":
    main()