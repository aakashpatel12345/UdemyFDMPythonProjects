from classes.game import bcolours, Person
from classes.magic import Spell
from classes.inventory import Item
import random

#print("\n\n")
#print( "NAME                      HP                                  MP ")
#print( "                          -------------------------          ----------")
#print( bcolours.BOLD + "  Aakash       160/160   |" + bcolours.OKGREEN + "█████████████████████████" + bcolours.ENDC + bcolours.BOLD + "|  65/65 |" + bcolours.ENDC + bcolours.OKBLUE + "██████████" + bcolours.ENDC + bcolours.BOLD + "|" + bcolours.ENDC)

#print( "NAME                     HP                                  MP ")
#print( "                         -------------------------          ----------")
#print( " Potato       160/160   |█████████████████████████|  65/65 |██████████|")

#print( "NAME                     HP                                  MP ")
#print( "                         -------------------------          ----------")
#print( " Dragon       160/160   |█████████████████████████|  65/65 |██████████|")

#print("\n\n\n")

#create spells
fire = Spell("Fire", 25, 600, "Black")
thunder = Spell("Thunder", 25, 600, "Black")
blizzard = Spell("Blizzard", 25, 500, "Black")
meteor = Spell("Meteor", 40, 1000, "Black")
earthquake = Spell("Earthquake", 30, 840, "Black")

#create healing magic
cure = Spell("Cure", 25, 650, "White")
cura = Spell("Cura", 38, 1800, "White")
curaga = Spell("Curaga", 50, 6000, "White")

#create items
potion = Item ("Potion", "potion", "Heals 50 HP", 50)
hiPotion = Item ("Hi-Potion", "potion", "Heals 100 HP", 100)
superPotion = Item ("Super Potion", "potion", "Heals 1000 HP", 1000)
elixer = Item ("Elixer", "elixer", "Fully restores HP & MP of one party member", 9999) 
hiElixer = Item ("MegaElixer", "elixer", "Fully restores HP & MP of entire party", 9999) 
grenade = Item ("Grenade", "attack", "Deals 500 damage", 500)

'''magic = [{"name": "Fire", "cost": 10, "damage": 100},
{"name": "Thunder", "cost": 12, "damage":180},
{"name": "Blizzard", "cost": 8, "damage": 90}]
'''

#print(player.generateDamage())
#print("This is spell damage for fire",player.generateSpellDamage(0))
#print("This is spell damage for thunder",player.generateSpellDamage(1))

playerSpells = [fire, thunder, blizzard, meteor, earthquake, cure, cura]

enemySpells = [fire, meteor, curaga]

playerItems = [
  {"Item": potion, "Quantity":15},
  {"Item": hiPotion, "Quantity":5},
  {"Item": superPotion, "Quantity":5},
  {"Item": elixer, "Quantity":2},
  {"Item": hiElixer, "Quantity":2},
  {"Item": grenade, "Quantity":5}
  ]

#create people
player1 = Person("Aakash : ",3260,132,300,34, playerSpells, playerItems)
player2 = Person("Potato : ",4160,100,311,34, playerSpells, playerItems)
player3 = Person("Dragon : ",3889,174,288,34, playerSpells, playerItems)



enemy1 = Person("Sidekick 1", 1120,130,500,325,enemySpells, [])
enemy2 = Person("Main Boss", 11200,221,455,25,enemySpells, [])
enemy3 = Person("Sidekick 2", 1120,130,500,325,enemySpells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]
running = True
i=0
print (bcolours.FAIL + bcolours.BOLD + "AN ENEMY ATTACKS" + bcolours.ENDC )

while running:
  print("==============================")

  #check if battle is over
  defeatedEnemies = 0
  defeatedPlayers = 0 

  #check if player won
  if defeatedEnemies ==2 :
    print(bcolours.OKGREEN +  "You have killed the enemies!!!" + "\n" +"YOU WIN!!!!!!" + bcolours.ENDC)
  
  #check if enemy won
  if defeatedPlayers ==2 :
    print(bcolours.FAIL +  "You have been killed by the enemies!!!" + "\n" +"YOU LOSE!!!!!!" + bcolours.ENDC)

  for player in players:

    print("\n\n")
    player.getStats()
    print("\n\n")

  for enemy in enemies:
    enemy.getEnemyStats()

  
  for player in players:
    player.chooseActions()
    #remove index 0 problem for user
    choice = input("    Choose actions: ")
    index = int(choice) - 1

    if index == 0 :
      damage = player.generateDamage()
      enemy = player.chooseTarget(enemies)
      enemies[enemy].takeDamage(damage)
      print ("You attacked " + enemies[enemy].name.replace(" ", "") + " for " + str(damage))

      if enemies[enemy].getHp() == 0:
        print (bcolours.BOLD + bcolours.OKGREEN + enemies[enemy].name.replace(" ", "") + " has died!" + bcolours.ENDC )
        del enemies[enemy]
    # print ("You attacked for " + str(damage) + "points of damage. Enemy HP : " + str(enemy.getHp()))
    elif index == 1:
      player.chooseMagic()
      #casting
      magicChoice = int(input ("    Choose magic : ")) -1

      if magicChoice == -1:
        continue
      #magicDamage = player.generateSpellDamage(magicChoice)
      #spell = player.getSpellName(magicChoice)
      #cost = player.getSpellCost(magicChoice)
    
      spell = player.magic[magicChoice]
      magicDamage=player.magic[magicChoice].generateDamage()
      currentMagicPoints = player.getMp()
      if spell.cost>currentMagicPoints:
        print (bcolours.FAIL + "You do not have enough MAGIC points" + bcolours.ENDC)
        continue
      else:
        player.reduceMp(spell.cost)
    
      if spell.type == "White":
        player.heal(magicDamage)
        print (bcolours.OKBLUE + "\n" + spell.name + " heals for " + str(magicDamage) + " HP" + bcolours.ENDC)
      elif spell.type == "Black":
        enemy = player.chooseTarget(enemies)
        enemies[enemy].takeDamage(magicDamage)
        
        print(bcolours.OKBLUE + "\n" + spell.name + " spell deals " + str(magicDamage) + " points of damage to " + enemies[enemy].name.replace(" ", "") + bcolours.ENDC)

      if enemies[enemy].getHp() == 0:
        print (bcolours.BOLD + bcolours.OKGREEN + enemies[enemy].name.replace(" ", "") + " has died!" + bcolours.ENDC)
        del enemies[enemy]       

    elif index == 2 :
      player.chooseItem()
      itemChoice = int(input ("    Choose item : ")) -1

      if itemChoice == -1:
        continue

      item = player.items[itemChoice]["Item"]

      #if quantity = 0
      #make sure you can't have -1 items
      if player.items[itemChoice]["Quantity"] == 0:
        print (bcolours.FAIL + "You don't have any " + player.items[itemChoice]["Item"].name + "s left " + bcolours.ENDC)
        continue
      else :
        player.items[itemChoice]["Quantity"] -=1

      if item.type ==  "potion":
        player.heal(item.prop)
        print(bcolours.OKGREEN + "\n" + item.name + " heals for ", str(item.prop) + "HP" + bcolours.ENDC)
      elif item.type == "elixer":

        if item.name == "MegaElixer":
          for i in players:
            i.hp = i.maxHp
            i.mp = i.maxMp
        else:
          player.hp = player.maxHp
          player.mp = player.maxMp
        print(bcolours.OKGREEN + "\n" + item.name + " fully restores HP & MP " + bcolours.ENDC)
      elif item.type == "attack":

        enemy = player.chooseTarget(enemies)
        enemies[enemy].takeDamage(item.prop)
        print(bcolours.FAIL + "\n" + str(item.name) + " deals ", str(item.prop), "points of damage to " + enemies[enemy].name.replace(" ", "") + bcolours.ENDC)

        if enemies[enemy].getHp() == 0:
          print (bcolours.BOLD + bcolours.OKGREEN + enemies[enemy].name.replace(" ", "") + " has died!" + bcolours.ENDC )
          del enemies[enemy]

  

  for player in players:
    if player.getHp() == 0:
      defeatedPlayers += 1


  for enemy in enemies:
    if enemy.getHp() <= 0:
      defeatedEnemies +=1

  

  print ("\n")
  #enemy attack phase
  for enemy in enemies:
            
    #enemy choice of attack
    enemyChoice = random.randrange(0,2) #0 is attack, 1 is magic, 2 is item

    if enemyChoice == 0 : #enemy chooses attack
      #target = random.randrange(0,3) #selects 0, 1 or 2 not 3

      if len(players) == 0:
        running = False
        break

      target = random.randrange(0,len(players))
      enemyDamage = enemies[0].generateDamage()

      players[target].takeDamage(enemyDamage)
      print(enemy.name.replace(" ","") + "Enemy attacks "+ players[target].name.replace(" ","") + "for", enemyDamage)
    elif enemyChoice == 1: #enemy chooses magic
      #enemy chooses spell from available options
      spell = enemy.chooseEnemySpell()
      magicDamage = enemy.chooseEnemySpell1()
      #magicDamage = spell.generateDamage()
      #magicDamage = spell.generateDamage()
      magicType = enemy.chooseEnemySpell2()
      magicName = enemy.chooseEnemySpell3()
      #enemy.reduceMp(spell.cost)

      if magicType == "White":
        enemy.heal(magicDamage)
        print (bcolours.OKBLUE + spell.name + " heals " + enemy.name + " for " + str(magicDamage) + " HP" + bcolours.ENDC)
      elif magicType == "Black":
        #target = random.randrange(0,3) #selects 0, 1 or 2 not 3)
        #target = random.randint(0,2)
        target = random.randrange(0,len(players))
        players[target].takeDamage(magicDamage)
        
        print(bcolours.OKBLUE + enemy.name.replace(" ","") + " uses " + magicName + " and the spell deals " + str(magicDamage) + " points of damage to " + players[target].name.replace(" ", "") + bcolours.ENDC)

        if players[target].getHp() == 0:
          print (bcolours.BOLD + bcolours.OKGREEN + players[target].name.replace(" ", "") + " has died!" + bcolours.ENDC)
          del players[target] #maybe players[player]


      #print("Enemy chose", spell.name, "Damage is", magicDamage )


    print ("%%%%%%%%%%%%%%%%%%%%%%%%%" + "\n")
    print("Enemy HP", bcolours.FAIL + str(enemy.getHp()) + "/" + str(enemy.getMaxHp()) + bcolours.ENDC + "\n" + "\n")

    print ("Your HP", bcolours.OKGREEN + str(player.getHp()) + "/" + str(player.getMaxHp()) + bcolours.ENDC)
    print("Your MP", bcolours.OKBLUE + str(player.getMp()) + "/" + str(player.getMaxMp()) + bcolours.ENDC + "\n")


    #print ("You chose", player.getSpellName(int(choice)))

  if player.getHp() <= 0:
    print (bcolours.FAIL+"!!!!!!!!!!!!!!!!" + bcolours.ENDC)
    print (bcolours.FAIL+"You have been killed. UNLUCKY" + bcolours.ENDC)
    running = False

  
  
  if enemy.getHp() <= 0:
    print (bcolours.OKGREEN+ "!!!!!!!!!!!!!!!!" + bcolours.ENDC)
    print (bcolours.OKGREEN +  "You have killed the enemy!!!" + bcolours.ENDC)
    running = False
  



  '''print("Let's overflow this stack", i)
  i=+1'''
  ''' Code to entire game is here
  https://github.com/nickgermaine/
  '''
