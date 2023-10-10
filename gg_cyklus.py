# vypise postupne cely cyklus.
znamky = [1, 3, 2, 1, 1, 2]
for z in znamky:
    print(z)


# vypise vschny maily se jmeny
jmena = ['petr', 'pavel', 'jitka', 'jana']
for jmeno in jmena:
    mail = jmeno + '@gmail.com'
    print(mail)

# vypise pocet jednicek
znamky = [1, 3, 2, 1, 1, 2]
pocet_jednicek = 0
for z in znamky:
    if z == 1:
        pocet_jednicek = pocet_jednicek + 1
print("Počet jedniček:", pocet_jednicek)


#vypise soucet celeho cyklu
soucet = 0
cisla = [2, 4, -1, 50, 0, 42, 3]
for cislo in cisla:
    soucet = soucet + cislo
print("Součet:", soucet)