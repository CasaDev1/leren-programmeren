from fruitmand import fruitmand
import random
aantal_vraag = int(input("Hoeveel fruit wilt u zien?: "))

for i in range(aantal_vraag):
    fruit = random.choice(fruitmand)   
    print(fruit['name'])