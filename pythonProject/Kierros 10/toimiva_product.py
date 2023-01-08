"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Template for the product assignment.
"""


class Product:
    """
    This class defines a simplified product for sale in a store.
    """

    def __init__(self, name="Product", normal_price=0.00,
                 sale_percentage=0.00,
                 sale_price=0.00):

        self.__name = name
        self.__sale_price = sale_price
        self.__sale_percentage = sale_percentage
        self.__normal_price = normal_price

    def get_price(self):
        if self.__sale_percentage == 0.00:
            return self.__normal_price

        else:
            return self.__sale_price

    def set_sale_percentage(self, sale_percentage):
        self.__sale_percentage = sale_percentage
        self.__sale_price = (100 - self.__sale_percentage) / 100 \
                            * self.__normal_price
        return self.__sale_price

    def printout(self):
        print(self.__name)
        print(f"  price: {self.__normal_price:.2f}")
        print(f"  sale%: {self.__sale_percentage:.2f}")


def main():
    ################################################################
    #                                                              #
    #  You can use the main-function to test your Product class.   #
    #  The automatic tests will not use the main you submitted.    #
    #                                                              #
    #  Voit käyttää main-funktiota Product-luokkasi testaamiseen.  #
    #  Automaattiset testit eivät käytä palauttamaasi mainia.      #
    #                                                              #
    ################################################################

    test_products = {
        "milk": 1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
