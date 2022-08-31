print("Anna rahasumma:")
budjetti = int(input())

onkoMaaraKelvollinen = False
while not onkoMaaraKelvollinen:
    print("Söytä tuotteiden lukumäärä:")
    tuotteiden_maara = int(input())
    if tuotteiden_maara > 0:
        onkoMaaraKelvollinen = True
    else:
        print("Syötä vain positiivisia kokonaislukuja.")

ostosten_yhteissumma = 0
onkoTarpeeksiRahaa = True
while onkoTarpeeksiRahaa:
    print("Syötä hinta:")
    hinta = int(input())
    ostosten_yhteissumma += hinta
    if hinta <= 0:
        print("Syötä vain positiivisia kokonaislukuja. ")

    if ostosten_yhteissumma > budjetti:
        print("Rahat eivät riitä!")
        onkoTarpeeksiRahaa = False
        