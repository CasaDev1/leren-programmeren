
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
            break
        elif meer_bestellen_vraag == "nee":
            print("Bedankt en tot ziens!")
            break
        else:
            print("Sorry, dat snap ik niet..")
    return meer_bestellen_vraag
