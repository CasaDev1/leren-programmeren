lijst_landen = []
for x in range(3):
    welke_landen = input("welke 3 landen spelen in groep A: ")
    lijst_landen.append(welke_landen)
# print(lijst_landen)

lijst_score =[]
print("je gaat nu de score invoeren top!")
uistslag1 = int(input("voer de score van land 1: "))
uistslag2 = int(input("voer de score van land 2: "))
lijst_score.append(uistslag1)
lijst_score.append(uistslag2)
# print(lijst_score)
doel_punten_saldo1 = 0
doel_punten_saldo2 = 0
puntenland1 = 0
puntenland2 = 0
land1 = lijst_landen[0]
land2 = lijst_landen[1]
uitslag_land1 = lijst_score[0]
uitslag_land2 = lijst_score[1]
if uitslag_land1 > uitslag_land2:
    doel_punten_saldo1 = uitslag_land1 - uitslag_land2
    puntenland1 += 3
    

elif uitslag_land1 < uitslag_land2:
    doel_punten_saldo2 = uitslag_land1 - uitslag_land2
    puntenland2 =+ 3

print(f"{land1} - {land2} eindigde in: {uitslag_land1} - {uitslag_land2}")
print("Overzicht groep A")
print(f"{land1}: punten{puntenland1}; doelsaldo: {doel_punten_saldo1}")
print(f"{land2}: punten{puntenland2}; doelsaldo: {doel_punten_saldo2}")








    