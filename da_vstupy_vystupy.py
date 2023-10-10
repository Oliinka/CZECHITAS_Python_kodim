# V tomto programu pomocí funkce print() vypište na obrazovku Divadlo Pěst na oko. 
# Program spusťte a vyzkoušejte, že dělá co má.

print("Divadlo Pěst na oko")

# Upravte tento program tak, že do proměnné nazev uložíte název nějakého divadelního představení 
# a do proměnné cas uložte čas konání tohoto představení. 
# Nyní pomocí funkce print() nechte program vypsat na obrazovku na jeden řádek název představení a čas konání, 
# např. Zkrocení zlé ženy - 19:30.

nazev = "Zkroceni zle zeny"
cas = "19:30"

print(nazev + " - " + cas)

# Upravte dále program tak, že do proměnné hodina uložíte hodinu konání představení (jako celé číslo) 
# a do proměnné minuta minutu konání, také jako celé číslo. 
# Zařiďte, aby výstup programu vypadal takto: Zkrocení zlé ženy - 19:30.

hodina = 19
minuta = 30

print(f"{nazev} - {hodina}:{minuta}")
# alternativn2 po staru ale to nad tim je kratsi a elegantnejsi
print(nazev + " - " + str(hodina) + ":" + str(minuta))