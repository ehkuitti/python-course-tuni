"""
The first example of a home made class.
"""


class Person:
    """
    This class models a person with a simple electronic wallet.
    """

    def __init__(self, name, initial_money, address, old_address="tie"):
        """
        A person object is initialized with the name and
        the initial amount of money in the wallet.

        :param name: str, the name of the person whose
            spending the object is following.
        :param initial_money: float, how much money will
            there be in the wallet at the point of creation.
        """

        self.__name = name
        self.__money = initial_money
        self.__address = address
        self.__oldaddress = old_address

    def printout(self):
        """
        When a person's data is needed to be printed on
        screen this method will handle it.  Also good
        for debugging and testing purposes.
        """

        if not (self.__address == self.__oldaddress):
            print("—" * 25)
            print("Name:   ", self.__name)
            print("Wealth: ", self.__money)
            print("Address:", self.__address)

        self.__oldaddress = self.__address

    def add_money(self, amount):
        """
        It is possible to add money in the electronic wallet.

        :param amount: float, the amount of money added.

        :return: True if operation successfull, False otherwise.
        """

        if amount < 0.0:
            return False
        else:
            self.__money += amount
            return True

    def make_payment(self, price):
        """
        When making a payment, money needs to be
        deducted from the person's wallet.

        :param price: float, the price of the purchase
            i.e. how much money to deduct from the wallet.
        """

        if price < 0.0:
            print("The price can't be negative.")
        elif price > self.__money:
            print("You can't afford that.")
        else:
            self.__money -= price

    def move(self, address):

        # onko_osoite_sama = False

        # if address == self.__address:
        #     onko_osoite_sama = True

        self.__address = address

        # if not onko_osoite_sama:
        self.printout()


def main():
    # Let's create an object of type Person, name it denzil,
    # and use to spy on Prof. Dexter's spending.
    person = Person("Dave", 0.0, "Vaajakatu 5")

    # State of Denzil
    person.printout()

    # Denzil moves out of a dormitory to a place of his own.
    person.move("Iidesranta 3")
    person.move("Iidesranta 3")

    person.move("Pyykkiojankatu 2")
    person.move("Pyykkiojankatu 2")


if __name__ == "__main__":
    main()
