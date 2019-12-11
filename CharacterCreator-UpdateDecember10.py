#!/usr/bin/env python
# coding: utf-8

# In[49]:


class character:
    def __init__(characterC, name, AC, dexterity, constitution, strength, intelligence, wisdom, charisma, level, HP, Class, feature,weapon,Race):
        characterC.name = name
        characterC.AC = AC
        characterC.dexterity = dexterity
        characterC.constitution = constitution
        characterC.strength = strength
        characterC.intelligence = intelligence
        characterC.wisdom = wisdom
        characterC.charisma = charisma
        characterC.level = level
        characterC.HP = HP
        characterC.Class = Class
        characterC.feature = feature
        characterC.weapon = weapon
        characterC.Race = Race

        
class monster:
    def __init__(mon, CR, name, AC, HP, ability):
        mon.CR = CR
        mon.name = name
        mon.AC = AC
        mon.HP = HP
        mon.ability = ability
        
    
class fighter(character):
    def __init__(fighterC,name, AC, dexterity, constitution, strength, intelligence, wisdom, charisma, level, HP, Class, feature,weapon,Race):
        super().__init__(name, AC, dexterity, constitution, strength, intelligence, wisdom, charisma, level, HP, Class, feature,weapon,Race)
        
        
class rogue(character):
    def __init__(rogueC,name, AC, dexterity, constitution, strength, intelligence, wisdom, charisma, level, HP, Class, feature,weapon,Race):
        super().__init__(name, AC, dexterity, constitution, strength, intelligence, wisdom, charisma, level, HP, Class, feature,weapon,Race)
        
        
        
        
        
class wizard(character):
     def __init__(wizardC,name, AC, dexterity, constitution, strength, intelligence, wisdom, charisma, level, HP, Class, feature,weapon,Spell,Race):
        super().__init__(name, AC, dexterity, constitution, strength, intelligence, wisdom, charisma, level, HP, Class, feature,weapon,Race)
        wizardC.Spell = Spell
        

c = fighter("Chris", 10, 10, 10, 11, 10, 10, 10, 3, 30,"Fighter","Dodge","Club","Human")



r = rogue("Rick",  10, 11, 10, 10, 10, 10, 10, 3,30,"Rogue","Dodge","Club","Human")

w = wizard("Wallace", 11, 11,11,11,11,11,11,3, 30, "Wizard","Dodge","Club","Acid Splash","Human")
    


# In[50]:


m = monster(1, "Ghoul", 14, 12, "Bite")

m1 = monster(1, "Imp", 17, 16, "Sting")


def makingCharacter():
   
    dexStat = int(input("what is your dexterity"))
    
    strStat = int(input("what is your strength"))
     
    Yato = fighter("Chris", 10, dexStat, 10, strStat, 10, 10, 10, 3, 30,"Fighter","Dodge","Club","Human")
    
    race = input("Enter your race")
    
    if(race == "Human"):
            
        x = 2
            
        print("because you are human one stat will be raised by 2")
            
        statRaise = input("Which stat would you like to increase? Dex or Str")
        if(statRaise == "Dex"):
            Yato.dexterity = Yato.dexterity + 2
        elif(statRaise == "Str"):
            Yato.stength = Yato.strength + 2
    
    if(race == "Elf"):
        y = 2
        print("2 Dexterity, +2 Intelligence, –2 Constitution")
        Yato.dexterity = Yato.dexterity + 2
        Yato.intelligence = Yato.intelligence + 2
        Yato.constitution = Yato.constitution - 2
    
    return print(Yato.dexterity,Yato.intelligence,Yato.constitution)
        
    


# In[ ]:





# In[51]:


makingCharacter()


# In[52]:


def rollToHit(character):
    
    accuracy = random.randint(1,20)
    prof = proficiency(character)
    
    return accuracy + prof


# In[53]:


def proficiency(character):
    if character.level == 3:
        return 3
    elif character.level == 4:
        return 4
    elif character.level == 5:
        return 5
    elif character.level == 6:
        return 6
    elif character.level == 7:
        return 7
    elif character.level == 8:
        return 8
    elif character.level == 9:
        return 9
    elif character.level == 10:
        return 10
    elif character.level == 11:
        return 11
    elif character.level == 12:
        return 12
    elif character.level == 13:
        return 13
    elif character.level == 14:
        return 14
    elif character.level == 15:
        return 15
    elif character.level == 16:
        return 16
    elif character.level == 17:
        return 17
    elif character.level == 18:
        return 18
    elif character.level == 19:
        return 19
    elif character.level == 20:
        return 20


# In[54]:


def Battle(character, monster):
    
    monsterHP = monster.HP
    
    characterHP = character.HP
    
    while monsterHP > 0 or characterHP > 0:
        
        RTH = input("Roll to his? Type YES or NO")
        print(RTH)
        if(RTH == "YES"):
        
            z = Battle1(character, monster)
            
            x = monsterHP - z
            
            monsterHP = x
            
            print(monsterHP)
            
            
            if(monsterHP <= 0):
                break
            
            zz = monBattle(character,monster)
            
            xx = characterHP - zz
            
            characterHP = xx
            
            print(characterHP)
            
            
        elif(RTH == "NO"):
            
            print("PASS")
        
        elif(RTH == "END"):
            break


# In[55]:


def Battle1(character, monster):
    accuracy = rollToHit(character)
    if accuracy >= monster.AC:
        attack = ifWizard(character) + weapon(character) + PlayerClassDamage(character) 
        return attack
    elif accuracy < monster.AC:
        return 0
    


# In[56]:


import random
def weapon(character):
    print("Swung" + character.weapon)
    if(character.weapon == "Club"):
        weapon = random.randint(1,6)
        return weapon + character.strength
    if(character.weapon == "Mace"):
        club = random.randint(1,8) 
        return weapon + character.strength
    if(character.weapon == "Simitar"):
        weapon = random.randint(1,6) 
        return weapon + character.strength
    if(character.weapon == "Longbow"):
        weapon = random.randint(1,8)
        return weapon + character.dexterity
    if(character.weapon == "Shortbow"):
        weapon = random.randint(1,6)
        return weapon + character.dexterity
    if(character.weapon == "Longsword"):
        weapon = random.randint(1,8)
        return weapon + character.strength


# In[ ]:





# In[57]:


def ifWizard(character):
    if(character.Class == "Wizard"):
        print("is a wizard")
        UAP = input("Use a Spell? Type YES or NO")
        if(UAP == "YES"):
            spellAttack = input("Please enter your spell")
            if(spellAttack == "Acid Splash"):
                if(spellAttack == character.Spell):
                    AS = random.randint(1,6)
                    return AS
        
            
            
    else:
        return 0
    


# In[58]:


def PlayerClassDamage(x):
    if(x.Class == "Fighter"):
        return ClassFighterDamage(x)
        print("called functionfighter")
    if(x.Class == "Rogue"):
        return ClassRougeDamage(x)
        print("called functionrogue")
    if(x.Class == "Wizard"):
        return ClassWizardDamage(x)
        print("called functionwizard")


# In[59]:



def ClassFighterDamage(x):
        if(x.level == 1):
            BaseAttackBonus = 1
        elif(x.level == 2):
            BaseAttackBonus = 2
        elif(x.level == 3):
            BaseAttackBonus = 3
        elif(x.level == 4):
            BaseAttackBonus = 4
        elif(x.level == 5):
            BaseAttackBonus = 5
        elif(x.level == 6):
            BaseAttackBonus = 6
        elif(x.level == 7):
            BaseAttackBonus = 7
        elif(x.level == 8):
            BaseAttackBonus = 8
        elif(x.level == 9):
            BaseAttackBonus = 9
        elif(x.level == 10):
            BaseAttackBonus = 10
        elif(x.level == 11):
            BaseAttackBonus = 11
        elif(x.level == 12):
            BaseAttackBonus = 12
        elif(x.level == 13):
            BaseAttackBonus = 13
        elif(x.level == 14):
            BaseAttackBonus = 14
        elif(x.level == 15):
            BaseAttackBonus = 15
        elif(x.level == 16):
            BaseAttackBonus = 16
        elif(x.level == 17):
            BaseAttackBonus = 17
        elif(x.level == 18):
            BaseAttackBonus = 18 
        elif(x.level == 19):
            BaseAttackBonus = 19
        elif(x.level == 20):
            BaseAttackBonus = 20
        return BaseAttackBonus
    
def ClassRougeDamage(x):
        if(x.level == 1):
            BaseAttackBonus = 0
        elif(x.level == 2):
            BaseAttackBonus = 1
        elif(x.level == 3):
            BaseAttackBonus = 2
        elif(x.level == 4):
            BaseAttackBonus = 3
        elif(x.level == 5):
            BaseAttackBonus = 3
        elif(x.level == 6):
            BaseAttackBonus = 4
        elif(x.level == 7):
            BaseAttackBonus = 5
        elif(x.level == 8):
            BaseAttackBonus = 6
        elif(x.level == 9):
            BaseAttackBonus = 6
        elif(x.level == 10):
            BaseAttackBonus = 7
        elif(x.level == 11):
            BaseAttackBonus = 8
        elif(x.level == 12):
            BaseAttackBonus = 9
        elif(x.level == 13):
            BaseAttackBonus = 9
        elif(x.level == 14):
            BaseAttackBonus = 10
        elif(x.level == 15):
            BaseAttackBonus = 11
        elif(x.level == 16):
            BaseAttackBonus = 12 
        elif(x.level == 17):
            BaseAttackBonus = 12
        elif(x.level == 18):
            BaseAttackBonus = 13
        elif(x.level == 19):
            BaseAttackBonus = 14
        elif(x.level == 20):
            BaseAttackBonus = 15
        return BaseAttackBonus
    
    
def ClassWizardDamage(x):
        if(x.level == 1):
            w.BaseAttackBonus = 0
        elif(x.level == 2):
            w.BaseAttackBonus = 1
        elif(x.level == 3):
            w.BaseAttackBonus = 1
        elif(x.level == 4):
            w.BaseAttackBonus = 2
        elif(x.level == 5):
            w.BaseAttackBonus = 2
        elif(x.level == 6):
            w.BaseAttackBonus = 3
        elif(x.level == 7):
            w.BaseAttackBonus = 3
        elif(x.level == 8):
            w.BaseAttackBonus = 4
        elif(x.level == 9):
            w.BaseAttackBonus = 4
        elif(x.level == 10):
            w.BaseAttackBonus = 5
        elif(x.level == 11):
            w.BaseAttackBonus = 5
        elif(x.level == 12):
            w.BaseAttackBonus = 6
        elif(x.level == 13):
            w.BaseAttackBonus = 6
        elif(x.level == 14):
            w.BaseAttackBonus = 7
        elif(x.level == 15):
            w.BaseAttackBonus = 7
        elif(x.level == 16):
            w.BaseAttackBonus = 8 
        elif(x.level == 17):
            w.BaseAttackBonus = 8
        elif(x.level == 18):
            w.BaseAttackBonus = 9
        elif(x.level == 19):
            w.BaseAttackBonus = 9
        elif(x.level == 20):
            w.BaseAttackBonus = 10
        return w.BaseAttackBonus


# In[60]:


def monBattle(character,monster):
    
    
    accuracy = rollToHitMon(monster)
    
    
    newAC = character.AC + feats(character)
    
    if accuracy >= newAC:
        
        attack = attackMon(monster)
        
        return attack
    
    elif accuracy < newAC:
        
        return 0
        
  
        


# In[61]:


def rollToHitMon(monster):
    accuracy = random.randint(1,20)
#    prof = proficiencyMon(character)
    
    return accuracy 


# In[67]:


def attackMon(monster):
    if(monster.ability == "Bite"):
        print("Monster used Bite")
        attack = random.randint(1,4)
    elif(monster.ability == "Sting"):
        attack = random.randint(1,5)
    return attack


# In[ ]:





# In[63]:


def feats(character):
    if(c.feature == 'Dodge'):
        return dodgeFeature()
    else:
        return 0
    


# In[64]:


def dodgeFeature():
    print("In dodgeFeature")
    return 1


# In[68]:


Battle(c,m)


# In[ ]:


Battle(r,m)


# In[ ]:


Battle(w,m)


# In[ ]:




