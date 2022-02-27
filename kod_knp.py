import random
from fce_bodovani import *


def main():
    ODDELOVAC = "=" * 50
    MOZNOSTI = ("kamen", "nuzky", "papir")
    score_hrac = 0
    score_pc = 0

    print(
        f"{ODDELOVAC}",
        f"{'Pojď si zahrát hru':^50}",
        f"{','.join(MOZNOSTI).upper():^50}",
        f"{ODDELOVAC}",
        sep="\n"
    )

    while True:
        print(ODDELOVAC)
        hrac = input("Tvoje volba: ").lower()
        pocitac = random.choice(MOZNOSTI)
        print(f"Počítač volí: {pocitac}")

        #ověření zadání
        if hrac not in MOZNOSTI:
            print("Neplatná volba!".upper())

        elif hrac in MOZNOSTI:
            # remíza
            if hrac == pocitac:
                vysledek = "remiza"
                print(ODDELOVAC)
                print(f"{'Remíza!':^50}")
                print(ODDELOVAC)
                bodovani(vysledek,score_hrac, score_pc)

            #papir - kámen
            if hrac == "papir":
                if pocitac == "kamen":
                    vysledek = "vyhra"
                    print(ODDELOVAC)
                    print(f"{'Vyhrál jsi!':^50}")
                    print(ODDELOVAC)
                    score_hrac += 1
                    bodovani(vysledek,score_hrac, score_pc)

            elif hrac == "kamen":
                if pocitac == "papir":
                    vysledek = "prohra"
                    print(ODDELOVAC)
                    print(f"{'Prohrál jsi!':^50}")
                    print(ODDELOVAC)
                    score_pc += 1
                    bodovani(vysledek,score_hrac, score_pc)
                    exit = input("Chceš hrát znovu? A/N: ").lower()
                    if exit != "a":
                        print(f"{'Díky za hru':^50}")
                        break

            #nuzky - kamen
            if hrac == "kamen":
                if pocitac == "nuzky":
                    vysledek = "vyhra"
                    print(ODDELOVAC)
                    print(f"{'Vyhrál jsi!':^50}")
                    print(ODDELOVAC)
                    score_hrac += 1
                    bodovani(vysledek,score_hrac, score_pc)

            elif hrac == "nuzky":
                if pocitac == "kamen":
                    vysledek = "prohra"
                    print(ODDELOVAC)
                    print(f"{'Prohrál jsi!':^50}")
                    print(ODDELOVAC)
                    score_pc += 1
                    bodovani(vysledek,score_hrac, score_pc)
                    exit = input("Chceš hrát znovu? A/N: ").lower()
                    if exit != "a":
                        print(f"{'Díky za hru':^50}")
                        break

            #nuzky - papir
            if hrac == "nuzky":
                if pocitac == "papir":
                    vysledek = "vyhra"
                    print(ODDELOVAC)
                    print(f"{'Vyhrál jsi!':^50}")
                    print(ODDELOVAC)
                    score_hrac += 1
                    bodovani(vysledek,score_hrac, score_pc)

            elif hrac == "papir":
                if pocitac == "nuzky":
                    vysledek = "prohra"
                    print(ODDELOVAC)
                    print(f"{'Prohrál jsi!':^50}")
                    print(ODDELOVAC)
                    score_pc += 1
                    bodovani(vysledek,score_hrac, score_pc)
                    exit = input("Chceš hrát znovu? A/N: ").lower()
                    if exit != "a":
                        print(f"{'Díky za hru':^50}")
                        break

if __name__ == "__main__":
    main()

