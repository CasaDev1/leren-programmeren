n = 50 
d = "50"
answer = 50
while answer < 1000:
    n = n + 1
    d = f"{d} + {n}"
    answer = answer + n
    print(f"{d} = {answer}")