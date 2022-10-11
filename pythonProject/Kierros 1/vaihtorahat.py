
def main():

    hinta = int(input("Purchase price: "))
    seteli = int(input("Paid amount of money: "))

    vaihtoraha = seteli - hinta

    if seteli == hinta:
        print("No change")

    elif hinta > seteli:
        print("No change")

    elif vaihtoraha > 0 and hinta < seteli:
        print("Offer change:")

        if vaihtoraha // 10 > 0:
            print(vaihtoraha//10, "ten-euro notes")
            vaihtoraha -= (vaihtoraha//10)*10

        if vaihtoraha // 5 > 0:
            print(vaihtoraha//5, "five-euro notes")
            vaihtoraha -= (vaihtoraha//5)*5

        if vaihtoraha // 2 > 0:
            print(vaihtoraha//2, "two-euro coins")
            vaihtoraha -= (vaihtoraha//2)*2

        if vaihtoraha // 1 > 0:
            print(vaihtoraha//1, "one-euro coins")
            vaihtoraha -= (vaihtoraha//1)*1


if __name__ == "__main__":
    main()


    # purchase_price = int(input("Purchase price: "))
    # paid_amount_of_money = int(input("Paid amount of money: "))
    #
    # if purchase_price == paid_amount_of_money:
    #     print("No change")
    #
    # elif purchase_price > paid_amount_of_money:
    #     print("No change")
    #
    # # Käytettävissä seuraavat eurot: 10, 5, 2, 1
    #
    # else:
    #
    #     current_change = paid_amount_of_money - purchase_price
    #
    #     print("Offer change: ")
    #     if current_change % 10 != 0:
    #         tens = change // 10
    #         print(tens, "ten-euro notes")
    #         current_change -= tens
    #     if current_change % 5 != 0:
    #         fives = change // 5
    #         print(fives, "five-euro notes")
    #         current_change -= fives
    #     if current_change % 2 != 0:
    #         twos = change // 2
    #         print(twos, "two-euro coins")
    #         current_change -= twos
    #     if current_change >= 1:
    #         ones = 1
    #         print(ones, "one-euro coins")