# Založte si program hesla.py a na jeho začátek vložte následující kód obsahující seznam hesel pro přihlášení do nějakého systému

hesla = [
    "xyz101",
    "punťa",
    "razor-blade",
    "1234",
    "12011986",
    "martin111",
    "trhnisi",
    "hokuspokus",
    "jeník15",
    "kristus-te-spasi",
    "beruška",
    "strčprstskrzkrk",
]
# Pomocí cyklu vypište všechny hesla na obrazovku, každé na jeden řádek.
for heslo in hesla:
    print(heslo)
# Upravte váš program tak, aby vypisoval jen bezpečná hesla, tedy taková, jež jsou delší než 8 znaků.
print("Bezpecna hesla jsou:")


for heslo in hesla:
    bezpecne_heslo = len(heslo) > 8
    if bezpecne_heslo == True:
        print(heslo)
    else:
        pass
