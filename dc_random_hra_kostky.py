import random
# jednoduchy zapis vybere cislo v rozmezi 1-6
nahodne_cislo = random.randint(1, 6)
print(nahodne_cislo)


# nahodny hod kostkou se zadanim poctu hodu
pocet_hodu_kostkou = int(input("Zadej počet hodů kostkou: "))
for i in range (pocet_hodu_kostkou):
    nahodne_cislo = random.randint(1, 6)
    print(nahodne_cislo)


