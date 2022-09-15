# Nadir Ait Chitt #opdracht pizzacalculator
pizza_small = 6
pizza_medium = 8
pizza_large = 11

aantal_small_pizzas = int(input("hoeveel small pizza's wilt u?"))
aantal_medium_pizzas = int(input("hoeveel medium pizza's wilt u?"))
aantal_large_pizzas = int(input("hoeveel large pizza's wilt u?"))

prijs_small = int(aantal_small_pizzas * pizza_small)
prijs_medium = int(aantal_medium_pizzas * pizza_medium)
prijs_large = int(aantal_large_pizzas * pizza_large)

print(f"{aantal_small_pizzas} small pizza €{pizza_small} €{prijs_small}  ")
print(f"{aantal_medium_pizzas} medium pizza €{pizza_medium} €{prijs_medium}  ")
print(f"{aantal_large_pizzas} large pizza €{pizza_large} €{prijs_large}  ")