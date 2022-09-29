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
praktijkdieren = int(input("Hoeveel jaar heeft uw praktijkervaring met dieren-dressuur?"))
praktijkjongleren = int(input("Hoeveel jaar heeft uw praktijkervaring met jongleren?"))
praktijkacrobatiek = int(input("Hoeveel jaar heeft uw praktijkervaring met acrobatiek?"))

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

if naam == "Stan":
    raise NameError("Stan is niet welkom want hij is dom")
elif naam == "Emilio":
    raise NameError("Emilio is niet welkom omdat hij een ezel is")

elif naam == "Sonny":
    raise NameError("Sonny is niet welkom omdat hij een zweter is")

if (praktijkdieren > 4 or praktijkjongleren > 5 or praktijkacrobatiek > 3) and diploma == "ja" and rijbewijs == "ja" and hoed == "ja" and (manVrouw == "vrouw" and krullen == "ja" and krullenlengte > 20) or (manVrouw == "man" and snor == "ja" and snorLengte > 10) and lengte > 150 and gewicht > 90 and certificaat == "ja":
    print("Gefeliciteerd!, uw komt in aanmerking met een sollicitatiegesprek, stuur zo snel mogelijk uw CV.")
else:
    print(f"Beste {naam}, uw voldoet helaas niet aan onze eisen, het spijt ons!")