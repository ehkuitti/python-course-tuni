def reverse_name(name):

    a, b = name.split(",")
    return b.strip() + " " + a.strip()

def main():
    nimi = input("Anna Nimi: ")
    print(reverse_name(nimi))

if __name__ == "__main__":
    main()