import random
from data import *

# variabelen
hoeveel_fout = 0
te_raden_woord = ""
geraden_van_woord = ""
fout_geraden_letters = []
goed_geraden_letters = []
woorden_lijst = []
max_raden = len(galgje_lijst)
VERSION = "0.1 Draft"

# import de data (woorden uit bestand)
# todo: uitbreiden met exception handling en een default woord indien file niet beschikbaar.

with open('woorden.txt', 'r') as file:
    content = file.read()
    #print(content)
woorden_lijst = content.split('\n')
te_raden_woord = random.choice(woorden_lijst)

print("Welkom bij Galgje TM")
print("copyright 2022")
print(f"versie: {VERSION}")
print(f"---------------------------------------------")
print(f"Je hebt {max_raden} kansen om het woord te raden!")
print("")
print(f"veel succes")
print(f"---------------------------------------------")


geraden_van_woord = "_" * len(te_raden_woord)
print("#####################################################")
print(f"Ronde {te_raden_woord}")
print("#####################################################")
while hoeveel_fout < max_raden:
    print(f"Te raden woord: {geraden_van_woord}")
    print("Voer de letter in die je wilt raden en toets enter...:")

    # vraag om één letter
    letter = ""
    while letter == "":
        letter = input("Voer letter in: ")

        # valideer de input
        if len(letter) != 1:
            print("Je moet max. 1 letter invoeren!!!")
            letter = ""
        elif not letter.isalpha():
            print("Je moet wel een letter invoeren!!!")
            letter = ""
        elif letter.isupper():
            print("Geen hoofdletters a.u.b.")
            letter = ""

    if letter in geraden_van_woord or letter in fout_geraden_letters:
        print("Heb je al gehad, maar vooruit maar... zucht.")
    elif letter in te_raden_woord:
        print("Keurig, zit er in!")
        goed_geraden_letters.append(letter)
    else:
        fout_geraden_letters.append(letter)
        print("Helaas, zit er niet in :-(")
        print(galgje_lijst[hoeveel_fout])
        hoeveel_fout += 1


    # regel dat je een woord krijgt om op het scherm te tonen.
    geraden_van_woord = ''
    for l_from_te_raden in te_raden_woord:
        if l_from_te_raden in goed_geraden_letters:
            geraden_van_woord += l_from_te_raden
        else:
            geraden_van_woord += "_"

    if not "_" in geraden_van_woord:
        print("Goed gedaan, woord geraden!!!")
        break

print("#####################################################")
print("Hartelijk dank voor het spelen van deze ronde.")
print(f"het woord was   : {te_raden_woord}")
print(f"door jou geraden: {geraden_van_woord}")
print("#####################################################")