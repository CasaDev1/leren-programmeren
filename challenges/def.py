def vraag_getal(vraag: str) -> int:
    while True:
        try:
            getal = int(input(vraag))
            break
        except ValueError:
            print("je moet wel een getal invullen")
            continue
return getal