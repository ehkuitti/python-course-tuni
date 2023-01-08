"""KOODI EI TOIMI TEHTÄVÄN ODOTTAMALLA TAVALLA."""

budjetti = 0
tuotteiden_lukumaara = 0
onko_annettu_laittomia_arvoja = False

# Arvoja kysellään niin kauan kun rahasumma tai tuotteiden lukumäärä on nolla
# tai negatiivinen
while True:
    budjetti = int(input("Anna rahasumma:\n"))
    tuotteiden_lukumaara = int(input("Syötä tuotteiden lukumäärä:\n"))
    if (budjetti <= 0) or (tuotteiden_lukumaara <= 0):
        print("Syötä vain positiivisia kokonaislukuja.")
        onko_annettu_laittomia_arvoja = True
        break
    # Annettiin positiivinen budjetti ja -tuotteiden määrä
    else:
        break

kysyttyjen_tuotteiden_lukumaara = 0
tuotteiden_kokonaissumma = 0
riittivatko_rahat = True
if not onko_annettu_laittomia_arvoja:
    while kysyttyjen_tuotteiden_lukumaara < tuotteiden_lukumaara:
        nykyisen_tuotteen_hinta = int(input("Syötä hinta:\n"))
        tuotteiden_kokonaissumma += nykyisen_tuotteen_hinta
        if tuotteiden_kokonaissumma > budjetti:
            print("Rahat eivät riitä!")
            riittivatko_rahat = False
            break
        kysyttyjen_tuotteiden_lukumaara += 1

if onko_annettu_laittomia_arvoja:
    riittivatko_rahat = False
if tuotteiden_kokonaissumma > 0 and riittivatko_rahat:
    print("Rahat riittävät, jäljelle jää", tuotteiden_kokonaissumma-budjetti)