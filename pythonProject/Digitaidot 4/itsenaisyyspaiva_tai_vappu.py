# Kuukaudet
TOUKOKUU = 5
JOULUKUU = 12

# Päivät
VAPPU = 1
ITSENAISYYSPAIVA = 6


print("Anna kuukausi:")
kuukausi = int(input())

print("Anna päivä:")
paiva = int(input())

if kuukausi == TOUKOKUU and paiva == VAPPU:
    print("Nyt on vappu tai itsenäisyyspäivä")
elif kuukausi == JOULUKUU and paiva == ITSENAISYYSPAIVA:
    print("Nyt on vappu tai itsenäisyyspäivä")
else:
    print("Nyt ei ole vappu tai itsenäisyyspäivä")