import random
import classes.magic
import classes.inventory
#import pretty print 
import pprint

class bcolours:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

class Person:
  def __init__(self, name, hp, mp, attack, defence, magic, items ):
    self.maxHp = hp #maximum
    self.hp = hp
    self.maxMp = mp
    self.mp = mp
    self.attackHigh = attack + 10
    self.attackLow = attack - 10
    self.defence = defence
    self.magic = magic
    self.items = items
    self.actions = ["Attack", "Magic", "Items"]
    self.name = name

  def generateDamage(self):
    return random.randrange(self.attackLow, self.attackHigh)

  #def generateSpellDamage(self, indexNo):
    #ngLow=self.magic[indexNo]["damage"] -5
    #ngHigh=self.magic[indexNo]["damage"] +5
    #return random.randrange(ngLow, ngHigh)

  def takeDamage(self, damage):
    #print (damage)
    if damage == None:
      return self.hp
    self.hp = self.hp - damage
    if self.hp < 0:
      self.hp = 0
    return self.hp

  def heal(self, damage):
    self.hp += damage
    if  self.hp > self.maxHp:
      self.hp = self.maxHp

  def getHp(self):
    return self.hp

  def getMaxHp(self):
    return self.maxHp

  def getMp(self):
    return self.mp

  def getMaxMp(self):
    return self.maxMp

  def reduceMp(self, cost):
    self.mp = self.mp - cost
   # self.mp -= cost
    return self.mp

  #def getSpellName(self, indexNo):
    #return self.magic[indexNo]["name"]  

  #def getSpellCost(self, indexNo):
    #return self.magic[indexNo]["cost"]

  def chooseActions(self):
   indexNo=1
   print("\n" + "    " +bcolours.BOLD + self.name + bcolours.ENDC)
   print("\t" + bcolours.OKBLUE + "    ACTIONS" + bcolours.ENDC)
   for item in self.actions:
     print("    " + str(indexNo)+ " . " + item)   
     indexNo += 1  

  def chooseMagic(self):
   indexNo=1
   print("\t" + bcolours.OKBLUE + "    MAGIC" + bcolours.ENDC)
   for spell in self.magic:
     print("    " + str(indexNo), " . " , spell.name, "cost : ", spell.cost) 
     #print(str(indexNo), " : " , item["name"], "cost : ",str(item["cost"]))   
     indexNo += 1  

  def chooseItem(self):
    i = 1

    print ("\t" +bcolours.OKGREEN + bcolours.OKBLUE + "    ITEMS" + bcolours.ENDC)   
    for item in self.items:
      print("    " + str(i) + " . ", item["Item"].name, " : ", item["Item"].description, "[x" + str(item["Quantity"])+"]")
      i += 1

  def chooseTarget(self, enemies):
    i=1
    print(bcolours.BOLD + bcolours.FAIL + "    TARGET:" + bcolours.ENDC)
    for enemy in enemies:
      if enemy.getHp() != 0: 
        print ("    " + str(i) + "." + enemy.name)
        i+=1
    choice = int(input("    Choose Target: "))-1  
    return choice


  def getEnemyStats(self):
    hpBar = ""
    barTicks = (self.hp / self.maxHp) * 100 / 2
    while barTicks >0:
      hpBar += "█"
      barTicks -= 1



    while len(hpBar)< 50:
      hpBar += " "
    
    hpString = str(self.hp) + "/" + str(self.maxHp)
    currentHp = ""

    if len(hpString) < 11:
      decreased = 11/ - len(hpString)

      while decreased > 0:
        currentHp += " "
        decreased -= 1


    print( "NAME                           HP ")

    print( "                               --------------------------------------------------")
    print( bcolours.BOLD + self.name + "       " + str(self.hp) + "/" + str(self.maxHp) + "   |" + bcolours.FAIL + hpBar + bcolours.ENDC + bcolours.BOLD + "|  " +  bcolours.ENDC)



  def getStats(self):
    hpBar = ""
    #divide by 4 because 25 blocks - each block is 4% of health
    hpBarTicks = (self.hp / self.maxHp) * 100 / 4

    while hpBarTicks > 0:
      hpBar += "█" 
      hpBarTicks -= 1

    while len(hpBar) < 25:
      hpBar += " "

    mpBar = ""
    mpBarTicks = (self.mp / self.maxMp) * 100 /10

    while mpBarTicks > 0:
      mpBar += "█" 
      mpBarTicks -= 1

    while len(mpBar) < 10:
      mpBar += " "

    hpString = str(self.hp) + "/" + str(self.maxHp)
    currentHp = ""

    if len(hpString) < 9:
      decreased = 9 - len(hpString)

      while decreased > 0:
        currentHp += " "
        decreased -= 1


    print( "NAME                        HP                                    MP ")
    print( "                            -------------------------             ----------")
    print( bcolours.BOLD + self.name + "       " + str(self.hp) + "/" + str(self.maxHp) + "   |" + bcolours.OKGREEN + hpBar + bcolours.ENDC + bcolours.BOLD + "|  " + str(self.mp) + "/" + str(self.maxMp) + " |" + bcolours.ENDC + bcolours.OKBLUE + mpBar + bcolours.ENDC + bcolours.BOLD + "|" + bcolours.ENDC)

  def chooseEnemySpell(self):
    enemyMagicChoice = random.randrange(0,(len(self.magic)-1))
    spell = self.magic[enemyMagicChoice]
    
    print (spell.name)
    magicDamage = spell.generateDamage()
    percentageOfEnemyHP = self.hp/self.maxHp * 100
    #if spell.type == "White" and percentageOfEnemyHP > 50:
      #if they have over 50% health and they choose a heal spell, they choose again
      #self.chooseEnemySpell()
    #else:
      #return spell
    if self.mp< spell.cost:
      #if they don't have enough magic points they choose again
      #self.chooseEnemySpell()
      #recursion error becuase you won't have enough MP for any of the spells
      print ("You don't have even magic points!!!!! BOI")
    elif spell.type == "White" and percentageOfEnemyHP > 50:
        self.chooseEnemySpell()
    else:
      return spell
    #can add AI - if HP below 20% then use heal

  def chooseEnemySpell1(self):
    enemyMagicChoice = random.randrange(0,(len(self.magic)-1))
    spell = self.magic[enemyMagicChoice]

   
    magicDamage = self.magic[enemyMagicChoice].generateDamage()
    percentageOfEnemyHP = self.hp/self.maxHp * 100

    if self.mp< spell.cost or (spell.type == "White" and percentageOfEnemyHP > 50):
      #if they don't have enough magic points they choose again
      #if they have over 50% health and they choose a heal spell, they choose again
      self.chooseEnemySpell()
    else:
      self.reduceMp(spell.cost)
      return magicDamage  

  def chooseEnemySpell2(self):
    enemyMagicChoice = random.randrange(0,(len(self.magic)-1))
    spell = self.magic[enemyMagicChoice]
    magicType = spell.type
    return magicType  

  def chooseEnemySpell3(self):
    enemyMagicChoice = random.randrange(0,(len(self.magic)-1))
    spell = self.magic[enemyMagicChoice]
    magicName = spell.name
    return magicName