#Takzvané Shannonovo číslo má hodnotu 10^123 a udává kolik nejméně lze odehrát různých šachových partií. 
#Vytvořte řetězec, který obsahuje toto číslo zapsané běžným způsobem pomocí cifer. 
#Například 10^3 je 1000, 10^6 je 1000000 atd.
mocnitel = int(input("mocnina> "))
cislo = (10**mocnitel)
print(cislo)

#Čísla s mnoha nulami je v Česku zvykem zapisovat tak, že každé tři nuly následuje mezera. 
#Jeden milión se tedy zapíše jako 1 000 000. Vytvořte řetězec, který obsahuje Shannonovo číslo z předchozího cvičení zapsané v tomto formátu.
 
print(f"{cislo:,d}")
