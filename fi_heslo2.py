import random
heslo = "heslo"
pocet_pismen = len(heslo)

for i in range (3):
    nahodne_cislo = random.randint(1, pocet_pismen)
    znak_hesla = input(f"Zadej {nahodne_cislo}. znak hesla: ")
    if znak_hesla != heslo[(nahodne_cislo-1)]:
        zamitnuty_vstup = True
    else:
        continue

if zamitnuty_vstup==True:
    print("Vstup zakázán.")
else:
    print("Vstup povolen.")

