getal = int(input("Voer een getal in waarvan je de tafel wilt weten:"))
print(f" de tafel van het {getal} is:")
for x in range (1,11):
    som = getal * x
    print(f"{x} x {getal} = {som}")