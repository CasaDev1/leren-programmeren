from fruitmand import fruitmand
kleuren_lijst = set()
for fruit in fruitmand:
    if fruit['name'] == 'druif':
        fruitmand.remove(fruit)
for fruit in fruitmand:
    kleuren_lijst.add(fruit['color'])
   
print(kleuren_lijst)
   

    