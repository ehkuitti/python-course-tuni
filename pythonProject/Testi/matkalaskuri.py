HENKILOMAARA = 5
PAIVIEN_MAARA = 5


def main():

    # PAKOLLISET KULUT

    majoitus = 244 / HENKILOMAARA
    lennot_menopaluu = 30
    diesel_tre_tku = 15
    ruokailu = 20 * PAIVIEN_MAARA
    pakolliset_kulut = majoitus + lennot_menopaluu + diesel_tre_tku \
                                + ruokailu

    # VALINNAISET, TODENNÄKÖISET KULUT

    museum_of_gdansk_opiskelija = 3.18
    museum_of_1939_opiskelija = 3.82
    old_town = 0


    valinnaiset_kulut = museum_of_1939_opiskelija + museum_of_gdansk_opiskelija

    kaikki_yhteensa = pakolliset_kulut + valinnaiset_kulut


    print(f"PAKOLLISET KULUT")
    print(f"Majoituksen hinta: {majoitus} euroa.")
    print(f"Lennot (menopaluu): {lennot_menopaluu} euroa.")
    print(f"Diesel TRE-TKU (menopaluu): {diesel_tre_tku} euroa.")
    print(f"Ruokailu (20e pv budjetti): {ruokailu} euroa.")
    print(f"Yhteensä: {pakolliset_kulut} euroa.")
    print()
    print("VALINNAISET KULUT")
    print(f"Museum of Gdansk (opiskelija): {museum_of_gdansk_opiskelija} "
          f"euroa.")
    print(f"Museum of 1939 (opiskelija): {museum_of_1939_opiskelija} euroa.")
    print(f"Yhteensä: {valinnaiset_kulut} euroa.")
    print()
    print(f"Kaikki yhteensä: {kaikki_yhteensa}")

    print("")


if __name__ == "__main__":
    main()
