# Použijte Python jako kalkulačku:
# Jeden lístek do divadla "Pěst na oko" stojí 12 euro. 
# Spočítejte měsíční příjem divadla ze vstupného přichází-li průměrně 174 návštěvnic a návštěvníků na jedno představení a divadlo hraje 15 představení měsíčně. 
# Výsledek vypište na obrazovku.

cena_listku = int(input("Zadej cenu listku: "))
# pocet_predstaveni_mesicne = int(input("Zadej pocet predstaveni mesicne: "))
pocet_prodanych_listku =  int(input("Zadej pocet prodaných lístků: "))
trzba = cena_listku * pocet_prodanych_listku

print(f"Měsíční příjem divadla z prodeje lístků je: {trzba}.")

print("""
Divadlo se rozhodlo prodávat studentské vstupné 
ve výši 65% plného vstupného. 
Jak se změní měsíční příjem divadla pokud víme,
že část návštěvníků jsou studentky a studenti?""")
print("Zadej procento návštěvníků co jsou studenti:")
procento_studentu = int(input("> "))
print("%") 
tzba_sleva = ((pocet_prodanych_listku * procento_studentu * 0.01)*cena_listku*0.5)
trzba_plne_vstupne = (pocet_prodanych_listku * (1-procento_studentu*0.01))*cena_listku

print(f"Cena z prodeje listků když studenti dostanou slevu je: {tzba_sleva+trzba_plne_vstupne}")
