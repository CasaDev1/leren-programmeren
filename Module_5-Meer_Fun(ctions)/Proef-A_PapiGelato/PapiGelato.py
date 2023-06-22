from functions import *

print("Welkom bij Papi Gelato!")

meer_bestellen = "ja"

while meer_bestellen == "ja":
    aantal_bolletjes = get_aantal_bolletjes()
    get_hoorntje_bakje(aantal_bolletjes)
    meer_bestellen = meerBestellen()
