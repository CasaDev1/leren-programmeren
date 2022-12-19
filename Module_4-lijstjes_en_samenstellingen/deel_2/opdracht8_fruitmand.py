from fruitmand import fruitmand
fruitmand.append({
    'name' : 'watermeloen',
    'weight' : 900,
    'color' : 'green',
    'round' : True
})
totaal_gewicht = 0
for fruit in fruitmand:
    totaal_gewicht +=  fruit['weight']
    print(fruit['weight'])
print(f"totaal: {totaal_gewicht}")

    

    