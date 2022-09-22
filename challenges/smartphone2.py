iphone_13 = int(input("hoe duur is de iphone 13?"))
samsung_galaxy_s22 = int(input ("hoe duur is de samsung galaxy s22?"))

iphone13 = "iphone 13"
samsungs22 = "Samsung galaxy s22"
if iphone_13 > 50:
    print(iphone_13)
if samsung_galaxy_s22 > 50:
    print (samsung_galaxy_s22)    

if iphone_13 > samsung_galaxy_s22:
    print(f"De {iphone13} is het duurst, de telefoon kost:{iphone_13}Euro")
elif iphone_13 < samsung_galaxy_s22:
    print(f"De {samsungs22} is het duurst,de telefoon kost:{samsung_galaxy_s22}Euro")

if iphone_13 < samsung_galaxy_s22:
    print(f"De {iphone13} is het goedkoopst, de telefoon kost:{iphone_13}Euro")
elif iphone_13 > samsung_galaxy_s22:
    print(f"De {samsungs22} is het goedkoopst,de telefoon kost:{samsung_galaxy_s22}Euro")

if iphone_13 > samsung_galaxy_s22:
    print(f"Het advies is dus de {samsungs22} te kopen.Deze is namelijk {iphone_13 - samsung_galaxy_s22} Euro goedkoper dan de iphone 13")
elif samsung_galaxy_s22 > iphone_13:
    print(f"Het advies is dus de {iphone13} te kopen.Deze is namelijk {samsung_galaxy_s22 - iphone_13} Euro duurder dan de samsung galaxy s22")




    

