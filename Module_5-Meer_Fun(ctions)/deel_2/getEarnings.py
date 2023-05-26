def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []

    # haal de juiste inhoud op
    adventuringFriends = []
    interestingInvestors = []
    adventuringInvestors = []
    investorsCuts = []
    goldCut = 0.0

    # verdeel de uitkomsten
    for person in people:
        #code aanvullen

        earnings.append({
            'name'   : '??',
            'start'  : 0.0,
            'end'    : 0.0
        })

    return earnings