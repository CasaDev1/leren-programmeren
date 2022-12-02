dagtuple = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")
print("alle dagen:")
for m in dagtuple:
    print(m)

print("werkdagen:")
for p in dagtuple[:5]:
    print(p)

print("dagen van het weekend:")
for t in dagtuple[5:7]:
    print(t)

print("dagen van de week omgekeerd: ")
for k in reversed(dagtuple):
    print(k)
    
print("werkdagen omgekeerd: ")
for g in reversed(dagtuple[:5]):
    print(g)

print("weekend omgekeerd: ")
for y in reversed(dagtuple[5:7]):
    print(y)