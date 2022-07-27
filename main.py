import player
import monster
import random

dead = 0

health = player.playerHealth()
attack = player.playerAttack()
name = player.playerName()

monster = monster.Enemy()
monHealth = monster.monsterHealth(20)
monName = monster.monsterName("John")

monHealth = str(monHealth)

print()
print("Name: " + name)
print("Health: " + health)
print("Attack: " + attack)

print()
print("Monster Name: " + monName)
print("Monster Health: " + monHealth)


while monHealth != dead:

    choice = input("Do you want to attack? Enter 'Yes' or 'No': ")

    if choice == "Yes" or choice == "yes":
        monHealth = int(monHealth)
        attack = int(attack)
        monHealth = monHealth - attack
        print()
        
        if monHealth >= dead:
           print(monName + " health is at " + str(monHealth))

           monAttack = monster.monsterAttack(random.randint(2, 5))
           health = int(health) - monAttack
           print("The monster hit you for " + str(monAttack))

           if health <= dead:
               choice = "No"
               health = dead

           print("Your health is at " + str(health))
           print()

        elif monHealth <= dead:
            print("You have vanquished the monster")
            monHealth = dead



    if choice == "No" or choice == "no":
        print("You have been eaten")
        print("Game Over")
        health <= dead
        monHealth = health

    else: 
        print("Please enter in 'Yes' or 'No': ")
