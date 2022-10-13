lengte =int(input("voor een de lengte in"))
breedte = int(input("voor een de breedte in"))
diep = int (input("voor in hoe diep het zwembad is"))
afmeting = lengte * breedte * diep
print(f"{afmeting} m3")

uitgraven_kosten = int(afmeting * 25)
afvoerengrond_kosten = int(afmeting * 32.50)
voorrijkosten = 250 + 20.50
totaal = uitgraven_kosten + afvoerengrond_kosten


print(f" Offerte voor een zwembad van {lengte} bij {breedte} bij {diep} meter(inhoud:{afmeting} m3")
print(f" Uitgraven:          €{uitgraven_kosten}")
print(f"Afvoeren grond:      €{afvoerengrond_kosten}")
print(f"Voorrijksten:        €{voorrijkosten}")
print(f"Totaal:              €{totaal}")
