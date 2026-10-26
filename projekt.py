from main import preved

if __name__ == "__main__":
    vstup = input("zadej emoji ")
    vysledek = preved(vstup)
    if vysledek == vstup:
        print("takové emoji neexistuje")
    else:
        print(vysledek)
