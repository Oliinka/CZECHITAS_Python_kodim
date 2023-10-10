# vyber nahodneho jmena ze seznamu
import random

rodina = ["Olga", "Samuel","Milos", "Jarmila"]
pocet_clenu = len(rodina)

print(f"Rodina má {pocet_clenu} členů.")

for jmeno in rodina:
    clen_rodiny = random.randint(jmeno, rodina)
    print(jmeno)
