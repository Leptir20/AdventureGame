import importlib
import player
import time

fight = "Yes"
dead = 0
shop = "Exit"

health = player.playerHealth()
attack = player.playerAttack()
name = player.playerName()
print()

print("Name: " + name)
print("Health: " + health)
print("Attack: " + attack)

while fight != "Close":

    import monster
    coins = player.playerCoins()

    monHealth = monster.monsterHealth()
    monName = monster.monsterName()
    monNum = monster.monsterNumber()
    monAttack = monster.monsterAttack()

    monHealth = str(monHealth)

    print()
    print("Monster Name: " + monName)
    print("Monster Health: " + monHealth)
    print("Monster Attack: " + str(monAttack))
    print()

    while monHealth != dead:

        choice = input("Do you want to attack? Enter 'Yes' or 'No': ")

        if choice == "Yes" or choice == "yes":
            monHealth = int(monHealth)
            attack = int(attack)
            monHealth = monHealth - attack
            print()
        
            if monHealth > dead:
               print(monName + " health is at " + str(monHealth))

               health = int(health) - int(monAttack)
               print("The monster hit you for " + str(monAttack))
               

               if health <= dead:
                   choice = "No"
                   health = dead

               print("Your health is at " + str(health))
               print()

            elif monHealth <= dead:
                print("You have vanquished the monster")
                print()
                shop = ""
                monHealth = dead



        if choice == "No" or choice == "no":
            print()
            shop = "Exit"
            print("You have been eaten")
            print("Game Over")
            monHealth = dead
            fight = "Close"

        while shop != "Exit":
            if fight == "Exit":
                break

            print("You have " + str(coins) + " coins")
            shop = input("Do you want to shop? ")
            if shop == "Yes" or shop == "yes":
                if shop != "Close":
                    print("What do you want to upgrade?")
                    time.sleep(1)
                    print("Health for 20 coins")
                    print("Attack for 15 coins")
                    time.sleep(1)
                    print()
                    print("Type 'Exit' to exit shop")
                    upgrade = input("")
                    if upgrade == "Health":
                        if coins >= 20:
                            health = player.updateHealth()
                            coins = player.coinsHealth()
                            print("You have upgraded your Health! You are at " + str(health) + " Health!")
                        elif coins < 20:
                            print("You do not have enough coins!")
                    if upgrade == "Attack":
                        if coins >= 15:
                            attack = player.updateAttack()
                            coins = player.coinsAttack()
                            print("You have upgraded your Attack! You are at " + str(attack) + " Attack!")
                        elif coins < 15:
                            print("You do not have enough coins!")
                    if upgrade == "Exit" or upgrade == "exit":
                        shop = "Exit"
            elif shop == "No" or shop == "no":
                shop = "Exit"


        importlib.reload(monster)
