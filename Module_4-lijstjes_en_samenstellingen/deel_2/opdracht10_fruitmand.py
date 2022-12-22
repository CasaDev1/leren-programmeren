from fruitmand import fruitmand
from operator import itemgetter

fruit_sorted = sorted(fruitmand, key=itemgetter('weight'), reverse=True )
print(fruit_sorted)
for fruit in fruit_sorted:
    kg = (fruit['weight'] / 1000)
    naam = fruit['name']

    print(f"naam: {naam}               gewicht: {kg}kg")