score = 0
scorerandom = 0
total = 12
def start():
    print("====================================================")
    print("         RANDOM WIE BEN IK VOETBAL EDITIE           ")
    print("====================================================")
    welkom = input("Welkom bij WIE BEN IK VOETBAL EDITIE Ben je er klaar voor ja of nee:")
    if welkom == "ja":
        print("Top! leuk dat je er klaar voor bent! de GAME gaat beginnen")
    elif welkom == "nee":
        print("Ainah! Je bent echt een dom persoon stop maar gelijk")
        print("GAME OVER!!!")
        exit()
    hulplijn = (input("wil je de hulplijn inschakelen?:"))
    if hulplijn.lower() == "ja":
        print("Oke ik onthoud het voor de ultieme vraag.......")
    else:
        print(" Oke Hier komen de vragen!")
    return start
start()
def vragen():
    messi = input("Hij is een Argentijn en hij speelde bij Barcalona en is 1 van de beste in de wereld. Kies A = Di Maria B = Messi C =Ronaldo:")
    if messi.lower() == "b":
        print("je hebt het GOED hiervoor krijg je 1 punt")
        score += 1
    else:
        print("Helaas je hebt de vraag FOUT!")
        randomvraag1 = input("Hoeveel dagen doet de aarde erover om 1 keer om de zon te draaien?:")
        if randomvraag1.lower() == "365 dagen":
            print("je hebt de random vraag GOED dus je krijgt als nog een punt")
            scorerandom += 1
        else:
            print("HELAAS je hebt de random vraag FOUT dus je krijgt als nog geen punt JE BENT ECHT DOM!")

    bergwijn = input("Hij is van surinaamse achtergrond speelt bij Nederland en is pas naar Ajax gegaan.Kies A= Berghuis B= Bergwijn C= Frenkie:")
    if bergwijn.lower() == "b":
            print("je hebt het GOED hiervoor krijg je 1 punt")
            score += 1
    else:
            print("Helaas je hebt de vraag FOUT!")
            randomvraag2 = input("Welke planeet is de grootste in ons zonnestelsel?:")
            if randomvraag2.lower() == "jupiter":
                print("je hebt de random vraag GOED dus je krijgt als nog een punt")
                scorerandom += 1
            else:
                print("HELAAS je hebt de random vraag FOUT dus je krijgt als nog geen punt JE BENT ECHT ZO DOM!")

    ronaldo = input("Hij is een Portugees en heeft bij Real Madrid gespeeld. Kies A = Cristiano Ronaldo B= Ronaldo Lima C= Bruno:")
    if ronaldo.lower() == "a":
        print("je hebt het GOED hiervoor krijg je 1 punt")
        score += 1
    else:
        print("Helaas je hebt de vraag FOUT!")
        randomvraag3 = input("Wat is de hoofdstad van Japan?:")
        if randomvraag3.lower() == "tokyo":
            print("je hebt de random vraag GOED dus je krijgt als nog een punt")
            scorerandom += 1
        else:
            print("HELAAS je hebt de random vraag FOUT dus je krijgt als nog geen punt JE BENT ECHT ZO DOM!")

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

    haaland = input("Hij komt uit Noorwegen speelt pas bij Man City en is een spits. kies A= Gabriel B= Choupo-Moting C= Haaland:")
    if haaland.lower() == "c":
        print("je hebt het GOED hiervoor krijg je 1 punt")
        score += 1
    else:
        print("Helaas je hebt de vraag FOUT!")
        randomvraag4 = input("Hoe worden wegen waarvoor je moet betalen om erop te mogen rijden genoemd?:")
        if randomvraag4.lower() == "tolwegen":
            print("je hebt de random vraag GOED dus je krijgt als nog een punt")
            scorerandom += 1
        else:
            print("HELAAS je hebt de random vraag FOUT dus je krijgt als nog geen punt JE BENT ECHT ZO DOM!")
            print("GAME OVER!!!")
            exit()

    lewandowski = input("Het is een poolse spits die pas geleden naar Barcalona is gegaan. kies A= Lewandowski B= Szczęsny C=Kante:")
    if lewandowski.lower() == "b":
        print("je hebt het GOED hiervoor krijg je 1 punt")
        score += 1
    else:
        print("Helaas je hebt de vraag FOUT!")
        randomvraag5 = ("Welke voetbalclub heeft het grootste voetbalstadion van Nederland?:")
        if randomvraag5.lower() == "ajax":
            print("je hebt de random vraag GOED dus je krijgt als nog een punt")
            scorerandom += 1
        else:
            print("HELAAS je hebt de random vraag FOUT dus je krijgt als nog geen punt JE BENT ECHT ZO DOM!")

    mbappe = input("Het is Fransman die voor PSG speelt en is een spits en is op dit moment 1 van de snelste voetballers nu. Kies A= Mbappe B= Ben yedder C= Benzema:")
    if mbappe.lower() == "a":
        print("je hebt het GOED hiervoor krijg je 1 punt")
        score += 1
    else:
        print("Helaas je hebt de vraag FOUT!")
        randomvraag6 = input("Wanneer eindigde de eerste wereldoorlog?:")
        if randomvraag6.lower() == "1918":
            print("je hebt de random vraag GOED dus je krijgt als nog een punt")
            scorerandom += 1
        else:
            print("HELAAS je hebt de random vraag FOUT dus je krijgt als nog geen punt JE BENT ECHT ZO DOM!")
    return vragen

vragen()
# als je minder dan 6 vragen goed hebt verlies je anders win je
prestatie = score + scorerandom
 
print ("Je hebt" ,prestatie, "van de 12 vragen goed")  
if prestatie > 4:
    print("GG WELL PLAYED YOU HAVE WON THE GAME")