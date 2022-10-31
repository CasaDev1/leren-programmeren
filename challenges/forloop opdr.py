gastheer = input("wie is de gastheer")
gasten = 4
drank = False
chips = True

if gastheer != "corbijn" and (gastheer == "rudi" or (drank and (gasten >= 4 and gastheer))):
    print("Start the Party")
else:
    print("No Party")