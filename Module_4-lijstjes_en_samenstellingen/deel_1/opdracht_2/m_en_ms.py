import random
MENM = ("oranje", "bruin", "groen", "blauw")
hoeveel = int(input("hoeveel m&m's wilt u?: "))
zak = []
for x in range (hoeveel):
    zak.append(random.choice(MENM))
print(zak)
