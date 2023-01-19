def fibonacci(aantal: int) -> list:
    lijst = [0,1]
    for x in range(aantal):
        lijst.append(lijst[x] + lijst[x + 1])
    snede = lijst[-1] / lijst[-2]
    return snede


print(fibonacci(10))