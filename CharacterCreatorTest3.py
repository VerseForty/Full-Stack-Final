#!/usr/bin/env python
# coding: utf-8

# In[42]:


class character:
    def __init__(characterC, name, AC, dexterity, constitution, strength, intelligence, wisdom, charisma, level, HP, Class, feature,weapon):
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


        
class monster:
    def __init__(mon, CR, name, AC, HP, ability):
        mon.CR = CR
        mon.name = name
        mon.AC = AC
        mon.HP = HP
        mon.ability = ability
        
    
class fighter(character):
    def __init__(fighterC, level, BaseAttackBonus, Fortitude, Reflex, Will, Special):
        fighterC.level = level
        fighterC.BaseAttackBonus = BaseAttackBonus
        fighterC.Fortitude = Fortitude
        fighterC. Reflex = Reflex
        fighterC.Will = Will
class rogue(character):
    def __init__(rogueC, level, BaseAttackBonus, Fortitude, Reflex, Will, Special):
        rogueC.level = level
        rogueC.BaseAttackBonus = BaseAttackBonus
        rogueC.Fortitude = Fortitude
        rogueC.Reflex = Reflex
        rogueC.Will = Will
        
        
        
        
        
class wizard(character):
     def __init__(wizardC,name, AC, dexterity, constitution, strength, intelligence, wisdom, charisma, level, HP, Class, feature,weapon,Spell):
        super().__init__(name, AC, dexterity, constitution, strength, intelligence, wisdom, charisma, level, HP, Class, feature,weapon)
        wizardC.Spell = Spell


# In[52]:


c = character("Chris", 10, 10, 10, 11, 10, 10, 10, 3, 30,"Fighter","Dodge","Club")

f = fighter(0,0,0,0,0,0)

r = character("Rick",  10, 11, 10, 10, 10, 10, 10, 3,30,"Rogue","Dodge","Club")

w = wizard("Wallace", 11, 11,11,11,11,11,11,3, 30, "Wizard","Dodge","Club","Acid Splash")
    


# In[53]:


m = monster(1, "Ghoul", 14, 12, "Bite" )
m.name

c.name
r.dexterity
w.Spell


# In[ ]:





# In[54]:


def rollToHit(character):
    accuracy = random.randint(1,20)
    prof = proficiency(character)
    
    return accuracy + prof


# In[55]:


def proficiency(character):
    if character.level == 3:
        print("Hi")
        return 3
    elif character.level == 4:
        print("yo")
        return 4
    elif character.level == 5:
        print("yoda")
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


# In[56]:


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


# In[57]:


def Battle1(character, monster):
    accuracy = rollToHit(character)
    if accuracy >= monster.AC:
        attack = attack1(character) + weapon(character) + PlayerClassDamage(character)
        return attack
    elif accuracy < monster.AC:
        return 0
    


# In[58]:


import random
def weapon(character):
    print("Swung Club")
    if(character.weapon == "Club"):
        club = random.randint(1,6)
        return club


# In[59]:


def attack1(character):
    if(character.Class == "Fighter"):
        return fighterAttack(character)
    elif(character.Class == "Rogue"):
        return rogueAttack(character)
    elif(character.Class == "Wizard"):
        return wizardAttack(character)


# In[60]:


def fighterAttack(character):
    if character.strength == 11:
        return 1
    elif character.strength == 12:
        return 2
    elif character.strength == 13:
        return 3
    elif character.strength == 14:
        return 5
    elif character.strength == 15:
        return 7
    elif character.strength == 16:
        return 10 
    elif character.strength == 17:
        return 13
    elif character.strength == 18:
        return 14
    
def rogueAttack(character):
    if character.dexterity == 11:
        return 1
    elif character.dexterity == 12:
        return 2
    elif character.dexterity == 13:
        return 3
    elif character.dexterity == 14:
        return 5
    elif character.dexterity == 15:
        return 7
    elif character.dexterity == 16:
        return 10 
    elif character.dexterity == 17:
        return 13
    elif character.dexterity == 18:
        return 14
    
def wizardAttack(character):
    if character.dexterity == 11:
        return 1
    elif character.dexterity == 12:
        return 2
    elif character.dexterity == 13:
        return 3
    elif character.dexterity == 14:
        return 5
    elif character.dexterity == 15:
        return 7
    elif character.dexterity == 16:
        return 10 
    elif character.dexterity == 17:
        return 13
    elif character.dexterity == 18:
        return 14


# In[61]:


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


# In[68]:



def ClassFighterDamage(x):
    print("in classfighter")
    if(x.Class == "Fighter"):
        if(x.level == 1):
            f.BaseAttackBonus = 1
        elif(x.level == 2):
            f.BaseAttackBonus = 2
        elif(x.level == 3):
            f.BaseAttackBonus = 3
        elif(x.level == 4):
            f.BaseAttackBonus = 4
        elif(x.level == 5):
            f.BaseAttackBonus = 5
        elif(x.level == 6):
            f.BaseAttackBonus = 6
            #suppose to add multiple hits
        elif(x.level == 7):
            f.BaseAttackBonus = 7
        elif(x.level == 8):
            f.BaseAttackBonus = 8
        elif(x.level == 9):
            f.BaseAttackBonus = 9
        elif(x.level == 10):
            f.BaseAttackBonus = 10
        elif(x.level == 11):
            f.BaseAttackBonus = 11
        elif(x.level == 12):
            f.BaseAttackBonus = 12
        elif(x.level == 13):
            f.BaseAttackBonus = 13
        elif(x.level == 14):
            f.BaseAttackBonus = 14
        elif(x.level == 15):
            f.BaseAttackBonus = 15
        elif(x.level == 16):
            f.BaseAttackBonus = 16
        elif(x.level == 17):
            f.BaseAttackBonus = 17
        elif(x.level == 18):
            f.BaseAttackBonus = 18 
        elif(x.level == 19):
            f.BaseAttackBonus = 19
        elif(x.level == 20):
            f.BaseAttackBonus = 20
        return f.BaseAttackBonus
    
def ClassRougeDamage(x):
    print("is a rogue")
    if(x.Class == "Rogue"):
        if(x.level == 1):
            r.BaseAttackBonus = 0
        elif(x.level == 2):
            r.BaseAttackBonus = 1
        elif(x.level == 3):
            r.BaseAttackBonus = 2
        elif(x.level == 4):
            r.BaseAttackBonus = 3
        elif(x.level == 5):
            r.BaseAttackBonus = 3
        elif(x.level == 6):
            r.BaseAttackBonus = 4
        elif(x.level == 7):
            r.BaseAttackBonus = 5
        elif(x.level == 8):
            r.BaseAttackBonus = 6
        elif(x.level == 9):
            r.BaseAttackBonus = 6
        elif(x.level == 10):
            r.BaseAttackBonus = 7
        elif(x.level == 11):
            r.BaseAttackBonus = 8
        elif(x.level == 12):
            r.BaseAttackBonus = 9
        elif(x.level == 13):
            r.BaseAttackBonus = 9
        elif(x.level == 14):
            r.BaseAttackBonus = 10
        elif(x.level == 15):
            r.BaseAttackBonus = 11
        elif(x.level == 16):
            r.BaseAttackBonus = 12 
        elif(x.level == 17):
            r.BaseAttackBonus = 12
        elif(x.level == 18):
            r.BaseAttackBonus = 13
        elif(x.level == 19):
            r.BaseAttackBonus = 14
        elif(x.level == 20):
            r.BaseAttackBonus = 15
        return r.BaseAttackBonus
    
    
def ClassWizardDamage(x):
    
    print("is a wizard")
    UAP = input("Use a Spell? Type YES or NO")
    if(UAP == "YES"):
        spellAttack = input("Please enter your spell")
        if(spellAttack == "Acid Splash"):
            if(spellAttack == x.Spell):
                AS = random.randint(1,6)
                return AS
        
            
            
    elif(x.Class == "Wizard"):
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


# In[69]:


def monBattle(character,monster):
    accuracy = rollToHitMon(monster)
    newAC = character.AC + feats(character)
    if accuracy >= newAC:
        print("THIS IS NEW AC",newAC)
        attack = attackMon(monster)
        return attack
    elif accuracy < newAC:
        return 0
        
  
        


# In[70]:


def rollToHitMon(monster):
    accuracy = random.randint(1,20)
#    prof = proficiencyMon(character)
    
    return accuracy 


# In[71]:


def attackMon(monster):
    return monster.CR


# In[72]:


def feats(character):
    if(c.feature == 'Dodge'):
        return dodgeFeature()
    else:
        return 0
    


# In[73]:


def dodgeFeature():
    print("In dodgeFeature")
    return 1


# In[74]:


Battle(c,m)


# In[20]:


Battle(r,m)


# In[75]:


Battle(w,m)


# In[ ]:




