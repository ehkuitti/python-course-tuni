"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game,
or more like, the stuff that the character carries around.
"""


class Character:
    # TODO: the class implementation goes here.
    def __init__(self, name, item_dict=None):
        if item_dict is None:
            item_dict = {}
        self.__item_dict = item_dict
        self.__name = name
        
    def give_item(self, item):
        if item in self.__item_dict:
            self.__item_dict[item] += 1
        else:
            self.__item_dict[item] = 1

    def remove_item(self, item_to_be_removed):
        if item_to_be_removed in self.__item_dict:
            self.__item_dict[item_to_be_removed] -= 1
            if self.__item_dict[item_to_be_removed] == 0:
                self.__item_dict.pop(item_to_be_removed)

    def printout(self):

        if not self.__item_dict:
            print(f"Name: {self.__name}")
            print(f"  --nothing--")

        else:
            print(f"Name: {self.__name}")
            for item, amount in sorted(self.__item_dict.items()):
                print(f"  {amount} {item}")

    def get_name(self):
        return self.__name

    def has_item(self, item):

        if item in self.__item_dict:
            return True

        else:
            return False

    def how_many(self, item):
        if item not in self.__item_dict:
            return 0
        else:
            return self.__item_dict.get(item)


def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
