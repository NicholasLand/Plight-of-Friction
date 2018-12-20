
# Nicholas Land / land.nicholas@outlook.com
# 10/5/2018
# Plight of friction

#TODO add more spells in ability selection and add them into level up function

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
    enemyCharDict['stats']['xp'] = enemyCharList[9]
    enemyCharDict['stats']['gold'] = enemyCharDict['stats']['xp'] * 2
def statDisplay(mainCharDict):
    if(len(mainCharDict['stats']) < 5):
        print("You have no character on file, please load your character or create a new one")
        return 0

    trigger = False
    while( trigger == False):
        print("\nEnter 1 to look at character stats")
        print("Enter 2 to look at inventory")
        print("Enter 3 to look at your abilities")
        statChoice = int(input("Enter your choice:"))

        while( not( 1<=statChoice<=3)):
            print("Input not understood.")
            statChoice = int(input("Please enter a valid number"))

        if( statChoice == 1):
            print("\n\nStats for: ",mainCharDict['stats']['name'])
            print("clan:\t\t\t\t", mainCharDict['stats']['clan'])
            print("class:\t\t\t\t", mainCharDict['stats']['class'])
            print("level:\t\t\t\t", mainCharDict['stats']['level'])
            print("attack:\t\t\t\t", mainCharDict['stats']['attack'])
            print("defense:\t\t\t", mainCharDict['stats']['defense'])
            print("health:\t\t\t\t", mainCharDict['stats']['health'])
            print("mana:\t\t\t\t", mainCharDict['stats']['mana'])
            print("critical strike:\t", mainCharDict['stats']['luck'], "%\n\n")

        if( statChoice == 2):
            print("\nYour inventory:")
            for i in mainCharDict['inventory']:
                print(i, mainCharDict['inventory'][i])
                print()

        if( statChoice == 3):
            print("Your abilities:")
            for i in mainCharDict['abilities']:
                print(mainCharDict['abilities'][i]['name'])
                print("mana cost:", mainCharDict['abilities'][i]['mana'])
                print("description:",mainCharDict['abilities'][i]['description'])
                print()



        exit = input("Do you want to look at anymore details about your character?(Enter yes or no):")

        if(exit == "no"):
            trigger = True
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
def getHealth(mainCharDict):
    charClass = mainCharDict['stats']['class']
    charLevel = mainCharDict['stats']['level']
    health = 0

    if(charClass == "warrior"):
        health == 200

    elif(charClass == "assassin"):
        health = 120

    else:
        health = 150

    if(charLevel == 1):
        return int(health)

    else:
        for i in range(charLevel-1):
            health*= 1.3
        return int(health)
def getMana(mainCharDict):
    charClass = mainCharDict['stats']['class']
    charLevel = mainCharDict['stats']['level']
    mana = 0

    if(charClass == "warrior"):
        mana == 100

    elif(charClass == "assassin"):
        mana = 150

    else:
        mana = 220

    if(charLevel == 1):
        return int(mana)

    else:
        for i in range(charLevel-1):
            mana*= 1.3
        return int(mana)


# COMBAT MECHANICS
def combatSim(mainCharDict, enemyDict):
    mainCharName = mainCharDict['stats']['name']
    mainCharHealth = mainCharDict['stats']['health']
    mainCharMana = mainCharDict['stats']['mana']
    healthPot = mainCharDict['inventory'].get('health potion', -1)
    manaPot = mainCharDict['inventory'].get('mana potion', -1)

    enemyName = enemyDict['stats']['name']
    enemyHealth = enemyDict['stats']['health']
    enemyMana = enemyDict['stats']['mana']





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
        print("Enter 3 to look at stats and inventory")
        print("Enter 4 to use a health potion")
        print("Enter 5 to use a mana potion")
        print("Enter 6 to run like a loser")
        print("Your mana is: ", mainCharMana,"\n\n")

        userChoice = int(input("Your choice is: "))

        if ( userChoice == 1 ):
            print(mainCharName, "uses a normal attack!")
            attack = attackWithCrit(mainCharDict)
            mainAttack = attackWithDef(attack, enemyDict)
            enemyHealth = enemyHealth - mainAttack
            print(mainCharName, "has attacked the enemy for", mainAttack, "damage!")
            print("The enemy has", enemyHealth, "health left! \n\n")

            print(enemyName + " uses basic attack!")
            enemyAttack = attackWithCrit(enemyDict)
            enemyMainAttack = attackWithDef(enemyAttack, mainCharDict)
            mainCharHealth = mainCharHealth - enemyMainAttack
            print(enemyName, "has attacked", mainCharName, "for", enemyMainAttack, "damage!")
            print(mainCharName + " has", mainCharHealth, "health left! \n\n")


        if ( userChoice == 2 ):
            moveResult = abilitySelection(mainCharDict)

            moveName = moveResult[0]
            moveDamage = moveResult[1]
            moveMana = moveResult[2]
            moveCondition = moveResult[3]
            changeInEnemyAtk = moveResult[4]
            changeInEnemyDef = moveResult[5]
            changeInMainAtk = moveResult[6]
            changeInMainDef = moveResult[7]

            if( mainCharMana > moveMana ):
                mainCharMana = mainCharMana - moveMana
                mainAttack = attackWithDef(moveDamage,enemyDict)
                enemyHealth = enemyHealth - mainAttack
                print(mainCharName, "has used", moveName, "for", mainAttack, "!")

                if(moveCondition == "stun"):
                    print(enemyName, "is now stunned! It cannot attack!")
                    print("... \nIt finally woke up!")

                else:
                    attack = attackWithCrit(enemyDict)
                    enemyAttack = attackWithDef(attack, mainCharDict)
                    print(enemyName, "uses normal attack for", enemyAttack, "!")
                    mainCharHealth = mainCharHealth - enemyAttack
                    print(mainCharName + " has", mainCharHealth, "health left! \n\n")

                print("The enemy now has", enemyHealth, "health!\n\n")

            else:
                print("You don't have enough mana! If you have mana potions drink them!")


        if( userChoice == 3 ):
                statDisplay(mainCharDict)


        if( userChoice == 4 ):
            maxHealth = getHealth(mainCharDict)

            if( healthPot <= 0 ):
                print("You don't have any health potions in your inventory!")

            elif( healthPot > 0 ):
                if (maxHealth == mainCharHealth):
                    print("You're already at full health!")

                else:
                    mainCharDict['inventory']['health potion'] = mainCharDict['inventory']['health potion'] - 1
                    mainCharHealth += 50
                    amountHealed = 50

                    if( mainCharHealth > maxHealth ):
                        amountHealed = ((mainCharHealth - maxHealth) - 50) * -1
                        mainCharHealth = maxHealth


                    print("You've been healed for", amountHealed, "health, your health is now", mainCharHealth)



        if( userChoice == 5 ):
                maxMana = getMana(mainCharDict)

                if (manaPot <= 0):
                    print("You don't have any mana potions in your inventory!")

                elif (manaPot > 0):
                    if (maxMana == mainCharMana):
                        print("You're already at full mana!")

                    else:
                        mainCharDict['inventory']['mana potion'] = mainCharDict['inventory']['mana potion'] - 1
                        mainCharMana += 50
                        amountHealed = 50

                        if (mainCharMana > maxMana):
                            amountHealed = ((mainCharMana - maxMana) - 50) * -1
                            mainCharMana = maxMana

                        print(amountHealed, "mana was restored! You now have", mainCharMana, "mana")


        if( userChoice == 6 ):
                print("You run away from the enemy and cower in fear")
                trigger == True


        if (enemyHealth <= 0):
            print(enemyName + " has been defeated!")
            mainCharDict['stats']['xp'] += enemyDict['stats']['xp']
            mainCharDict['stats']['health'] = mainCharHealth
            trigger = True

        if (mainCharHealth <= 0):
            print(mainCharName + " has been defeated!")
            mainCharDict['stats']['health'] = mainCharHealth
            trigger = True


    if (mainCharDict['stats']['health'] <= 0):
        print("Well", mainCharHealth, "it looks like you've been defeated.")
        print("Luckily the gods of PLIGHT OF FRICTION have decided to resurrect you from the dead")
        print("You now start of back alive with 60hp, please be more prepared as you go into dungeons")
        mainCharDict['stats']['health'] = 60

    mainCharDict['stats']['health'] = mainCharHealth
    mainCharDict['stats']['mana'] = mainCharMana

    levelUp(mainCharDict)
    save(mainCharDict)
def attackWithCrit(aCharDict):

    # only use the mainCharDict as the parameter because the function takes care of the rest
    crit = random.randint(0,100)

    if(aCharDict['stats']['luck'] >= crit):
        print("CRITICAL STRIKE!")
        return aCharDict['stats']['attack']*2
    else:
        return aCharDict['stats']['attack']
def attackWithDef(attack, aCharDict):
    difference = attack * aCharDict['stats']['defense']
    return int(attack - difference)
def abilitySelection(aCharDict):
    spells = aCharDict['abilities']

    abilities = []
    num = 1

    print("\nYour Spells:")
    for i in spells:
        print("\nEnter", num, "for:", i.upper())
        print("Info:")
        print(spells[i]['mana'], "mana cost")
        print("Description:", spells[i]['description'])
        abilities.append(i)
        num+=1

    abilityChoice = int(input("Please enter your choice: "))

    while(not(1<=abilityChoice<=len(abilities))):
        print("Your choice is not in your ability range")
        abilityChoice = int(input("Please enter your choice: "))

    abilitySelection = abilities[abilityChoice-1]

    print("You chose:", abilitySelection)

    return abilityList(abilitySelection,aCharDict)
def abilityList(selectedMove, aCharDict):
    aList = []

    attack = aCharDict['stats']['attack']
    defense = aCharDict['stats']['defense']

    selectedMove.lower()

    # Warrior Spells: crush lvl 1, smash lvl 2
    # Assassin Spells: gouge lvl 1, cheap shot lvl 2
    # Sorcerer Spells: energy blast lvl 1, magic bind lvl 2



    if(selectedMove == "crush"):
        aList.append("Crush")
        aList.append(float(attack * 1.5))           # damage
        aList.append(50)                            # mana
        aList.append("none")                        # enemy condition
        aList.append(0)                             # enemy ATK changes
        aList.append(0)                             # enemy DEF changes
        aList.append(0)                             # main ATK changes
        aList.append(0)                             # main DEF changes
        return aList

    elif(selectedMove == "gouge"):
        aList.append("Gouge")
        aList.append(float(attack * 1.5))
        aList.append(50)
        aList.append("none")
        aList.append(0)
        aList.append(0)
        aList.append(0)
        aList.append(0)
        return aList

    elif(selectedMove == "energyBlast"):
        aList.append("Energy Blast")
        aList.append(float(attack * 1.7))
        aList.append(50)
        aList.append("none")
        aList.append(0)
        aList.append(0)
        aList.append(0)
        aList.append(0)
        return aList
                                                    # lvl 2 abilities
    elif(selectedMove == "smash"):
        aList.append("Smash")
        aList.append(float(attack* 1.5))
        aList.append(60)
        aList.append("stun")
        aList.append(0)
        aList.append(0)
        aList.append(0)
        aList.append(0)
        return aList

    elif(selectedMove == "shadowStep"):
        aList.append("Shadow Step")
        aList.append(float(attack * 1.5))
        aList.append(60)
        aList.append("stun")
        aList.append(0)
        aList.append(0)
        aList.append(0)
        aList.append(0)
        return aList

    elif(selectedMove == "magic bind"):
        aList.append("Magic Bind")
        aList.append(float(attack * 1.5))
        aList.append(60)
        aList.append("stun")
        aList.append(0)
        aList.append(0)
        aList.append(0)
        aList.append(0)
        return aList

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
        enemyList.append(10) # xp

    if (enemyList[2] == "assassin"):
        enemyList.append(1)  # level
        enemyList.append(7)  # attack
        enemyList.append(.3)  # defense
        enemyList.append(60)  # health
        enemyList.append(100)  # mana
        enemyList.append(15)  # luck
        enemyList.append(10)  # xp

    if (enemyList[2] == "sorcerer"):
        enemyList.append(1)  # level
        enemyList.append(8)  # attack
        enemyList.append(.5)  # defense
        enemyList.append(70)  # health
        enemyList.append(100)  # mana
        enemyList.append(5)  # luck
        enemyList.append(10) # xp

    enemyCharDict = {'stats': {},'inventory': {}, "moves": {}}

    convertFromListToDictEnemy(enemyList,enemyCharDict)

    combatSim(mainCharDict,enemyCharDict)
def averageCaveFight(mainCharDict):
    print("This is your average cave fight")

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

    enemyList.append("Average Enemy")

    enemyList.append(randEnemyElementPool[elementDecider])

    enemyList.append(randEnemyClassPool[classDecider])

    if (enemyList[2] == "warrior"):
        enemyList.append(5)     # level
        enemyList.append(18)    # attack
        enemyList.append(.5)    # defense
        enemyList.append(170)   # health
        enemyList.append(100)   # mana
        enemyList.append(5)     # luck
        enemyList.append(40)    # xp

    if (enemyList[2] == "assassin"):
        enemyList.append(1)     # level
        enemyList.append(14)    # attack
        enemyList.append(.3)    # defense
        enemyList.append(145)   # health
        enemyList.append(100)   # mana
        enemyList.append(15)    # luck
        enemyList.append(40)    # xp

    if (enemyList[2] == "sorcerer"):
        enemyList.append(1)     # level
        enemyList.append(16)    # attack
        enemyList.append(.5)    # defense
        enemyList.append(160)   # health
        enemyList.append(100)   # mana
        enemyList.append(5)     # luck
        enemyList.append(40)    # xp


    enemyCharDict = {'stats': {},'inventory': {}, "abilities": {}}
    convertFromListToDictEnemy(enemyList,enemyCharDict)
    combatSim(mainCharDict,enemyCharDict)
def deepCaveFight(mainCharDict):
    print("This is a deep cave fight")

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

    enemyList.append("HUGE Enemy")

    enemyList.append(randEnemyElementPool[elementDecider])

    enemyList.append(randEnemyClassPool[classDecider])

    if (enemyList[2] == "warrior"):
        enemyList.append(5)  # level
        enemyList.append(28)  # attack
        enemyList.append(.5)  # defense
        enemyList.append(300)  # health
        enemyList.append(100)  # mana
        enemyList.append(5)  # luck
        enemyList.append(60)  # xp

    if (enemyList[2] == "assassin"):
        enemyList.append(1)  # level
        enemyList.append(23)  # attack
        enemyList.append(.3)  # defense
        enemyList.append(250)  # health
        enemyList.append(100)  # mana
        enemyList.append(25)  # luck
        enemyList.append(60)  # xp

    if (enemyList[2] == "sorcerer"):
        enemyList.append(1)  # level
        enemyList.append(25)  # attack
        enemyList.append(.5)  # defense
        enemyList.append(280)  # health
        enemyList.append(100)  # mana
        enemyList.append(5)  # luck
        enemyList.append(60)  # xp

    enemyCharDict = {'stats': {}, 'inventory': {}, "abilities": {}}
    convertFromListToDictEnemy(enemyList, enemyCharDict)
    combatSim(mainCharDict, enemyCharDict)
def shop(mainCharDict):
    print("**You walk into a dusty old shop, behind the counter sits an old store owner**")
    print("Hello traveller, I am the potion seller, please take a look at my wares\n")

    currentGold = mainCharDict['inventory']['gold']
    inventory = mainCharDict['inventory']
    print("You currently have", currentGold, "gold")

    shopDict = {"items": {"health potion": {"name": "health potion", "cost": 15},
                          "mana potion": {"name": "mana potion", "cost": 10}}}

    num = 1
    shopList = []

    print("Shop inventory:\n")
    for i in shopDict['items']:
        print("Enter", num, "for:")
        print(shopDict['items'][i]['name'])
        print("cost:", shopDict['items'][i]['cost'], "gold\n")
        shopList.append(shopDict['items'][i]['name'])
        num += 1

    itemIndex = int(input("Enter the item # of what you would like to buy: "))

    while (not (1 <= itemIndex <= len(shopList))):
        print("I'm sorry we don't have that item in stock, please enter a valid item #")
        itemIndex = int(input("Enter the item # of what you would like to buy: "))

    selectedItem = shopList[itemIndex - 1]
    selectedItemPrice = shopDict['items'][selectedItem]['cost']

    print("You chose", selectedItem)

    itemQuantity = int(input("How many " + selectedItem + "'s would you like? (Enter number amount)"))

    transactionTotal = itemQuantity * selectedItemPrice

    print("The total for your", itemQuantity, selectedItem + "(s) is", transactionTotal, "gold")

    buyDecision = input("Would you like to finalize this transaction? (Enter yes or no)")

    if (buyDecision == "yes"):

        if (currentGold >= transactionTotal):
            currentGold = currentGold - transactionTotal
            print("\nGood deal! Enjoy your items!")
            print("You have", currentGold, " gold left")
            inventory.update({selectedItem: itemQuantity})
            currentGold = mainCharDict['inventory']['gold']

        if (currentGold < transactionTotal):
            print("\nWell dang traveller, looks like you don't have enough cheddar...")
            print("Come back next time with enough dough and maybe we'll talk then")

    else:
        print("Alright, then get the hell out of my shop and come back when you want to buy something")

    print("Here's your inventory:", inventory)
    save(mainCharDict)
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


        # cave selection to go into combat
        if(userControl == "3"):
            caveSelection(mainChar)


        # go to shop
        if(userControl == "4"):
            shop(mainChar)


        # look at stats on character
        if(userControl == "5"):
            statDisplay(mainChar)




mainChar = {'stats': {}, 'inventory': {}, 'abilities': {}}

main()
































