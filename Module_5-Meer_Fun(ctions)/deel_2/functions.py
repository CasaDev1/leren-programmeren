import time
import math
from termcolor import colored
from data import JOURNEY_IN_DAYS
from data import COST_FOOD_HUMAN_COPPER_PER_DAY
from data import COST_FOOD_HORSE_COPPER_PER_DAY
from data import COST_TENT_GOLD_PER_WEEK
from data import COST_HORSE_SILVER_PER_DAY
from data import COST_INN_HUMAN_SILVER_PER_NIGHT
from data import COST_INN_HORSE_COPPER_PER_NIGHT

##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5
def copper2gold(amount:int) -> float:
    return amount / 50

def platinum2gold(amount:int) -> float:
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    platinum = platinum2gold(personCash['platinum'])
    goud = personCash['gold']
    zilver = silver2gold(personCash['silver'])
    koper = copper2gold(personCash['copper'])
    totaal = platinum + goud + zilver + koper
    return totaal


##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    people_copper =  people * COST_FOOD_HUMAN_COPPER_PER_DAY * JOURNEY_IN_DAYS
    horses_copper =  horses * COST_FOOD_HORSE_COPPER_PER_DAY * JOURNEY_IN_DAYS
    totaal = people_copper + horses_copper
    return copper2gold(totaal)

##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    lijst = []
    for x in list:
        if key in x and x[key] == value:
            lijst.append(x)
    return lijst    

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, "adventuring", True)

def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs(friends, "shareWith", True)

def getAdventuringFriends(friends:list) -> list:
    nieuwe_lijst = []
    for dict in getAdventuringPeople(friends):
        if dict in getShareWithFriends(friends):
            nieuwe_lijst.append(dict)
    return nieuwe_lijst

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    paarden = horses * silver2gold(COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS
    tenten = tents * COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS / 7 )
    totaal = paarden + tenten
    return float(totaal)

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    item_tekst = []
    for item in items:
        item_tekst.append(f"{item['amount']}{item['unit']} {item['name']}")


    return ", ".join(item_tekst)

def getItemsValueInGold(items:list) -> float:
    list = []
    for item in items:
        if item['price']['type'] == 'copper':
            copper = item['amount'] * item['price']['amount']
            list.append(copper2gold(copper))
        elif item['price']['type'] == 'silver':
            silver = item['amount'] * item['price']['amount']
            list.append(silver2gold(silver))
        elif item['price']['type'] == 'platinum':
            platinum = item['amount'] * item['price']['amount']
            list.append(platinum2gold(platinum))
        else:
            goud = item['amount'] * item['price']['amount']
            list.append(goud)
    return sum(list)
#sum is dat t alles bij elkaar op telt

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    total = 0
    for w in people:
        total += platinum2gold(w['cash']['platinum'])
        total += silver2gold(w['cash']['silver'])
        total += copper2gold(w['cash']['copper'])
        total += w['cash']['gold']
    return total

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    return [x for x in investors if x["profitReturn"] <= 10]# dit is een kortere versie van een for-loop die ik dan return 
    
def getAdventuringInvestors(investors:list) -> list:
    return [x for x in investors if x["adventuring"] and x["profitReturn"] <= 10]

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    total = 0
    AdventuringInvestors = getAdventuringInvestors(investors)
    total += getItemsValueInGold(gear) * len(AdventuringInvestors)

    total += getJourneyFoodCostsInGold(len(AdventuringInvestors),len(AdventuringInvestors))
    total += getTotalRentalCost(len(AdventuringInvestors), len(AdventuringInvestors))
    return total


##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    humans = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    horses = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    total = int(leftoverGold / (humans + horses))
    return total

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    goldANight = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT)
    humans =  goldANight * people 
    horses_gold = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT)
    horse_A_Night= horses_gold * horses 
    total = round((humans + horse_A_Night) * nightsInInn,2)
    return total

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    list = []
    for investor in getInterestingInvestors(investors):
            list.append(round(investor['profitReturn'] / 100 * profitGold,2) )# round rond af op hoeveel getallen jij dat aangeeft in dit geval 2 decimalen
    return list

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    total = round((profitGold - sum(investorsCuts)) / fellowship,2)
    return total

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []
    donatie = 10

    # haal de juiste inhoud op
    adventuringFriends = getAdventuringFriends(friends)
    interestingInvestors = getInterestingInvestors(investors)
    adventuringInvestors = getAdventuringInvestors(investors)
    investorsCuts = getInvestorsCuts(profitGold,investors)
    goldCut = getAdventurerCut(profitGold, investorsCuts, len(adventuringFriends)+1 + len(adventuringInvestors))#die plus 1 is om de maincharacter erbij te tellen

    # verdeel de uitkomsten
    for person in people:
        cash = person["cash"]
        begin = getPersonCashInGold(cash)

        if person == mainCharacter:
            einde = begin + goldCut + (donatie*len(adventuringFriends))
        elif person in adventuringFriends:
            einde = round((begin + goldCut) - donatie,2)
        else:
            einde = begin

        if "profitReturn" in person:
            if person in interestingInvestors:
                if person in adventuringInvestors:
                    einde_1 = (profitGold/100)
                    einde_2 = einde_1 * person["profitReturn"]
                    einde = einde_2 + begin + goldCut
                else:
                    einde_1 = (profitGold/100)
                    einde_2 = einde_1 * person["profitReturn"]
                    einde = einde_2 + begin

                    
        

        earnings.append({
            'name'   : person["name"],
            'start'  : begin,
            'end'    : einde
        })

    return earnings

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()