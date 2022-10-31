vraag_iphone = 'Hoe duur is de Iphone telefoon ?'
vraag_samsung = 'Hoe duur is de Samsung telefoon ?'
vraag_budget = 'wat is uw budget ?'



antwoord_iphone = int(input(vraag_iphone))
antwoord_samsung =int(input(vraag_samsung))
antwoord_budget = int(input(vraag_budget))
verschil_samsung_iphone = antwoord_iphone - antwoord_samsung

if verschil_samsung_iphone > 50:
    
    print(f'De iphone kost u {antwoord_iphone} en is meer dan 50 euro duurder dan de Samsung. Als advies geven we je mee dat je beter de Samsung kunt kopen.')



if verschil_samsung_iphone < 50:

    print(f'de iphone kost u {antwoord_iphone} en is niet meer dan 50 euro duurder dan de Samsung. We raden u aan om de Iphone te kopen')

   

if antwoord_samsung > antwoord_iphone:

    print(f'de Samsung kost u {antwoord_samsung} en is duurder dan de Iphone. Als advies geven we je mee dat je beter de Iphone kunt kopen.')



if antwoord_iphone == antwoord_samsung + 50:

    print(f'de iphone kost u {antwoord_iphone} en is niet meer dan 50 euro duurder dan de Samsung. We raden u aan om de Iphone te kopen')

     

if antwoord_iphone and antwoord_samsung > antwoord_budget:

    print(f'De Iphone en samsung die u wilt kopen kosten meer dan uw {antwoord_budget} dus raad ik u aan om geen iphone te kopen')



if antwoord_iphone > antwoord_budget > antwoord_samsung:

    print('De iphone die u wilt kopen gaat over uw budget heen maar de samsung is onder uw budget dus raad ik aan om die te halen')



if antwoord_samsung > antwoord_budget > antwoord_iphone:

    print('de Samsung die u wilt kopen gaat over uw budget heen maar de Iphone is onder uw budget dus raad ik aan om die te halen')



if antwoord_budget > antwoord_samsung and antwoord_iphone:

    print('Beide telefoons vallen onder uw budget dus kunt u ze allebei halen')

