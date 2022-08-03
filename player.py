coins = 0
health = 10

def playerName():
    name = input("Please enter your name: ")
    return name

def playerHealth():
    health = 10
    health = str(health)
    return health

def playerAttack():
    attack = 5
    attack = str(attack)
    return attack

def playerCoins():

    global coins
    import monster
    monNum = monster.monsterNumber()

    if monNum == 1:
        coins = int(coins) + 5
    if monNum == 2:
        coins = int(coins) + 10
    if monNum == 3:
        coins = int(coins) + 15
    return coins

def updateHealth():
    global health
    health = health + 5
    return health

def coinsHealth():
    global coins
    coins = int(coins) - 20
    return coins
