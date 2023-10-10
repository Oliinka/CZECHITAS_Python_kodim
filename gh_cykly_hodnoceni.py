# Mějme seznam hodnocení divadelní hry Plyšáci na útěku , který vypadá takto:

hodnoceni = [7, 9, 6, 7, 9, 8]

# Vytvořte program, který projde tento seznam a vypíše každé hodnocení na nový řádek.
# znamka je nova promenna a muze to byt cokoliv, x, i, p prostě nějaké nové oznaceni promenne:
for znamka in hodnoceni:
    print(znamka)

# Upravte program tak, aby vypisoval výstup v tomto formátu znamka/10

for znamka in hodnoceni:
    print(f"{znamka}/10")