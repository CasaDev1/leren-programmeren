from fruitmand import fruitmand
kleuren_lijst = []
kleurenfruitmand = []
for fruit in fruitmand:
    if fruit['name'] != 'druif':
        kleurenfruitmand.append(fruit)
        if fruit['color'] not in kleuren_lijst:
            kleuren_lijst.append(fruit['color'])

print(kleuren_lijst)
   

    