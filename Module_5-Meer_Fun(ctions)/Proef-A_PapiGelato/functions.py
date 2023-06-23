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
            elif aantal_bolletjes > 8:
                print("Sorry, zulke grote bakken hebben we niet.")
        except ValueError:
            print("Sorry dat snap ik niet...")
    return aantal_bolletjes

#  hier bepaal ik of het een hoorntje of een bakje is:
def get_hoorntje_bakje(aantal_bolletjes):
    if aantal_bolletjes >= 4 and aantal_bolletjes <= 8:
        print(f"Hier is uw bakje met {aantal_bolletjes} bolletje(s).")
        return "bakje"

    while True:
        vraag_hoorntje_bakje = input(f"Wilt u deze {aantal_bolletjes} bolletje(s) in een hoorntje of een bakje?")
        if vraag_hoorntje_bakje == "hoorntje" or vraag_hoorntje_bakje == "bakje":
            print(f"Hier is uw {vraag_hoorntje_bakje} met {aantal_bolletjes} bolletje(s).")
            break
        else:
            print("Sorry, dat snap ik niet..")
    return vraag_hoorntje_bakje


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
def bonnetje(aantal_bolletjes, vraag_hoorntje_bakje):
    if vraag_hoorntje_bakje == "bakje":
        prijs = PRIJS_BAKJE
        type = "bakje"
    else:
        prijs = PRIJS_HOORNTJE
        type = "hoorntje"
    totale_kosten = aantal_bolletjes * PRIJS_BOLLETJE + prijs
    print('\n--- ["PapiGelato"]---')
    print(f"Aantal bolletjes: {aantal_bolletjes}")
    print(f"Type: {type}")
    print(f"Totale kosten: €{totale_kosten:.2f}")
    print("Bedankt en tot ziens!\n")