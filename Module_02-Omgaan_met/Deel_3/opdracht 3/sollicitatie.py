print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++
         +      SollicitatieFormulier "Vrachtwagenchaffeur"      +
         +++++++++++++++++++++++++++++++++++++++++++++++++++++++
         Er wordt u een aantal relevante vragen gesteld...
         Gelieve die naar eer en geweten in te vullen
         Als blijkt dat u aan de criteria voldoet dan komt u in
         Aanmerking voor een sirieus sollicitatiegesprek!
         Ontspan maar blijf wakker, hier komen de vragen
         +++++++++++++++++++++++++++++++++++++++++++++++++++++++""")

naam = input(" wat is uw naam?")
diploma = input("Bent uw in bezit van een MBO 4 Ondernemen diploma? ja/nee:")
praktijk = int(input("Hoeveel jaar heeft uw praktijkervaring met dieren-dressuur?"))
rijbewijs = input("Bent uw in bezit van een geldig Vrachtwagen rijbewijs? ja/nee:")
hoed = input("Bent uw in bezit van een hoed? ja/nee:")
manVrouw = input("Bent uw een man of een vrouw?:")

if manVrouw == "man":
    snor = input("Heeft uw een snor? ja/nee:")
    if snor == "ja":
        snorLengte = int(input("Hoelang is uw snorlengte? (in cm):"))

elif manVrouw == "vrouw":
    krullen = input("Heeft uw rood krullend haar? ja/nee:")
    if krullen == "ja":
        krullenlengte = int(input("Hoelang is uw rood krullend haar? (in cm):"))


lengte = int(input("Wat is uw lengte? (in cm)"))
gewicht = int(input("Wat is uw gewicht (in kg):"))
certificaat = input("Heeft uw een certificaat? ja/nee:")

if praktijk > 4 and diploma == "ja" and rijbewijs == "ja" and hoed == "ja" and (manVrouw == "vrouw" and krullen == "ja" and krullenlengte > 20) or (manVrouw == "man" and snor == "ja" and snorLengte > 10) and lengte > 150 and gewicht > 90 and certificaat == "ja":
    print("Gefeliciteerd!, uw komt in aanmerking met een sollicitatiegesprek, stuur zo snel mogelijk uw CV.")
else:
    print(f"Beste {naam}, uw voldoet helaas niet aan onze eisen, het spijt ons!")