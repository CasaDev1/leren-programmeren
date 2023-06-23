from functions import *

print("Welkom bij Papi Gelato!")

meer_bestellen = "ja"

while True:
    aantal_bolletjes = get_aantal_bolletjes()
    verpakking = get_hoorntje_bakje(aantal_bolletjes)
    if not meerBestellen():
        bonnetje(aantal_bolletjes, verpakking)
        break