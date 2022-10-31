from random import randint


naam = input("Wat is uw naam?")
aantal_comp = int (input("hoe veel complimenten wilt uw?"))

random_getal = randint(1, 4)

for x in range(aantal_comp):
    if random_getal == 1:
        (f"je bent een topper{naam}")
    if random_getal == 2:
        (f"je bent een toffe gozer{naam}")
    if random_getal == 3:
        (f"je bent goed bezig{naam}")
    if random_getal == 4:
        (f"je bent een coole gast{naam}")
