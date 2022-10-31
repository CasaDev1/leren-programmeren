zin = input("voer een zin in")
zin2 = ""
woord = ""

for c in zin:

    if c == " ":
        zin =+ woord + " " + woord + " "
        woord = ""
    else:
        woord += c

zin2 += woord + " " + woord

print(zin2)
