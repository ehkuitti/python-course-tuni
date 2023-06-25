def main():
    # TIEDETYT SUMMAT EUROISSA
    lento = 15
    majoitus_gdansk = 233
    pysakointi_ja_tkutre_menopaluu = 25
    ruoan_paivabudjetti = 20

    # MÄÄRÄT
    paivien_maara = 4
    osallistujien_maara = 5

    # Lasketaan majoituksen hinta arvoilla
    majoitus_yhteensa = (majoitus_gdansk / 5)

    # Lasketaan menopaluun hinta
    menopaluu_lento = lento * 2

    # Lasketaan ruokailut (viiden päivän edestä)
    ruokailut = paivien_maara * ruoan_paivabudjetti

    # Lasketaan bensan hinta per henkilö
    bensahinta = 60 // 4

    # PUUTTUU MAHD. MUSEOVIERAILU TMS. OHJELMAA VARSOVASSA

    kokonaishinta = bensahinta + \
                    majoitus_yhteensa + menopaluu_lento + ruokailut

    print("KAIKKI HINNAT ON PER HENKILÖ")
    print()
    print(f"Majoitus: {majoitus_yhteensa} euroa")
    print(f"Lennot (menopaluu): {menopaluu_lento} euroa")
    print(f"Ruokailut: {ruokailut} euroa")
    print()
    print(f"MATKAN KOKONAISHINTA: {kokonaishinta} euroa")

    if majoitus_yhteensa > 300:
        print("Kallista on.")
        return 1

    return 0


if __name__ == "__main__":
    main()
