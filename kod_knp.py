import random

ODDELOVAC = "=" * 50
MOZNOSTI = ("kamen", "nuzky", "papir")



def vypsani_uvitani():
    ODDELOVAC = "=" * 50
    MOZNOSTI = ("kamen", "nuzky", "papir")
    print(
        f"{ODDELOVAC}",
        f"{'Pojď si zahrát hru':^50}",
        f"{','.join(MOZNOSTI).upper():^50}",
        f"{ODDELOVAC}",
        sep="\n"
    )


def loop_hra():
    skore_hrac = 0
    skore_computer = 0
    while True:
        hrac_volba = zadani_hrac()
        ukonceni_hry(hrac_volba)
        overeni_zadani(hrac_volba, MOZNOSTI)
        computer_volba = zadani_computer()
        print(f"Počítač volí: {computer_volba}")
        print(f"{ODDELOVAC}")
        vysledek = vyhodnoceni(hrac_volba, computer_volba)
        print(f"{vysledek: ^50}".upper())
        print(f"{ODDELOVAC}")
        skore_hrac, skore_computer = pricteni_bodu(vysledek, skore_hrac, skore_computer)  # uložim si do dvou proměnných
        vypsani_skore(skore_hrac, skore_computer)
        print(f"{'Další hra': ^50}")
        print(f"{ODDELOVAC}")


def zadani_hrac() -> str:
    moznost_hrac = input(f"Vyber možnost nebo q pro ukončení hry:").lower()
    return moznost_hrac


def overeni_zadani(zadani_od_hrace, MOZNOSTI):
    if zadani_od_hrace not in MOZNOSTI:
        print("Neplatný výběr! Vyber z možností!")


def ukonceni_hry(zadani_od_hrace) -> str:
    if zadani_od_hrace == "q":
        print("Díky za hru!")
        exit()


def zadani_computer() -> str:
    moznost_computer = random.choice(MOZNOSTI)
    return moznost_computer


def vyhodnoceni(volba_hrac, volba_computer) -> str:
    vysledek = ""
    if volba_hrac == volba_computer:
        vysledek = "remiza"

    elif volba_hrac == "kamen":
        if volba_computer == "nuzky":
            vysledek = "vyhra"
        else:
            vysledek = "prohra"

    elif volba_hrac == "papir":
        if volba_computer == "kamen":
            vysledek = "vyhra"
        else:
            vysledek = "prohra"

    elif volba_hrac == "nuzky":
        if volba_computer == "papir":
            vysledek = "vyhra"
        else:
            vysledek = "prohra"
    return vysledek


def pricteni_bodu(vysledek_hry: str, pricteni_bodu_hrac:int, pricteni_bodu_computer: int) -> [int,int]: #nesmím to mít ve funkci, protože to veme vždycky znovu hodnoty skore s nulou!
    if vysledek_hry == "vyhra":
        return pricteni_bodu_hrac + 1, pricteni_bodu_computer
    if vysledek_hry == "prohra":
        return pricteni_bodu_hrac, pricteni_bodu_computer + 1
    return pricteni_bodu_hrac, pricteni_bodu_computer


def vypsani_skore(body_hrac, body_computer):
    print(f"Body Hráč: {body_hrac} vs Počítač: {body_computer}")
    print("-" * 50)
