
print("""
Uložte si do proměnné nazev řetězec s názvem "Divadlo Pěst na oko". 
Pokud použijeme designové písmo nad hlavní vchod budovy, jeden znak (i mezera) bude široký 30 cm. 
Použijte funkci len() abyste zjistili počet znaků v názvu divadla a spočítejte délku nápisu v centimetrech.
""")

nazev = ("Divadlo Pěst na oko")

znak = 30

pocet_znaku = len(nazev)
print(f"Počet znaků v názvu včetně mezer je: {pocet_znaku}")

delka_nazvu = znak*pocet_znaku
print(f"Délka názvu je: {delka_nazvu} cm")