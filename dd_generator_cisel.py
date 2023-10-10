import random

# nahodny generator cisel v zadaném rozsahu

spodni_mez = int(input("Zadej spodni mez z rozsahu cisel: "))
horni_mez = int(input("Zadej hodni mez z rozsahu cisel:"))
for i in range (horni_mez - spodni_mez):
    nahodne_cislo = random.randint(spodni_mez, horni_mez)
    print(nahodne_cislo)