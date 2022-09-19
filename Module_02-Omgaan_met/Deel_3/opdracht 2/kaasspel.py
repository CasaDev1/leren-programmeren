kaas = input("is de kaas geel?")
if kaas == "ja":
    gaten = input("zitten er gaten in?")
    if gaten == "ja":
        duur = input("is de kaas belachelijk duur?")
        if duur == "ja":
            print("Emmenthaler")
        elif duur == "nee":
            print("Leerdammer")
    elif gaten == "nee":
        hard = ("is de kaas hard als steen?")
        if hard == "ja":
            print("Parmigiano Reggiano")  
        elif hard == "nee":
            print("Goudse Kaas")  
elif kaas == "nee":
    schimmel = input("Heeft de kaas blauweschimmel?")
    if schimmel == "ja":
        korsten = input("heeft de kaas een korst?")
        if korsten == "ja":
            print("Blue de Rochbaron")
        elif korsten == "nee":
            print("Foume d'Ambert")
    elif schimmel == "nee":
        korsten2 = input("heeft de kaas een korst?")
        if korsten2 == "ja":
            print ("Camembert")
        elif korsten2 == "nee":
            print("Mozzarella")

    
    
    