#import random
from pomocne_fce_knp import *

ODDELOVAC = "=" * 50
MOZNOSTI = ("kamen", "nuzky", "papir")

#úvod, který importuju do main()
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
# hlavní kod hry, přes definované fce, které importuji do main()
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


