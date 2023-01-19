# def vraag_getal(vraag: str) -> int:
#     while True:
#         try:
#             getal = int(input(vraag))
#             break
#         except ValueError:
#             print("je moet wel een getal invullen")
#             continue
#     return getal


# leeftijd = vraag_getal("voer een leeftijd in: ")    
# print(leeftijd)

# def invoeren_naam(question: str) -> str:
#     naam = input("voer je naam in")
#     naam = naam.lower()
#     return naam

# namen= invoeren_naam("voer je voornaam in: ")
# print(namen)

def hallo_naam(vraag: str) -> str:
    vraag_naam = input("wat is je naam: ")
    vraag_naam = vraag_naam
    return (f"hallo {vraag_naam}")

namen_hallo= hallo_naam("wat is je naam?: ")
print(namen_hallo)