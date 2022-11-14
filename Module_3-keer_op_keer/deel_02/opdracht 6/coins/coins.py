# name of student: Nadir
# number of student: 99073112
# purpose of program: het wissel geld berekenen en het geven 
# function of program: het berekend het wisselgeld en het laat zien hoeveel je van een bepaalde munt hebt gegeven
# structure of program: Er wordt gebruik gemaakt van inputs , if , while , variable , exeptions en operators
vijfeuro = 500
tweeeuro = 200
eeneuro = 100
vijftigcent = 50
twintigcent = 20
tiencent = 10
vijfcent = 5
tweecent = 2
eencent = 1

toPay = int(float(input('Amount to pay: '))* 100) #
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay # dit is de wisselgeld variable 

if change > 0: # als het wisselgeld groter dan nul is dan begint het programma
  coinValue = 500 # de beginwaarde van de coin
  
  while change > 0 and coinValue > 0: # dit is de start van de while loop en de loop stopt pas als de waarde wordt gegeven
    nrCoins = change // coinValue # bereking van de change gedeeld door de waarde en dan krijg je nrCoins

    if nrCoins > 0: # als er nog een coin word gegeven dan start de IF
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #hij laat zien hoeveel munten van een coin kan gegeven
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # hier vraagt die hoeveel coins je wilt geven
      change -= nrCoinsReturned * coinValue # change is min de aantal coins dat is ingevoerd 



# comment on code below: en hier gaat die langs alle coins 
    if coinValue == vijfeuro:
      pan = nrCoinsReturned
      coinValue = tweeeuro
    elif coinValue == tweeeuro:
      pan1 = nrCoinsReturned
      coinValue = eeneuro
    elif coinValue == eeneuro:
      pan2 = nrCoinsReturned 
      coinValue = vijftigcent
    elif coinValue == vijftigcent:
      pan3 = nrCoinsReturned
      coinValue = twintigcent
    elif coinValue == twintigcent:
      pan4 = nrCoinsReturned
      coinValue = tiencent 
    elif coinValue == tiencent:
      pan5 = nrCoinsReturned
      coinValue = vijfcent 
    elif coinValue == vijfcent:
      pan6 = nrCoinsReturned
      coinValue = tweecent
    elif coinValue == tweecent:
      pan7 = nrCoinsReturned
      coinValue = eencent 
    else:
      coinValue = 0 



try:
  if change > 0: #Hier laat hij de change zien dat is ingevuld plus als de change niet compleet is terug gegeven 
    print('Change not returned: ', str(change) + ' cents')
  else:
    print(f"{vijfeuro}: {pan}")
    print(f"{tweeeuro}: {pan1}")
    print(f"{eeneuro}: {pan2}")
    print(f"{vijftigcent}: {pan3}")
    print(f"{twintigcent}: {pan4}")
    print(f"{tiencent}: {pan5}")
    print(f"{vijfcent}: {pan6}")
    print(f"{tweecent}: {pan7}")
except NameError:
  print("done")
  exit()