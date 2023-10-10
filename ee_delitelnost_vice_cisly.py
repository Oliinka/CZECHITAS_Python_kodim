# Tip: nezapomeňte si zadané číslo převést na int.

# Tip 2: K ověření dělitelnosti použij operátor % - zbytek po celočíselném dělení a zkontroluj, zda je výsledek 0.
# Například 15 % 5 vrací 0, protože 15 je dělitelné 5.

print("Zadej číslo:")
cislo = int(input("> "))

delitelnost_3 = cislo%3
delitelnost_2 = cislo%2

#print(delitelnost_3)
#print(delitelnost_2)

if delitelnost_2==0 and delitelnost_3==0:
    print("Číslo je dělitelné dvěma i třema.")
elif delitelnost_2==0 and delitelnost_3!=0:
    print ("Číslo je dělitelné dvěma.")
elif delitelnost_2!=0 and delitelnost_3==0:
    print("Číslo je dělitelné třema.")
else:
    print("Číslo není dělitelné dvěma ani třema.")