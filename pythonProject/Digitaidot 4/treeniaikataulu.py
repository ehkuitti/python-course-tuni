print("Anna viikonpäivä:")
viikonpaiva = input()

if viikonpaiva == "ma" or viikonpaiva == "maanantai":
    print("19-20.30")

elif viikonpaiva == "ke" or viikonpaiva == "keskiviikko":
    print("18-20")

elif viikonpaiva == "to" or viikonpaiva == "torstai":
    print("18.30-20")

else:
    print("Tuntematon viikonpäivä.")