gastheer = input("wie is de gastheer")
gasten = 4
drank = True
chips = True
doritos_chips = False
if gastheer != "rudi" and drank and (gastheer == "abdi" or (doritos_chips and (gasten >= 4 and gastheer))):
    print("Start the Party")
else:
    print("No Party")