"""
TÄMÄ MESIERKKI ON VIHREELLINEN!
"""

def main():
    sum = 0

    repetition_counter = 1

    # Ohjelma menee ikuiseen looppiin, sillä REPETITION_COUNTERIA EI KOSKAAN KASVATETA, vaan pelkkää summaa
    while repetition_counter <= 5:
        number = int(input("Enter the next number: "))
        sum += number

    print("The sum of the numbers is", sum)

    if sum < 0:
        print("Which is a negative number!")
    elif sum > 0:
        print("Which is a positive number!")

if __name__ == "__main__":
    main()