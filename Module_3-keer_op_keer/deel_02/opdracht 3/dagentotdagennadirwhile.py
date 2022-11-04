dagenweek = ["1= maandag" , "2= dinsdag" , "3= woensdag", "4= donderdag","5= vrijdag", "6= zaterdag", "7= zondag"]
kiesdag = int(input("kies een dag uit de week(in cijfers):"))
w = 0
while w < kiesdag:
    print(dagenweek[w])
    w = w + 1