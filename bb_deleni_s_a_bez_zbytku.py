#Zaexperimentujte s operátory celočíselného dělení a dělení se zbytkem.

#Kolikrát se vejde číslo 72 do 1024? Kolik je zbytek po dělení čísla 1024 číslem 72?
delenec = int(input("Delene cislo: "))
delitel = int(input("Delitel: "))
podil = delenec/delitel

print(f"Podil je:{podil}")

zaokrouhleny_podil = (round(podil, 0))
# zaokrouhleni na dve desetina cisla: zaokrouhleny_podil = (round(podil, 2)) 
cele_cislo = int(podil)

print(f"Když podíl zaokrouhlím je číslo: {zaokrouhleny_podil}")
print(f"Když budu chtít pouze cele cislo z delěni prevedu podil na intiger: {cele_cislo}")

zbytek = (delenec - (delitel * cele_cislo))
print(f"Zbytek deleni je: {zbytek}")

# Divadlo má délky představení vždy uloženo v minutách. 
# Například extrémně nudné a zničující představení "Smrt v přímém přenosu" trvá 265 minut. 
# Uložte tuto hodnotu do proměnné delka.
print("pocet minut je 265")
delka = 265
prevod_na_hodiny = int(delka / 60)
# Použijte proměnnou delka a spočítejte trvání představení vyjádřeno v hodinách a minutách. 
# Do proměnné hodin uložte počet celých hodin a do proměnné minut uložte zbylé minuty.
 
print(f"Pocet hodin a minuty je: {prevod_na_hodiny}h a {delka-prevod_na_hodiny*60}min")