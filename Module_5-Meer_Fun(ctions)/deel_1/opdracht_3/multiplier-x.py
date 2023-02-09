def tafel_getal():
    getal = int(input ("vul een getal in: "))
    for x in range (1,11):
        antwoord = x * getal
        print (f" {x} x {getal} = {antwoord}")
tafel_getal()