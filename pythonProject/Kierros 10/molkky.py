"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Code template for Mölkky.
"""


class Player:

    def __init__(self, name, points=0, mean=0, amount_of_numbers=0,
                 total_points=0):
        self.__name = name
        self.__points = points
        self.__mean = mean
        self.__amount_of_numbers = amount_of_numbers
        self.__total_points = total_points
        
    def get_name(self):
        return self.__name

    def check_for_cheers(self, currect_throw_points):


    def add_points(self, points):
        self.__points += points
        if 40 < self.__points < 49:
            print(f"{self.__name} needs only {50-self.__points} points. It's "
                  f"better to avoid knocking down the pins with higher points.")

        self.__total_points += points
        self.__amount_of_numbers += 1


    def get_points(self):
        return self.__points

    def has_won(self):
        if self.__points > 50:
            self.__points = 25
            return False

        elif self.__points < 50:
            return False

        # Tapaus TASAN 50 PISTETTÄ
        else:
            return True


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        # TODO:
        # c) Add a supporting feedback printout "Cheers NAME!" here.

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p")  # TODO: d)
        print(player2.get_name() + ":", player2.get_points(), "p")  # TODO: d)
        print("")

        throw += 1


if __name__ == "__main__":
    main()
