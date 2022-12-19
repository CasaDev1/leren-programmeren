from fruitmand import fruitmand
fruitmand.remove({'name' : 'druif','weight' : 5,'color' : 'red','round' : True})
kleuren_lijst = []
for fruit in fruitmand:
    if fruit['color'] not in kleuren_lijst:
        kleuren_lijst.append(fruit['color'])

print(kleuren_lijst)

    

    