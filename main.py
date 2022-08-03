import importlib
import player

fight = "Yes"
dead = 0
shop = "No"

health = player.playerHealth()
attack = player.playerAttack()
name = player.playerName()
print()

print("Name: " + name)
print("Health: " + health)
print("Attack: " + attack)

while fight != "No":

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
                   fight = "No"
                   health = dead

               print("Your health is at " + str(health))
               print()

            elif monHealth <= dead:
                print("You have vanquished the monster")
                shop = ""
                monHealth = dead



        if choice == "No" or choice == "no":
            print()
            print("You have been eaten")
            print("Game Over")
            health = dead
            monHealth = health
            fight = "No"

        while shop != "No":
            if fight == "No":
                break

            print("You have " + str(coins) + " coins")
            shop = input("Do you want to shop? ")

            if shop != "No":
                upgrade = input("What do you want to upgrade? ")
                if upgrade == "Health":
                    if coins >= 20:
                        health = player.updateHealth()
                        coins = player.coinsHealth()
                    elif coins < 20:
                        print("You do not have enough coins!")


        importlib.reload(monster)
