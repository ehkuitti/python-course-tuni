kertoma = 1

print("Anna luku:")
luku = int(input())

i = 0

if luku == 0:
    kertoma = 1

else:
    vahennetty_luku = luku
    while i < luku:
        kertoma *= vahennetty_luku
        vahennetty_luku -= 1
        i += 1

print("Luvun kertoma on", kertoma)
