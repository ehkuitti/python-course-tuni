"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150541820
Name:   Eetu Kuittinen
Email:  eetu.kuittinen@tuni.fi

Ohjelma laskee kolmion kulmia annettujen parametrien perusteella.
"""


def calculate_angle(angle_1, angle_2=90):
    """Laskee kolmion kulmia annetuilla parametreilla. Jos toista parametria
    ei anneta, käyttää suoran kulman astelukua 90."""
    angle_3 = 0
    sum_of_angles = 180

    angle_3 = sum_of_angles - angle_1 - angle_2

    return angle_3


def main():
    angle_1 = 0
    angle_2 = 0

    angle_1 = int(input("Enter angle 1: "))
    angle_2 = int(input("Enter angle 2: "))

    calculate_angle(angle_1, angle_2)


if __name__ == "__main__":
    main()
