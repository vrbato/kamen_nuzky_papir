import random
MOZNOSTI = ("kamen", "nuzky", "papir")

#pro každý krok kodu - si definuji funkci ideálně co jeden krok -> to funkce, nebo když se mi to opakuje, tak to dát do 1 fce

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