# heslo: CZECHITAS
# Zadej 2. znak hesla: z
# Zadej 5. znak hesla: h
# Zadej 7. znak hesla: t
# Vstup povolen

# Zadej 2. znak hesla: e
# Zadej 5. znak hesla: h
# Zadej 7. znak hesla: t
# Vstup zamítnut

import random
heslo = "heslo"
pocet_pismen = len(heslo)

for i in range (3):
    nahodne_cislo = random.randint(1, pocet_pismen)
    znak_hesla = input(f"Zadej {nahodne_cislo}. znak hesla: ")
    if znak_hesla != heslo[(nahodne_cislo-1)]:
        zamitnuty_vstup = print("Vstup zamítnut!")
        exit()
    else:
        continue
print("Vstup povolen.")