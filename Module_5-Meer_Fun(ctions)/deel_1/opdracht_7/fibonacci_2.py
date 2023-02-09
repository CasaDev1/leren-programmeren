def fibonacci(lijst, lengte):
    if len(lijst) >= lengte:
        return lijst
    else:
        lijst.append(lijst[-1] + lijst[-2])
        return fibonacci(lijst, lengte)
        

print(fibonacci([0, 1], 50))
