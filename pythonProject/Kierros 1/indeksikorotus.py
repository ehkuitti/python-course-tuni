# Luetaan syote string-muuttujaan
syote = input("Enter the amount of the study benefits: ")

# Muunnetaan liukuluvuksi
luku = float(syote)

# Tehdään lasku
tulos = luku * 1.0117

# Tulostetaan vaadittu teksti
print("If the index raise is 1.17 percent, the study benefit,")
print("after a raise, would be", tulos, "euros")

uusiTulos = tulos * 1.0117

print("and if there was another index raise, the study")
print("benefits would be as much as", uusiTulos, "euros")