hry = [
    ["Ňadro na ňadru na nádru", 180],
    ["Útok plyšových krokodýlů", 95],
    ["Cesta do říše zelí", 128],
    ["Romance na zdymadle", 144],
    ["Zátiší s mimozemšťanem", 135],
    ["Čtyři facky a dortík", 100],
    ["Motorová okurka", 165],
    ["Johnny Noir", 140],
    ["Pražská kavárna vrací úder", 130],
    ["Pět sester ve vratech", 111],
    ["Stařec a krajta", 187],
    ["Růžová nemoc", 210],
    ["Smrt v přímém přenosu", 265],
]
print("""
Pomocí cyklu projděte tento seznam 
a vypište na výstup názvy všech her.
""")
for nazev_hry in hry:
    print(nazev_hry[0])

print("""
Vypište na výstup názvy všech her, 
které trvají více než 120 minut.""")

for nazev_hry in hry:
    delka_hry = nazev_hry[1] > 120
    if delka_hry == True:
        print(nazev_hry[0])
    else:
        pass

# Vypište na výstup názvy všech her spolu s jejich trváním v hodinách a minutách.