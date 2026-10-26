import emoji

def preved(vstup):
      vysledek = emoji.emojize(vstup)
      if vysledek == vstup:
          return None          # takové emoji neexistuje
      return vysledek
