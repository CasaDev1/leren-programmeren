PRIJS_BOLLETJE = 1.10
PRIJS_HOORNTJE = 1.25
PRIJS_BAKJE = 0.75

# hier bepaal ik het aantal bolletjes:
def get_aantal_bolletjes():
    while True:
        try:
            aantal_bolletjes = int(input("Hoeveel bolletjes wilt u?"))
            if aantal_bolletjes >= 1 and aantal_bolletjes <= 3:
                break
            elif aantal_bolletjes >= 4 and aantal_bolletjes <= 8:
                print(f'Dan krijgt u van mij een bakje met {aantal_bolletjes} bolletjes.')
                break
            elif aantal_bolletjes > 8:
                print("Sorry, zulke grote bakken hebben we niet.")
        except ValueError:
            print("Sorry dat snap ik niet...")
    return aantal_bolletjes

#  hier bepaal ik of het een hoorntje of een bakje is:
def get_hoorntje_bakje(aantal_bolletjes):
    if aantal_bolletjes >= 4 and aantal_bolletjes <= 8:
        print(f"Hier is uw bakje met {aantal_bolletjes} bolletje(s).")
        dict_bak_of_hoorn["bakje"] += 1
        return "bakje"

    while True:
        vraag_hoorntje_bakje = input(f'Wilt u deze {aantal_bolletjes} bolletje(s) in een hoorntje of een bakje?')
        if vraag_hoorntje_bakje == 'hoorntje':
            print(f'Hier is uw {vraag_hoorntje_bakje} met {aantal_bolletjes} bolletje(s).')
            dict_bak_of_hoorn['hoorntje'] += 1
            break
        elif vraag_hoorntje_bakje == 'bakje':
            print(f'Hier is uw {vraag_hoorntje_bakje} met {aantal_bolletjes} bolletje(s).')
            dict_bak_of_hoorn['bakje'] += 1
            break
        else:
            print("Sorry, dat snap ik niet..")
    return vraag_hoorntje_bakje

dict_ijsjes = []

dict_bak_of_hoorn = {'bakje': 0,
                'hoorntje': 0}

# dit is voor dat de de bolletjes wel doortelt voor het bonnetje 
def totaal_aantal_bollen(aantal_bolletjes):
    dict_ijsjes.append(aantal_bolletjes)
    totaal = sum(dict_ijsjes)
    return totaal

#  hier vraag ik of u meer wilt bestellen:
def meerBestellen():
    while True:
        meer_bestellen_vraag = input("Wilt u nog meer bestellen ja of nee?")
        if meer_bestellen_vraag == "ja":
            return True
        elif meer_bestellen_vraag == "nee":
            return False
        else:
            print("Sorry, dat snap ik niet..")

#hier bereken ik de bon
dict_smaken = {'aardbei' : 0,
                   'chocolade' : 0,
                   'munt': 0,
                   'vanille' : 0}
    

def bonnetje(totaal_bollen):
    prijs_alle_bakjes = (dict_bak_of_hoorn['bakje'] * PRIJS_BAKJE)
    prijs_alle_hoorntjes = (dict_bak_of_hoorn['hoorntje'] * PRIJS_HOORNTJE)
    prijs_alle_bollen = (totaal_bollen * PRIJS_BOLLETJE)
    
    bonnetje_maken = ''
    
    bonnetje_maken += (f' --------------------["Papi Gelato"]--------------------\n')
    bonnetje_maken += (    f'Bolletjes {totaal_bollen} x {PRIJS_BOLLETJE} = € {prijs_alle_bollen:.2f}\n') # die 2f is voor het afronden met 2 decimalen

    if dict_smaken['aardbei'] >= 1:
        bonnetje_maken += (f'B.aardbei {dict_smaken["aardbei"]} x {PRIJS_BOLLETJE:.2f} = {dict_smaken["aardbei"] * PRIJS_BOLLETJE:.2f}\n')
   
    if dict_smaken['vanille'] >= 1:
        bonnetje_maken += (f'B.vanille {dict_smaken["vanille"]} x {PRIJS_BOLLETJE:.2f} = {dict_smaken["vanille"]} * {PRIJS_BOLLETJE:.2f}\n')
   
    if dict_smaken['chocolade'] >= 1:
        bonnetje_maken += (f'B.chocolade {dict_smaken["chocolade"]} x {PRIJS_BOLLETJE:.2f} = {dict_smaken["chocolade"]} * {PRIJS_BOLLETJE:.2f}\n')
    
    if dict_smaken['munt'] >= 1:
        bonnetje_maken += (f'B.munt {dict_smaken["munt"]} x {PRIJS_BOLLETJE:.2f} = {dict_smaken["munt"]} * {PRIJS_BOLLETJE:.2f}\n')

    if dict_bak_of_hoorn["hoorntje"] >= 1:      
        bonnetje_maken += (   f'Hoorntje  {dict_bak_of_hoorn["hoorntje"]} x {PRIJS_HOORNTJE} = $ {prijs_alle_hoorntjes:.2f}\n')

    if dict_bak_of_hoorn["bakje"] >= 1:      
        bonnetje_maken += (   f'Bakjes {dict_bak_of_hoorn["bakje"]} x {PRIJS_BAKJE} = $ {prijs_alle_bakjes:.2f}\n')  
    
    bonnetje_maken += ('-------------------------------------------------------- +\n')
    Totaal = prijs_alle_bakjes + prijs_alle_bollen + prijs_alle_hoorntjes
    bonnetje_maken += (f'Totaal            = € {Totaal:.2f}\n')
    bonnetje_maken += (     'Bedankt en tot ziens!\n')
    print(bonnetje_maken)

def smaken(aantal_bolletjes):
    while True:
        try:
            for x in range(aantal_bolletjes):
                smaak_vraag = input("Welke smaak wilt u voor bolletje nummer {x}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?")
                if smaak_vraag == "a".lower():
                    dict_smaken['aardbei'] += 1
                if smaak_vraag == "c".lower():
                    dict_smaken['chocolade'] += 1
                if smaak_vraag == "m".lower():
                    dict_smaken['munt'] += 1
                if smaak_vraag == "v".lower():
                    dict_smaken['vanille'] += 1
                if x == aantal_bolletjes:
                    break
        except NameError:
            print("Sorry dat snap ik niet!")
        return dict_smaken