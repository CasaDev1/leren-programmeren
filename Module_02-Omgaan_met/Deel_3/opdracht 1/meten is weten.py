a = int(input("geef een getal"))
b = int(input("geef een getal"))

Max = a
Min = b

if a > b:
    print(f"a is het grootste getal: {Max}")
elif a < b:
    print(f"b is het kleinste getal: {Min}")
else:
    print(f"a en b zijn even groot")

print(f"het minimum is: {Min}")
print(f"het maximum is: {Max}")
