# prestupny rok

print("Zadej rok:")
rok=int(input("> "))

# prestupnost = rok/4 je celé číslo a zároveň pakliže je rok dělitelný 100 musí být zároveň i dělitelný 400 
# tzn.: 1900 neni přestuný a 2000 je přesupný

prestupnost = int(rok/4)
podminka_400 = int(rok/400)
podminka_100 = int(rok/100)
#neprestupny = rok/100 a zároveň rok/400 je celé číslo

# if prestupnost*4 == rok and podminka_400*400==rok:

if prestupnost*4 != rok:
    print("Rok není přestupný.")
elif podminka_400*400 == rok:
    print("Rok je přestupný.")
elif podminka_100*100 == rok:
    print("Rok není přestupný.")
else:
    print("Rok je přestupný.")