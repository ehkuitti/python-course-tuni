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
    """This command is run when the user inputs the word quit. It prints the
    decided message and returns to the main program.  """
    print("Bye bye!")
    return


def command_add(frac_dict):
    """
    The user inputs a fraction to be added to a dictionary. Then the user
    chooses a name for the fraction. The fraction gets added to a dictionary
    as a pair. The key will be the name and the payload will be the fraction.
    """

    # Integers
    numerator = 0
    denominator = 0

    # Lists
    my_stripped_input = []

    # Strings
    frac_name = ""
    frac_str = ""
    my_input = ""

    my_input = input("Enter a fraction in the form integer/integer: ")

    my_splitted_input = my_input.split("/")
    numerator = int(my_splitted_input[0])
    denominator = int(my_splitted_input[1])

    frac = Fraction(numerator, denominator)
    frac_str = frac.return_string()

    frac_name = input("Enter a name: ")

    frac_dict[frac_name] = frac_str

    # TODO: Toteuta lisättävän murtoluvun nimeäminen


def command_unknown_command():
    """This function prints an error message when the user inputs a command
    which doesn't exist. """
    print("Unknown command!")


def command_list(frac_dict):
    """This command acts essentially as a print command. It iterates over a
    dictionary and prints its contents in the desired format."""
    for key, payload in sorted(frac_dict.items()):
        print(f"{key} = {payload}")


def command_times(frac_dict):
    """This command multiplies two values by input. The program seeks for
    these values in the dictionary and does the calculation if found."""

    # Strings
    first_operand = ""
    first_fraction = ""
    second_fraction = ""
    second_operand = ""
    simplified_str = ""
    operand_product = ""
    multi_str = ""

    # Integers
    first_numerator = 0
    first_denominator = 0
    second_numerator = 0
    second_denominator = 0

    # Lists
    first_fraction_split = []

    first_operand = input("1st operand: ")
    if first_operand in frac_dict:
        for key, first_operand_payload in frac_dict.items():
            if key == first_operand:
                first_fraction = first_operand_payload
    else:
        print(f"Name {first_operand} was not found")
        return

    first_fraction_split = first_fraction.split("/")
    first_numerator = int(first_fraction_split[0])
    first_denominator = int(first_fraction_split[1])

    second_operand = input("2nd operand: ")
    if second_operand in frac_dict:
        for key, second_operand_payload in frac_dict.items():
            if key == second_operand:
                second_fraction = second_operand_payload

    else:
        print(f"Name {second_operand} was not found")
        return

    second_fraction_split = second_fraction.split("/")
    second_numerator = int(second_fraction_split[0])
    second_denominator = int(second_fraction_split[1])

    first_frac = Fraction(first_numerator, first_denominator)
    second_frac = Fraction(second_numerator, second_denominator)

    multiplied_fraction = first_frac.multiply(second_frac)
    multi_str = multiplied_fraction.return_string()

    print(f"{first_numerator}/{first_denominator} * {second_numerator}/"
          f"{second_denominator} ="
          f" {multi_str}")

    simplified_str = multiplied_fraction.simplify()

    print(f"simplified {simplified_str}")
        

def command_file(frac_dict):
    """TBA: This function reads a file and its contents and copies them over
    to a dictionary in the desired format."""

    fraction_name = ""
    filename = ""

    split_row = []
    split_fraction = []

    filename = input("Enter the name of the file: ")

    try:
        my_file = open(filename, "r")
    except FileNotFoundError:
        print("Error: the file cannot be read.")
        return

    for line in my_file:
        try:
            split_row = line.split("=")
            fraction_name = split_row[0]
            original_fraction = split_row[1]
        except IndexError:
            print("Error: the file cannot be read.")
            return

        try:
            split_fraction = original_fraction.split("/")
            numerator = int(split_fraction[0])
            denominator = int(split_fraction[1])
            frac_obj = Fraction(numerator, denominator)
            frac_clause = frac_obj.return_string()
            frac_dict[fraction_name] = frac_clause
        except IndexError:
            print("Error: the file cannot be read.")
            return


def command_print(frac_dict):
    """The function goes through a desired file and adds all rows as entries
    to the fraction dictionary."""
    frac_name = ""

    frac_name = input("Enter a name: ")

    if frac_name in frac_dict:
        for key, payload in sorted(frac_dict.items()):
            if key == frac_name:
                print(f"{key} = {payload}")
    else:
        print(f"Name {frac_name} was not found")


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

        elif my_stripped_input == "print":
            command_print(frac_dict)

        elif my_stripped_input == "*":
            command_times(frac_dict)

        elif my_stripped_input == "file":
            command_file(frac_dict)

        else:
            command_unknown_command()


if __name__ == "__main__":
    main()
