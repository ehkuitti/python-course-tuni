YOLISA = 3.00

hinta = 0.0

print("Anna matkustajan ikä:")
ika = int(input())

print("Anna matkan alkamisaika tasatunteina:")
kellonaika = int(input())

if ika <= 65 and 9 <= kellonaika <= 14:
    hinta = 1.20

elif ika <= 6:
    hinta = 0.00

elif 7 <= ika <= 16 and 0 <= kellonaika <= 4:
    hinta = 1.10 + YOLISA

elif 17 <= ika <= 24 and 0 <= kellonaika <= 4:
    hinta = 1.50 + YOLISA

elif ika >= 25 and 0 <= kellonaika <= 4:
    hinta = 2.10 + YOLISA

elif 7 <= ika <= 16:
    hinta = 1.10

elif 17 <= ika <= 24:
    hinta = 1.50

elif ika >= 25:
    hinta = 2.1

print("Matkan hinta on:")
print(hinta)
