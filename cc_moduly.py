# importujeme modul math na začátku programu
import math

number = math.pi
print("pi zaokrouhleno funkci math:")
rounded_down = math.floor(number)
print(rounded_down)


print("pi zaokrouhleno v pythonu na 0 a na 2 deseina cisla")
print(round(number))
print(round(number, 0))
print(round(number, 2))

print("kdyz pi prevedu na intiger, ziskam cele cislo, bez zbytku jakoby zaokrouhleno dolu:")
print(int(number))


print("funkci x=math.ceil(pi) prevedu cislo na nejblizsi vyssi cislo")
zaokrouhlene_cislo = math.ceil(number)
print(zaokrouhlene_cislo)




