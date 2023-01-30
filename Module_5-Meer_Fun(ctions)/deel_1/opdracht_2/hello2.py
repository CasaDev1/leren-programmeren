def mijn_function(getal):
    lijstje = []
    for k in range(1,getal+1):
        lijstje.append(f"Hello from function town {k}!")
    return lijstje
for a in mijn_function(7):
    print(a)