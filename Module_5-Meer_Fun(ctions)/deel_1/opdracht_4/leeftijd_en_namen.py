
def namen_en_leeftijden() -> dict:
    namen_leeftijd_dict = {}
    naamvraag = input("Wat is je naam? voer 'klaar'in als je klaar bent: ")
    if naamvraag == "klaar":
        leeftijdvraag = 0
    else:
        leeftijdvraag = int(input("Wat is je leeftijd? type 'klaar' als je klaar bent: "))
    namen_leeftijd_dict["naam"] = naamvraag
    namen_leeftijd_dict["leeftijd"] = leeftijdvraag        
    return namen_leeftijd_dict 



namen_leeftijd_lijst = []
     
while True:
    mijn_dict = namen_en_leeftijden()
    if mijn_dict['naam'] != "klaar":
        namen_leeftijd_lijst.append(mijn_dict)
    else:
        break    
for y in namen_leeftijd_lijst:
    namen = y["naam"]
    leeftijden = y["leeftijd"]
    print(f"{namen} is {leeftijden} jaar")
    