from vragen_game import*
#eerst heb ik een function gemaakt voor de start van het programma(game) en ik heb 2 dictionary's gemaakt
# 1 met de voetbal vragen en 1 met de random vragen en dan maak ik een function die de vragen en antwoorden checkt
# en die ook gelijk de scores bijhoudt en aan het einde print ik de score

start()
def spel_spelen():
    score = 0
    scorerandom = 0
    total = len(voetbal_vragen)
    for vraag, antwoord in voetbal_vragen.items():
        speler = input(f"{vraag}: ").lower()
    if speler == antwoord.lower():
        score += 1
        print("Goed!!!")
    else:
        print("Fout!!!")

    for vraag, antwoord in random_vragen.items():
            speler = input(f"{random_vragen}: ").lower()
    if speler == antwoord.lower():
            scorerandom += 1
            print("Goed!!!")
    else:
        ("Fout!!!")
    

    ultimate = input("wil je de ultimate vraag beatwoorden JA of NEE, dan heb je gelijk gewonnen als je het fout hebt verlies je gelijk")
    if ultimate.lower() == "ja":
        print("GOED, Hier komt de ultieme vraag........")
        hulplijn = input("Was de hulplijn Ja Of Nee:")
        if hulplijn.lower == "ja":
            print("Oke je krijgt een hint De hint is dat diegene het EK had gewonnen in 2016")
        elif hulplijn.lower() == "nee":
            print("Oke je krijgt de hint niet") 
        ultimatevraag = input("Wie is de GOAT Ronaldo of Messi?:")
        if ultimatevraag.lower() == "ronaldo":
            print("JE HEBT GEWONNEN!!!!!!!!!!!!!")
            exit()
        else:
            print("Je hebt het FOUT!!")
            print("GAME OVER!!!")
            exit()
    else:
        print("IS GOED dan gaat de game verder....")
    # als je minder dan 6 vragen goed hebt verlies je anders win je
    prestatie = score + scorerandom
 
    print ("Je hebt" ,prestatie, "van de 12 vragen goed")  
    if prestatie > 4:
        print("GG WELL PLAYED YOU HAVE WON THE GAME")
spel_spelen()