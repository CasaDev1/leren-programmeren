def tafel_getal (aantal: int) -> str:
    for y in range(1,11):
        print(f'{aantal} x {y} = {y * aantal}')

antwoord = int(input("Van welke getal wilt u de tafel zien?: "))
tafel_getal(antwoord)