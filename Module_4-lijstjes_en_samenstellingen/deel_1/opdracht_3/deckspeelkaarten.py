import random
kaarten = ["schoppen", "ruiten", "harten", "klaver"]
specialcards = ["boer", "vrouw", "heer", "aas"]
jokers = ["joker", "joker2"]
deck = []

for n in kaarten:
    for m in specialcards:
        deck.append(f"{n} {m}")
    for z in range(2, 11, 1):
        deck.append(f"{n} {z}")

random.shuffle(deck)

for v in range(1,8):
    speelkaart = random.choice(deck)
    print(f"kaart {v}: {speelkaart}")
    deck.remove(speelkaart)
print(f"de overige kaarten: (47 kaarten):{deck}")

