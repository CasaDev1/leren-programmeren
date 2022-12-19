from fruitmand import fruitmand
namen_lijst = []
kg_lijst = []
for fruit in fruitmand:
    fruitkg =  fruit['weight'] / 1000, 'kg'
    fruit_namen =fruit['name']
    namen_lijst.append(fruit_namen)
    kg_lijst.append(fruitkg)
    kg_lijst.sort(reverse=True)
  

print (kg_lijst)
print(namen_lijst)



    

    


    

    