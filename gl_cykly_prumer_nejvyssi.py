hry = [
    ["Ňadro na ňadru na nádru", 180],
    ["Útok plyšových krokodýlů", 95],
    ["Cesta do říše zelí", 128],
    ["Romance na zdymadle", 144],
    ["Zátiší s mimozemšťanem", 135],
    ["Čtyři facky a dortík", 100],
    ["Motorová okurka", 1650],
    ["Johnny Noir", 140],
    ["Pražská kavárna vrací úder", 130],
    ["Pět sester ve vratech", 111],
    ["Stařec a krajta", 187],
    ["Růžová nemoc", 210],
    ["Smrt v přímém přenosu", 265],
]
print("""
vypocet nejvyssi hodnoty:----------------------------------------------------------------------""", end = "\n\n")

print(max(map(lambda x: x[-1],hry)))

print("""
vypocet nejvyssi hodnoty: ----------------------------------------------------------------------""", end = "\n\n")

def max_value(hry):
    return max([sublist[1] for sublist in hry])
print (max_value(hry))

print("""
vypocet prumerne hodnoty: ----------------------------------------------------------------------""", end = "\n\n")
