import random
menms_lijst = ["rood", "blauw", "groen", "geel", "bruin"]
hoeveel = int(input("hoeveel m&m's wilt u?: "))
zak_dic = {

}


for x in range (hoeveel):
    color = random.choice(menms_lijst)
    if color not in zak_dic:
        zak_dic.update({color : 1})
    elif color in zak_dic:
        zak_dic[color] += 1

print(zak_dic)
