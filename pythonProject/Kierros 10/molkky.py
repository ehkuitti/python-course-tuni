"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Code template for Mölkky.
"""


class Player:

    def __init__(self, name, points=0, non_adjusted_points=0, mean=0,
                 amount_of_numbers=0, total_points=0, hit_percentage=0.0,
                 hits=None):
        if hits is None:
            hits = []
        self.__name = name
        self.__points = points
        self.__non_adjusted_points = non_adjusted_points
        self.__mean = mean
        self.__amount_of_numbers = amount_of_numbers
        self.__total_points = total_points
        self.__hit_percentage = hit_percentage
        self.__hits = hits

    def get_name(self):
        return self.__name

    def count_hit_rate(self):

        amount_of_values_greater_than_one = 0
        total_amount_of_hits = len(self.__hits)

        # [0, 1, 0, 1]
        #     1
        for value in self.__hits:
            if value >= 1:
                amount_of_values_greater_than_one += 1

        if total_amount_of_hits >= 1:
            self.__hit_percentage = (amount_of_values_greater_than_one /
                                     total_amount_of_hits) * 100

        return self.__hit_percentage

    def check_for_cheers(self, currect_throw_points):
        self.__mean = self.__total_points / self.__amount_of_numbers

        if currect_throw_points > self.__mean:
            print(f"Cheers {self.__name}!")

    def add_points(self, points):
        self.__points += points
        if 40 < self.__points < 49:
            print(f"{self.__name} needs only {50 - self.__points} points. It's "
                  f"better to avoid knocking down the pins with higher points.")
        self.__hits.append(points)
        self.__total_points += points
        self.__amount_of_numbers += 1

    def get_points(self):
        return self.__points

    def has_won(self):
        if self.__points > 50:
            self.__non_adjusted_points = self.__points
            self.__points = 25
            print(self.__name, "gets penalty points!")
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

        in_turn.check_for_cheers(pts)

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p,",
              "hit percentage", round(player1.count_hit_rate(), 1))  # TODO: d)
        print(player2.get_name() + ":", player2.get_points(), "p,",
              "hit percentage", round(player2.count_hit_rate(), 1))  # TODO: d)
        print("")

        throw += 1


if __name__ == "__main__":
    main()
