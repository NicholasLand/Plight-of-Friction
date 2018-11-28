
# Nicholas Land 2 hour project
# 10/5/2018
# Plight of friction


# EX: mainChar = [name, element, class, level, attack, defense, health, mana, luck]
# Warrior starts out with good attack/def alright health low mana and next to low luck


# /////WORK LOG\\\\\:
# 10/24/2018: Added the while loop feature menu thing
# 11/7/2018: Added basic combat features
# 11/12/2018

# /////SHIT TO WORK ON\\\\\:
# add different abilities for the classes and factions
# figure out what the hell is going on with the combat sim, when i tried refactoring it
# --it went on it's dumb shit again with the going past 0 health, but the old version works
# add shop feature with gold currency


import random
import json



# GAME MECHANICS
def welcome(mainCharList):

    # the reason why theres a list as the parameter is because nick is a lazy POS and he didnt
    # want to convert the character creation from a list format into a dictionary format
    # so instead i just built a dictionary convert the list return from def welcome


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
            mainCharList.append(0)  # gold

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
            mainCharList.append(0)  #gold

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
            mainCharList.append(0)  # gold

        else:
            classDecision = str(input("Please enter a valid class, or possibly check your previous spelling"))

        print(
            "\n\nYour character starts out at level 1, and as you kill more monsters you gain xp and you level up")
        print("right now you are level ", mainCharList[3])




        return mainCharList
def save(aCharDict):

    if(len(aCharDict['stats']) > 0):
        with open('charStats.json', 'w') as outfile:
            json.dump(aCharDict, outfile)
            outfile.close()
        print("Character has been saved!")
    else:
        print("It seems you don't have a character file on selection, please load one or create one.")
def load(aCharDict):
    with open('charStats.json', 'r') as readfile:
        try:
            data = json.load(readfile)
            aCharDict.update(data)
            print("Character has been loaded!")
        except:
            print("There are currently no characters saved.")
def levelUp(mainCharDict):
    xp = mainCharDict['stats']['xp']
    level = mainCharDict['stats']['level']
    attack = mainCharDict['stats']['attack']
    defense = mainCharDict['stats']['defense']
    health = mainCharDict['stats']['health']
    mana = mainCharDict['stats']['mana']
    gold = mainCharDict['inventory']['gold']

    print("You now have", mainCharDict['stats']['xp'], "experience")

    # level 2
    if (30 <= xp < 70 and mainCharDict['stats']['level'] < 2):

        print("Congrats you are now level 2!")

        if (mainCharDict['stats']['class'] == "warrior"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 50

            mainCharDict['abilities']['smash'] = {}
            mainCharDict['abilities']['smash']['name'] = "Smash"
            mainCharDict['abilities']['smash']['mana'] = 60
            description = "You smash your weapon at the enemy's feet creating a shock that stuns them for a turn"
            mainCharDict['abilities']['smash']['description'] = description


        if (mainCharDict['stats']['class'] == "assassin"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 50

            mainCharDict['abilities']['shadowStep'] = {}
            mainCharDict['abilities']['shadowStep']['name'] = "Shadow Step"
            mainCharDict['abilities']['shadowStep']['mana'] = 60
            description = "You flash behind your opponent slapping the side of their head and stunning them for a turn "
            mainCharDict['abilities']['shadowStep']['description'] = description

        if (mainCharDict['stats']['class'] == "sorcerer"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 50

            mainCharDict['abilities']['magicBind'] = {}
            mainCharDict['abilities']['magicBind']['name'] = "Magic Bind"
            mainCharDict['abilities']['magicBind']['mana'] = 70
            description = "You cast a binding spell on the enemy stunning them for a turn"
            mainCharDict['abilities']['magicBind']['description'] = description



    # level 3
    if (70 <= xp < 100 and mainCharDict['stats']['level'] < 3):

        print("Congrats you are now level 3!")

        if (mainCharDict['stats']['class'] == "warrior"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 60

        if (mainCharDict['stats']['class'] == "assassin"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 60

        if (mainCharDict['stats']['class'] == "sorcerer"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 60

    # level 4
    if (140 <= xp < 190 and mainCharDict['stats']['level'] < 4):

        print("Congrats you are now level 4!")

        if (mainCharDict['stats']['class'] == "warrior"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 70

        if (mainCharDict['stats']['class'] == "assassin"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 70

        if (mainCharDict['stats']['class'] == "sorcerer"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 70

    # level 5
    if (190 <= xp < 250 and mainCharDict['stats']['level'] < 5):

        print("Congrats you are now level 5!")

        if (mainCharDict['stats']['class'] == "warrior"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 80

        if (mainCharDict['stats']['class'] == "assassin"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 80

        if (mainCharDict['stats']['class'] == "sorcerer"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 80

    # level 6
    if (250 <= xp < 320 and mainCharDict['stats']['level'] < 6):

        print("Congrats you are now level 6!")

        if (mainCharDict['stats']['class'] == "warrior"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 90

        if (mainCharDict['stats']['class'] == "assassin"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 90

        if (mainCharDict['stats']['class'] == "sorcerer"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 90

    # level 7
    if (320 <= xp < 390 and mainCharDict['stats']['level'] < 7):

        print("Congrats you are now level 7!")

        if (mainCharDict['stats']['class'] == "warrior"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 100

        if (mainCharDict['stats']['class'] == "assassin"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 100

        if (mainCharDict['stats']['class'] == "sorcerer"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 100

    # level 8
    if (390 <= xp <= 470 and mainCharDict['stats']['level'] < 8):

        print("Congrats you are now level 8!")

        if (mainCharDict['stats']['class'] == "warrior"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 100

        if (mainCharDict['stats']['class'] == "assassin"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 100

        if (mainCharDict['stats']['class'] == "sorcerer"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 100

    # level 9
    if (470 <= xp < 600 and mainCharDict['stats']['level'] < 9):

        print("Congrats you are now level 9!")

        if (mainCharDict['stats']['class'] == "warrior"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 100

        if (mainCharDict['stats']['class'] == "assassin"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 100

        if (mainCharDict['stats']['class'] == "sorcerer"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 100

    # level 10
    if (xp > 600 and mainCharDict['stats']['level'] < 10):

        print("Congrats you are now level 10!")
        print("You are at the level cap of the game!")

        if (mainCharDict['stats']['class'] == "warrior"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 150

        if (mainCharDict['stats']['class'] == "assassin"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 150

        if (mainCharDict['stats']['class'] == "sorcerer"):
            level += 1
            attack *= 1.3
            defense *= 1.3
            health *= 1.3
            mana *= 1.3
            gold += 150
def convertFromListToDict(mainCharList, mainCharDict):


    mainCharDict['stats']['name'] = mainCharList[0]
    mainCharDict['stats']['clan'] = mainCharList[1]
    mainCharDict['stats']['class'] = mainCharList[2]
    mainCharDict['stats']['level'] = mainCharList[3]
    mainCharDict['stats']['attack'] = mainCharList[4]
    mainCharDict['stats']['defense'] = mainCharList[5]
    mainCharDict['stats']['health'] = mainCharList[6]
    mainCharDict['stats']['mana'] = mainCharList[7]
    mainCharDict['stats']['luck'] = mainCharList[8]
    mainCharDict['stats']['xp'] = mainCharList[9]
    mainCharDict['inventory']['gold'] = mainCharList[10]

    print(mainCharDict)

    if (mainCharDict['stats']['class'] == "warrior"):
        mainCharDict['abilities']['crush'] = {}
        crush = mainCharDict['abilities']['crush']
        crush['name'] = "crush"
        crush['mana'] = 50
        description = "Your character jumps up and slams its weapon down on the enemy and deals 1.5x attack damage"
        crush['description'] = description

    if (mainCharDict['stats']['class'] == "sorcerer"):
        mainCharDict['abilities']['energyBlast'] = {}
        energyBlast = mainCharDict['abilities']['energyBlast']
        energyBlast['name'] = "energy blast"
        energyBlast['mana'] = 50
        description = "Your character conjures a energy into a ball and sends it at the enemy dealing 1.5x atk dmg"
        energyBlast['description'] = description

    if (mainCharDict['stats']['class'] == "assassin"):
        mainCharDict['abilities']['gouge'] = {}
        gouge = mainCharDict['abilities']['gouge']
        gouge['name'] = "gouge"
        gouge['mana'] = 50
        description = "Your character runs up to the enemy and shoves its weapon into the back of the enemy"
        gouge['description'] = description
def convertFromListToDictEnemy(enemyCharList, enemyCharDict):
    enemyCharDict['stats']['name'] = enemyCharList[0]
    enemyCharDict['stats']['clan'] = enemyCharList[1]
    enemyCharDict['stats']['class'] = enemyCharList[2]
    enemyCharDict['stats']['level'] = enemyCharList[3]
    enemyCharDict['stats']['attack'] = enemyCharList[4]
    enemyCharDict['stats']['defense'] = enemyCharList[5]
    enemyCharDict['stats']['health'] = enemyCharList[6]
    enemyCharDict['stats']['mana'] = enemyCharList[7]
    enemyCharDict['stats']['luck'] = enemyCharList[8]
    enemyCharDict['stats']['xp'] = 10
def statDisplay(mainCharDict):
    print("\n\nStats for: ",mainCharDict['stats']['name'])
    print(mainCharDict['stats']['name'] + "'s clan element is ", mainCharDict['stats']['clan'])
    print(mainCharDict['stats']['name'] + "'s class is: ", mainCharDict['stats']['class'])
    print(mainCharDict['stats']['name'] + "'s level is: ", mainCharDict['stats']['level'])
    print(mainCharDict['stats']['name'] + "'s attack is: ", mainCharDict['stats']['attack'])
    print(mainCharDict['stats']['name'] + "'s defense is: ", mainCharDict['stats']['defense'])
    print(mainCharDict['stats']['name'] + "'s health is: ", mainCharDict['stats']['health'])
    print(mainCharDict['stats']['name'] + "'s mana is: ", mainCharDict['stats']['mana'])
    print(mainCharDict['stats']['name'] + "'s critical strike chance is:", mainCharDict['stats']['luck'], "%\n\n")
def warningForCharCreation():
    print("\n\n\n***WARNING*** if you have a previously saved file on this game then creating a new character will delete it")
    print("Enter 0 if you wish to go back to the main menu")
    print("Or")
    print("Enter literally any other number to continue forward with character creation")

    charCreation = input()

    if(charCreation == "0"):
        return False

    else:
        return True

# COMBAT MECHANICS
def combatSim(mainCharDict, enemyDict):
    mainCharName = mainCharDict['stats']['name']
    mainCharHealth = mainCharDict['stats']['health']

    enemyName = enemyDict['stats']['name']
    enemyHealth = enemyDict['stats']['health']


    print("You are now fighting", enemyName,"starting out with", enemyHealth,"health")

    print("You start out the fight with", mainCharHealth, "health")

    # 1 to use a normal attack
    # 2 to use a special ability
    # 3 to drink health potion
    # 4 to drink mana potion

    trigger = 0

    while (trigger == False):

        print("\nEnter 1 to do a basic attack")
        print("Enter 2 to do a special ability")
        print("Enter 3 to use a health potion")
        print("Enter 4 to use a mana potion")
        print("Enter 5 to run like a loser")

        userChoice = int(input("Your choice is: "))

        if (userChoice == 1):
            print(mainCharName, "uses a normal attack!")
            mainAttack = attackWithCrit(mainCharDict)
            enemyDict['stats']['health'] = enemyDict['stats']['health'] - mainAttack
            print(mainCharName, "has attacked the enemy for", mainAttack, "damage!")
            print("The enemy has", enemyDict['stats']['health'], "health left! \n\n\n")

            print(enemyDict['stats']['name'] + " uses basic attack!")
            enemyAttack = attackWithCrit(enemyDict)
            mainCharHealth = mainCharHealth - enemyAttack
            print(enemyName, "has attacked", mainCharName, "for", enemyAttack, "damage!")
            print(mainCharName + "has", mainCharHealth, "health left! \n\n\n")

        if (enemyDict['stats']['health'] <= 0):
            print(enemyName + " has been defeated!")
            mainCharDict['stats']['xp']+=enemyDict['stats']['xp']
            trigger = True

        if (mainCharHealth <= 0):
            print(mainCharName + " has been defeated!")
            trigger = True


    if (mainCharDict['stats']['health'] <= 0):
        print("Well", mainCharHealth, "it looks like you've been defeated.")
        print("Luckily the gods of PLIGHT OF FRICTION have decided to resurrect you from the dead")
        print("You now start of back alive with 60hp, please be more prepared as you go into dungeons")
        mainCharDict['stats']['health'] = 60

    levelUp(mainCharDict)
    save(mainCharDict)
def attackWithCrit(mainCharDict):

    # only use the mainCharDict as the parameter because the function takes care of the rest
    crit = random.randint(0,100)

    if(mainCharDict['stats']['luck'] >= crit):
        print("CRITICAL STRIKE!")
        return mainCharDict['stats']['attack']*2
    else:
        return mainCharDict['stats']['attack']

# LEVEL MECHANICS
def caveSelection(mainCharDict):
    print("\n\nAlright you are now off on your adventure!\n\n")
    response = str(input("There are three caves in front of you, Would you like to go into the shallow one, average one, or deep one? "))
    response.lower()

    trigger = 0
    while (trigger == 0):

        if (response == "shallow"):
            shallowCaveFight(mainCharDict)
            trigger += 1

        elif (response == "average"):
            averageCaveFight(mainCharDict)
            trigger += 1

        elif (response == "deep"):
            deepCaveFight(mainCharDict)
            trigger += 1

        else:
            response = str(input("Please input 'shallow', 'average', or 'deep' "))
def shallowCaveFight(mainCharDict):
    print("\nThis is a shallow cave fight")

    randEnemyElementPool = []
    randEnemyClassPool = ["warrior", "assassin", "sorcerer"]

    enemyList = []

    if (mainCharDict['stats']['clan'] == "water"):
        randEnemyElementPool.append("fire")
        randEnemyElementPool.append("forest")

    elif (mainCharDict['stats']['clan'] == "fire"):
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

    enemyCharDict = {'stats': {},'inventory': {}, "moves": {}}

    convertFromListToDictEnemy(enemyList,enemyCharDict)

    combatSim(mainCharDict,enemyCharDict)
def averageCaveFight(mainCharDict):
    print("This is an average cave fight")
    print(mainCharDict)
def deepCaveFight(mainCharDict):
    print("This is a deep cave fight")
    print(mainCharDict)





def main():
    endGame = True


    while( endGame != False):
        print("\n")
        print("WELCOME TO PLIGHT OF FRICTION\n\n")
        print("Enter 0 if you would like to save the game and quit")
        print("Enter 1 if you would like to create a new character for the game")
        print("Enter 2 if you would like to load a character into the game")
        print("Enter 3 if you would like to go into dungeon mode")
        print("Enter 4 if you would like to visit the shop")
        print("Enter 5 if you want to view your stats")



        userControl = input("Please type in your selection: ")


        # save and quit
        if(userControl == "0"):
            save(mainChar)
            print("Thanks for playing! See you soon!")
            endGame = False



        # create a new character
        if(userControl == "1"):
            if(warningForCharCreation()):
                mainCharList = []
                mainCharList = welcome(mainCharList)
                convertFromListToDict(mainCharList,mainChar)
                statDisplay(mainChar)


        # load character
        if(userControl == "2"):
            load(mainChar)
            statDisplay(mainChar)


        # cave selection to go into combat
        if(userControl == "3"):
            caveSelection(mainChar)


        # go to shop
        if(userControl == "4"):
            return 0
            # need to create shop


        # look at stats on character
        if(userControl == "5"):
            statDisplay(mainChar)




mainChar = {'stats': {}, 'inventory': {}, 'abilities': {}}

main()
































