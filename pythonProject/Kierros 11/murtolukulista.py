"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Fractions code template
"""


class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def simplify(self):
        greatest_common = greatest_common_divisor(self.__numerator,
                                                  self.__denominator)
        self.__numerator = self.__numerator // greatest_common
        self.__denominator = self.__denominator // greatest_common
        clause = self.return_string()
        return clause

    # FI: Käänteisluku
    def reciprocal(self):
        return Fraction(self.__denominator, self.__numerator)

    # FI: Vastaluku
    def complement(self):
        return Fraction(-self.__numerator, self.__denominator)

    def multiply(self, other):
        new_numerator = self.__numerator * other.__numerator
        new_denominator = self.__denominator * other.__denominator
        return Fraction(new_numerator, new_denominator)

    def divide(self, other):
        new_numerator = self.__numerator * other.__denominator
        new_denominator = other.__numerator * self.__denominator
        return Fraction(new_numerator, new_denominator)

    def add(self, other):
        self_expanded_denominator = self.__denominator * other.__denominator
        self_numerator_sum = self.__numerator * other.__denominator + \
                            other.__numerator * self.__denominator

        # other_expanded_denominator = other.__denominator * self.__denominator
        # other_expanded_numerator = other.__numerator * self.__denominator

        return Fraction(self_numerator_sum, self_expanded_denominator)

    def deduct(self, other):
        self_expanded_denominator = self.__denominator * other.__denominator
        self_numerator_deduction = (self.__numerator * other.__denominator) - \
                                   other.__numerator * self.__denominator
        return Fraction(self_numerator_deduction, self_expanded_denominator)

    def __str__(self):
        str_return_clause = self.return_string()
        str_return_clause_simplified = self.simplify()
        return f"{str_return_clause} = {str_return_clause_simplified}"


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator are divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a


def main():

    print("Enter fractions in the format integer/integer.")
    print("One fraction per line. Stop by entering an empty line.")

    i = 0
    oma_syote = ""
    splitattu_syote = []
    lista_murtoluvuista = []

    while True:
        oma_syote = input()
        stripattu_syote = oma_syote.strip()
        if stripattu_syote == "":
            break

        splitattu_syote = oma_syote.split("/")

        osoittaja = int(splitattu_syote[0])
        nimittaja = int(splitattu_syote[1])

        murtoluku = Fraction(osoittaja, nimittaja)
        lista_murtoluvuista.append(murtoluku)

        i += 1

    print("The given fractions in their simplified form:")
    for alkio in lista_murtoluvuista:
        print(alkio)


if __name__ == "__main__":
    main()
