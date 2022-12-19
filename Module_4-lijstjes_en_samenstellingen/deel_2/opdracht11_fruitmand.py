from fruitmand import fruitmand
rond_fruit = 0
niet_rond_fruit = 0
d = False
while d == False:
      kleur = input("kies een kleur(in het engels): ")
      for fruit in fruitmand:
            if fruit['color'] == kleur:
                  d = True
                  
                  if fruit['round'] == True:
                        rond_fruit += 1
                              
                  else:
                        niet_rond_fruit += 1
                  
                  if rond_fruit > niet_rond_fruit:
                        print(f"Er zijn {rond_fruit - niet_rond_fruit} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur}")
                                          
                  elif rond_fruit < niet_rond_fruit:
                        print(f"Er zijn {niet_rond_fruit - rond_fruit} minder ronde vruchten dan niet ronde vruchten in de kleur {kleur}")
                                          
                  elif rond_fruit == niet_rond_fruit:
                        print(f"Er zijn {rond_fruit} ronde vruchten en {niet_rond_fruit} niet ronde vruchten in de kleur {kleur}")
                  exit() 
                        
      else:
            print(f"{kleur} zit er niet in")
    
            




    

    