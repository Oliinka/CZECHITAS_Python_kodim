hodnota= int(input("Zadej hodnotu: "))

jednotky = input("Zadej jednotky F/C: ")

if jednotky == "f":
    farenheit = 9*hodnota/5+32
    print(f"{hodnota}°C je {farenheit}°F")
elif jednotky == "c":
    celsius = int(5*(hodnota-32)/9)
    print(f"{hodnota}°F je {celsius}°C")

else:
    print("Neplatná hodnota jednotek.")