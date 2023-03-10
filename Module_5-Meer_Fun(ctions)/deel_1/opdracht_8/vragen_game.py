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







voetbal_vragen = {
        'Hij is een Argentijn en hij speelde bij Barcalona en is 1 van de beste in de wereld. Kies A = Di Maria B = Messi C =Ronaldo' : "b",
        'Hij is van surinaamse achtergrond speelt bij Nederland en is pas naar Ajax gegaan.Kies A= Berghuis B= Bergwijn C= Frenkie': "b",
        'Hij is een Portugees en heeft bij Real Madrid gespeeld. Kies A = Cristiano Ronaldo B= Ronaldo Lima C= Bruno' : "a",
        'Hij komt uit Noorwegen speelt pas bij Man City en is een spits. kies A= Gabriel B= Choupo-Moting C= Haaland': "c",
        'Het is een poolse spits die pas geleden naar Barcalona is gegaan. kies A= Lewandowski B= Szczęsny C=Kante' : "a",
        'Het is Fransman die voor PSG speelt en is een spits en is op dit moment 1 van de snelste voetballers nu. Kies A= Mbappe B= Ben yedder C= Benzema' : "a",
    }
random_vragen = {
        'Hoeveel dagen doet de aarde erover om 1 keer om de zon te draaien?' : "365 dagen",
        'Welke planeet is de grootste in ons zonnestelsel?' : "jupiter",
        'Wat is de hoofdstad van Japan?' : "tokyo",
        'Hoe worden wegen waarvoor je moet betalen om erop te mogen rijden genoemd?' : "tolwegen",
        'Welke voetbalclub heeft het grootste voetbalstadion van Nederland?' : "ajax",
        'Wanneer eindigde de eerste wereldoorlog?' : "1918",
    }