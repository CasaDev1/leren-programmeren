import random
menm = ("oranje", "bruin", "groen", "blauw")
hoeveel = int(input("hoeveel m&m's wilt u?: "))
zak = []
for x in range (hoeveel):
    randomcijfer = random.randint(0,3)
    zak.append(menm[randomcijfer])

print(zak)
