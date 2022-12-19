from fruitmand import fruitmand
gewicht = 0
letter = 0
vertaal_dict = dict(orange = "oranje", red = "red", brown = "bruin", green = "groen", yellow = "geel", pink = "roze", purple = "paars", black = "zwart")
for fruit in fruitmand:
    if letter < len(fruit['name']):
        name = fruit['name']
        kleur = fruit['color']
        gewicht = fruit['weight']
        letter = len(fruit['name'])

print(f"de {name} ({letter}) heeft een {vertaal_dict.get(kleur)} kleur en een gewicht van {gewicht} kg")


