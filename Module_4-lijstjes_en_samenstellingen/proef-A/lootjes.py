import random
namen = []
namen2 = []
teller = 0
vraag = input("Wilt u lootjes trekken?: ").lower()
if vraag == "ja":
    while True:
        name = input("Voer een naam in (voer 'klaar' in om lootjes te trekken): ")
        if name == 'klaar':
            if len(namen) < 3:
                print("Er zijn minder dan 3 namen ingevoerd. Voer minimaal 3 namen in om lootjes te kunnen trekken.")
                continue
            else:
                break
        elif name in namen2:
            print("Deze naam is al ingevoerd. Voer een unieke naam in.")
        else:            
            namen.append(name)
            namen2 = list(namen)
else:
    exit()
while True:
    if namen[teller] == namen2[teller]:
        random.shuffle(namen2)
        teller = 0
    else:
        teller += 1
    if teller == len(namen):
        break
for x in range(len(namen)):
    print(f"{namen[x]} : {namen2[x]}")
