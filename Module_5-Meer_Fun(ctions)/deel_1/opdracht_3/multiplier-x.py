def tafel_getal (aantal: int) -> str:
    for y in range(1,11):
        print(f'{y} x {aantal} = {y * aantal}')

antwoord = int(input("Van welke getal wilt u de tafel zien?: "))
tafel_getal(antwoord)