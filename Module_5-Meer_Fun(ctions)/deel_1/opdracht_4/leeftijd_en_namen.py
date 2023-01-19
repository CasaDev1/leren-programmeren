def namen_en_leeftijden():
    namen = []
    leeftijden = []
    while True:
        naamvraag = input("Wat is je naam? voer 'klaar'in als je klaar bent: ")
        if naamvraag == "klaar":
            break
        leeftijdvraag = input("Wat is je leeftijd? type 'klaar' als je klaar bent: ")
        if leeftijdvraag == "klaar":
            break
        namen.append(naamvraag)
        leeftijden.append(leeftijdvraag)
    n = zip(namen, leeftijden)
    return n


for x,y in namen_en_leeftijden():
    print(f"{x} is {y} jaar")