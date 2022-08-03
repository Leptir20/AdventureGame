import random

number = 1

def monsterName():
    if randomChoice == 1:
        monsterName = "John"
    if randomChoice == 2:
        monsterName = "Jim"
    if randomChoice == 3:
        monsterName = "Joe"
    return monsterName

def monsterHealth():
    if randomChoice == 1:
        monsterHealth = 10
    if randomChoice == 2:
        monsterHealth = 10
    if randomChoice == 3:
        monsterHealth = 10
    return monsterHealth

def monsterAttack():
    if randomChoice == 1:
        monsterAttack = 2
    if randomChoice == 2:
        monsterAttack = 2
    if randomChoice == 3:
        monsterAttack = 2
    return monsterAttack

def monsterNumber():
    if randomChoice == 1:
        monsterNumber = 1
    if randomChoice == 2:
        monsterNumber = 2
    if randomChoice == 3:
        monsterNumber = 3
    return monsterNumber

def randomMonster():
    randomChoice = ""
    randomChoice = random.randint(1,3)
    return randomChoice

while number == 1:
    randomChoice = randomMonster()
    monsterName()
    monsterHealth()
    monsterAttack()
    break
