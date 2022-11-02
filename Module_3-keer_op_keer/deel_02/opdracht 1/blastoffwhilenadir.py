from time import sleep

m = 30
vertraging = 1
print("de raketlancering gaat beginnen!!!")
while m > 0:
    print(m)
    m = m - 1
    sleep(vertraging)

print("de raket is gelanceerd!!!!")