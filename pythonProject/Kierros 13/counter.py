"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 0123456
Name:       Xxxx Yyyyyy
Email:      xxxx.yyyyyy@tuni.fi

Code template for counter program.
"""

from tkinter import *


class Counter:
    def __init__(self):
        self.__mainwindow = Tk()

        # TODO: You have to creater one label and four buttons and store
        #       them in the following attributes:
        #
        #       self.__current_value_label  # Label displaying the current value of the counter.
        #       self.__reset_button         # Button which resets counter to zero.
        #       self.__increase_button      # Button which increases the value of the counter by one.
        #       self.__decrease_button      # Button which decreases the value of the counter by one.
        #       self.__quit_button          # Button which quits the program.
        #
        #       Make sure you name the components exactly as shown above,
        #       otherwise the automated tests will fail.

        self.__current_value = 1

        self.__current_value_label = Label(self.__mainwindow,
                                           text=self.__current_value,
                                           relief=GROOVE)
        self.__current_value_label.grid(row=0, column=0)

        self.__reset_button = Button(self.__mainwindow, text="Reset",
                                     command=self.reset)
        self.__reset_button.grid(row=1, column=0)

        self.__increase_button = Button(self.__mainwindow, text="Increase",
                                        command=self.increase)
        self.__increase_button.grid(row=1, column=1)

        self.__decrease_button = Button(self.__mainwindow, text="Decrease",
                                        command=self.decrease)
        self.__decrease_button.grid(row=1, column=2)

        self.__quit_button = Button(self.__mainwindow, text="Quit",
                                    command=self.quit)
        self.__quit_button.grid(row=1, column=3)

        # TODO: Implement the rest of the needed methods here.

        self.__mainwindow.mainloop()

    def reset(self):
        self.__current_value = 0
        self.__current_value_label.config(text=self.__current_value)

    def increase(self):
        self.__current_value += 1
        self.__current_value_label.config(text=self.__current_value)

    def decrease(self):
        self.__current_value -= 1
        self.__current_value_label.config(text=self.__current_value)

    def quit(self):
        self.__mainwindow.destroy()


def main():
    # There is no need to modify the main function.
    # As a matter of fact, automated tests ignore main
    # once again.

    Counter()


if __name__ == "__main__":
    main()
