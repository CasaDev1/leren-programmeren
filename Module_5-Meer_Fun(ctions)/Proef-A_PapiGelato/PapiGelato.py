from functions import *

print("Welkom bij Papi Gelato!")

meer_bestellen = "ja"

while True:
    aantal_bolletjes = get_aantal_bolletjes()
    verpakking = get_hoorntje_bakje(aantal_bolletjes)
    totaal_bollen = totaal_aantal_bollen(aantal_bolletjes)
    if not meerBestellen():
        bonnetje(totaal_bollen)
        break