# Nicholas Land 2 hour project
# 10/5/2018
# Plight of friction


# Characters are composed in list with indexs referring to the specific stats, name, stuff like that
# Basically a dungeon crawler
# will have function to combat
#
# function that checks xp amount to level up

# EX: mainChar = [name, element, class, level, attack, defense, health, mana, luck]
# Warrior starts out with good attack/def alright health low mana and next to low luck


# /////WORK LOG\\\\\:
# 10/24/2018: Added the while loop feature menu thing
#

# /////SHIT TO WORK ON\\\\\:
# add different abilities for the classes and factions
# add the saving feature at the end of the fights
# add the inventory feature
# add shop feature with gold currency


import random
import json


def welcome(mainCharList):
    mainCharList.append(str(input("Hello adventurer, welcome to Plight of Friction! What is your name? ")))
    print("Awesome, nice to meet you ", mainCharList[0])

    print("\n\nIn this game there are 3 main factions that rule Plight of Friction.")
    print("The 3 factions are: ")
    print("First there is the fire clan, who use the destructive power of fire as their core.")
    print("Next there is the water clan who uses the healing and power aspects of water.")
    print("Finally there is the forest clan who uses the power of earth, plants, and nature.")
    elementDecision = str(input("What clan would you like to associate yourself with? (fire, water, or forest) "))
    elementDecision.lower()

    elementTrigger = 0
    while (elementTrigger == 0):
        if (elementDecision == "fire"):
            print("Congrats you chose the fire clan!")
            mainCharList.append(elementDecision)
            elementTrigger += 1
        elif (elementDecision == "water"):
            print("Congrats you chose the water clan!")
            mainCharList.append(elementDecision)
            elementTrigger += 1
        elif (elementDecision == "forest"):
            print("Congrats you chose the forest clan!")
            mainCharList.append(elementDecision)
            elementTrigger += 1
        else:
            elementDecision = str(input("Please enter a valid clan or possibly check your spelling "))

    print("\n\nIn this game there are 3 classes to choose from with each having their own niche in the game.")
    print("The classes are: ")
    print("Warrior: A class who relies raw strength and power to mercilessly defeat his enemies")
    print("Assassin: A class that uses deception and agility to outsmart his or her foes into defeat")
    print("Sorcerer: A class that taps into the arcane and mystic energy to conjure spells to eliminate enemies")
    classDecision = str(input("What class would you like to become? "))
    classDecision.lower()

    classTrigger = 0
    while (classTrigger == 0):
        if (classDecision == "warrior"):
            print("Congrats you chose the Warrior class!")
            mainCharList.append(classDecision)
            classTrigger += 1
            mainCharList.append(1)  # level
            mainCharList.append(20)  # attack
            mainCharList.append(.15)  # defense
            mainCharList.append(200)  # health
            mainCharList.append(100)  # mana
            mainCharList.append(5)  # luck
            mainCharList.append(0)  # xp

        elif (classDecision == "assassin"):
            print("Congrats you chose the Assassin class!")
            mainCharList.append(classDecision)
            classTrigger += 1
            mainCharList.append(1)  # level
            mainCharList.append(14)  # attack
            mainCharList.append(.10)  # defense
            mainCharList.append(120)  # health
            mainCharList.append(150)  # mana
            mainCharList.append(40)  # luck
            mainCharList.append(0)  # xp

        elif (classDecision == "sorcerer"):
            print("Congrats you chose the Sorcerer class!")
            mainCharList.append(classDecision)
            classTrigger += 1
            mainCharList.append(1)  # level
            mainCharList.append(16)  # attack
            mainCharList.append(.10)  # defense
            mainCharList.append(150)  # health
            mainCharList.append(220)  # mana
            mainCharList.append(15)  # luck
            mainCharList.append(0)  # xp

        else:
            classDecision = str(input("Please enter a valid class, or possibly check your previous spelling"))

        print(
            "\n\nYour character starts out at level 1, and as you kill more monsters you gain xp and you level up")
        print("right now you are level ", mainCharList[3])

        mainCharDict = {}

        mainCharDict['name'] = mainCharList[0]
        mainCharDict['clan'] = mainCharList[1]
        mainCharDict['class'] = mainCharList[2]
        mainCharDict['level'] = mainCharList[3]
        mainCharDict['attack'] = mainCharList[4]
        mainCharDict['defense'] = mainCharList[5]
        mainCharDict['health'] = mainCharList[6]
        mainCharDict['mana'] = mainCharList[7]
        mainCharDict['luck'] = mainCharList[8]
        mainCharDict['xp'] = mainCharList[9]

        with open('charStats.json', 'a') as outfile:
            json.dump(mainCharDict, outfile)



        return mainCharList



def shallowCaveFight(mainCharList):
    print("This is a shallow cave fight")
    print(mainCharList)

    randEnemyElementPool = []
    randEnemyClassPool = ["warrior", "assassin", "sorcerer"]

    enemyList = []

    if (mainCharList[1] == "water"):
        randEnemyElementPool.append("fire")
        randEnemyElementPool.append("forest")



    elif (mainCharList[1] == "fire"):

        randEnemyElementPool.append("forest")

        randEnemyElementPool.append("water")


    else:

        randEnemyElementPool.append("water")

        randEnemyElementPool.append("fire")

    classDecider = random.randint(0, 2)

    elementDecider = random.randint(0, 1)

    enemyList.append("Small Enemy")

    enemyList.append(randEnemyElementPool[elementDecider])

    enemyList.append(randEnemyClassPool[classDecider])

    if (enemyList[2] == "warrior"):
        enemyList.append(1)  # level

        enemyList.append(10)  # attack

        enemyList.append(.5)  # defense

        enemyList.append(80)  # health

        enemyList.append(100)  # mana

        enemyList.append(5)  # luck

    if (enemyList[2] == "assassin"):
        enemyList.append(1)  # level

        enemyList.append(7)  # attack

        enemyList.append(.3)  # defense

        enemyList.append(60)  # health

        enemyList.append(100)  # mana

        enemyList.append(15)  # luck

    if (enemyList[2] == "sorcerer"):
        enemyList.append(1)  # level

        enemyList.append(8)  # attack

        enemyList.append(.5)  # defense

        enemyList.append(70)  # health

        enemyList.append(100)  # mana

        enemyList.append(5)  # luck

    statDisplay(enemyList)

    statDisplay(mainCharList)

    combatSim(mainCharList,enemyList)

    print(mainCharList)
def averageCaveFight(mainCharList):
    print("This is an average cave fight")
    print(mainCharList)
def deepCaveFight(mainCharList):
    print("This is a deep cave fight")
    print(mainCharList)
def statDisplay(charList):
    print("Stats for: ",charList[0])
    print(charList[0] + "'s clan element is ", charList[1])
    print(charList[0] + "'s class is: ", charList[2])
    print(charList[0] + "'s level is: ", charList[3])
    print(charList[0] + "'s attack is: ", charList[4])
    print(charList[0] + "'s defense is: ", charList[5])
    print(charList[0] + "'s health is: ", charList[6])
    print(charList[0] + "'s mana is: ", charList[7])
    print(charList[0] + "'s critical strike chance is: ", charList[8], "%")
def caveSelection(mainCharList):
    print("\n\nAlright you are now off on your adventure!\n\n")
    response = str(input("There are three caves in front of you, Would you like to go into the shallow one, average one, or deep one? "))
    response.lower()

    trigger = 0
    while (trigger == 0):

        if (response == "shallow"):
            shallowCaveFight(mainCharList)
            trigger += 1

        elif (response == "average"):
            averageCaveFight(mainCharList)
            trigger += 1

        elif (response == "deep"):
            deepCaveFight(mainCharList)
            trigger += 1

        else:
            response = str(input("Please input 'shallow', 'average', or 'deep' "))
def attackWithCrit(charList):
    crit = random.randint(0,100)

    if(charList[8] >= crit):
        print("CRITICAL STRIKE!")
        return charList[4]*2
    else:
        return charList[4]
def combatSim(main, enemy):
    print("You are now fighting", enemy[0])

    print("You start out the fight with", main[6], "health")

    # 1 to use a normal attack
    # 2 to use a special ability
    # 3 to drink health potion
    # 4 to drink mana potion

    trigger = 0


    while(trigger == 0):

        print("\nEnter 1 to do a basic attack")
        print("Enter 2 to do a special ability")
        print("Enter 3 to use a health potion")
        print("Enter 4 to use a mana potion")
        print("Enter 5 to run like a loser")

        userChoice = int(input("Your choice is: "))



        if(userChoice==1):
            print(main[0], "uses a normal attack!")
            mainAttack = attackWithCrit(main)
            enemy[6] = enemy[6] - mainAttack
            print(main[0], "has attacked the enemy for", mainAttack, "damage!")
            print("The enemy has", enemy[6], "health left! \n\n\n")

            print(enemy[0] + " uses basic attack!")
            enemyAttack = attackWithCrit(enemy)
            main[6] = main[6] - enemyAttack
            print(enemy[0], "has attacked the enemy for", enemyAttack, "damage!")
            print(main[0]+ "has", main[6], "health left! \n\n\n")



        if(enemy[6] <= 0):
            print(enemy[0] + " has been defeated!")
            print(main)


        if(main[6] <= 0):
            print(main[0] + " has been defeated!")
            print(main)


    if(main[6] <= 0 ):
        print("Well", main[0], "it looks like you've been defeated.")
        print("Luckily the gods of PLIGHT OF FRICTION have decided to resurrect you from the dead")
        print("You now start of back alive with 60hp, please be more prepared as you go into dungeons")
        main[6] = 60


    with open('charStats.json', 'r+') as file:
        data = json.load(file)
        data['name'] = main[0]
        data['clan'] = main[1]
        data['class'] = main[2]
        data['level'] = main[3]
        data['attack'] = main[4]
        data['defense'] = main[5]
        data['health'] = main[6]
        data['mana'] = main[7]
        data['luck'] = main[8]
        data['xp'] = main[9]








def main():
    userControl = -1


    while( userControl != "0" ):
        print("\n\n")
        print("WELCOME TO PLIGHT OF FRICTION\n\n\n")
        print("Enter 1 if you would like to create a new character for the game")
        print("Enter 2 if you would like to load a character into the game")
        print("Enter 3 if you would like to go into dungeon mode")



        userControl = input("Please type in your selection: ")


        mainChar = []



        if(userControl == "1"):
            mainChar = welcome(mainChar)



        if(userControl == "2"):
            mainChar = loadCharacter()
            #need to work on
            statDisplay(mainChar)



        if(userControl == "3"):
            caveSelection(mainChar)




main()

































