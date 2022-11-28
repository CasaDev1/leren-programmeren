import random

jaofnee = input("Ben je er klaar voor om getal len te raden? ja of nee: ")
if jaofnee.lower() == "ja":
    print("oke je gaat getallen raden!!!")
else:
    print("GAME OVER!!")
    exit()

# keren_dat_je_raad = 0
ronde = 0
punten = 0
# aantal_poginge = 10
# aantal_rondes = 20
# geraden_getal = 0 # hij staat op 0 zodat die de variable herkent
for rondes in range(20):
    geheim_getal = random.randint(1, 1000)
    print(geheim_getal)
    for pogingen in range (10):
        geraden_getal = int(input("Raad een getal tussen 1 en 1000: "))
        if geraden_getal == geheim_getal:
                print("Je hebt het goed Gefeliciteerd!!!")
                punten += 1
                ronde += 1
                break
        verschil = abs(geraden_getal - geheim_getal)
        if geraden_getal > geheim_getal:
            print("Lager")
        elif geraden_getal < geheim_getal:
            print("Hoger")
        if verschil <= 20:
            print("Je bent heel erg warm!")
        elif verschil <= 50:
            print("Je bent warm!")
    ronden_ja_of_nee = input("wil je nog een keer raden ja of nee?: ")
    if ronden_ja_of_nee == "nee":
        break
    else:
        print(f"je hebt {punten} Punt(en)")

print(f"je score is {punten} en je hebt {ronde} rondes gespeeld")




            
        

