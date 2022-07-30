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


def command_quit():
    print("Bye bye!")
    return


def command_add(frac_dict):

    # Integers
    numerator = 0
    denominator = 0

    # Lists
    my_stripped_input = []

    # Strings
    frac_name = ""
    frac_str = ""
    my_input = ""

    print("Enter a fraction in the form integer/integer: ")
    my_input = input()

    my_splitted_input = my_input.split("/")
    numerator = int(my_splitted_input[0])
    denominator = int(my_splitted_input[1])

    frac = Fraction(numerator, denominator)
    frac_str = frac.return_string()

    print("Enter a name: ")
    frac_name = input()

    frac_dict[frac_name] = frac_str

    # TODO: Toteuta lisättävän murtoluvun nimeäminen


def command_unknown_command():
    print("Unknown command!")


def command_list(frac_dict):
    for key, payload in frac_dict.items():
        print(f"{key} = {payload}")


def command_times(frac_dict):

    # Strings
    first_operand = ""
    second_operand = ""
    simplified_str = ""
    operand_product = ""
    
    # Integers

    print("1st operand: ")
    first_operand = input()

    print("2nd operand: ")
    second_operand = input()

    if (first_operand in frac_dict) and (second_operand in frac_dict):
        
        # String-muodossa supistamatta
        operand_product = frac_dict[first_operand] * frac_dict[second_operand]
        
        split_result = operand_product.split()
        numer = int(split_result[0])
        denom = int(split_result[1])
        
        simpl_frac = Fraction(numer, denom)
        simplified_str = simpl_frac.simplify()
        
        print(f"{first_operand} * {second_operand} = {operand_product}")
        print(f"simplified {simplified_str}")
        

def command_file(frac_dict):
    pass


def main():

    # Booleans
    is_input_quit = False

    # Dictionaries
    frac_dict = {}

    # Strings
    my_input = ""

    while not is_input_quit:
        my_input = input("> ")

        # Stripataan välilyönnit, jotta komennot toimisivat oikein
        my_stripped_input = my_input.strip()

        if my_stripped_input.lower() == "quit":
            command_quit()
            is_input_quit = True

        elif my_stripped_input == "add":
            command_add(frac_dict)

        elif my_stripped_input == "list":
            command_list(frac_dict)

        elif my_stripped_input == "*":
            command_times(frac_dict)

        else:
            command_unknown_command()


if __name__ == "__main__":
    main()
