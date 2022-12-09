boodschappen_tas_dic = {

}


while True:
    vraagboodschap = input("Voeg een product toe aan het lijst (typ hier): ")
    if vraagboodschap in boodschappen_tas_dic:
        boodschappen_tas_dic[vraagboodschap] += 1
    else: 
        boodschappen_tas_dic.update({vraagboodschap : 1})
    voeg_product = input("wil je nog een product toe(typ hier):")
    if voeg_product == "ja":
        continue
    else:
        break
print("[BOODSCHAPPENLIJST]")
for key,value in boodschappen_tas_dic.items():
    print(f"{value}x {key}")
print("------------------------")