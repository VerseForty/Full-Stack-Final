#!/usr/bin/env python
# coding: utf-8

# In[1]:


class character:
    def __init__(characterC, name, AC, dexterity, constitution, strength, intelligence, wisdom, charisma, level, HP, Class):
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


        
class monster:
    def __init__(mon, CR, name, AC, HP, ability):
        mon.CR = CR
        mon.name = name
        mon.AC = AC
        mon.HP = HP
        mon.ability = ability
        
    
class fighter:
    def __init__(fighterC, level, BaseAttackBonus, Fortitude, Reflex, Will, Special):
        fighterC.level = level
        fighterC.BaseAttackBonus = BaseAttackBonus
        fighterC.Fortitude = Fortitude
        fighterC. Reflex = Reflex
        fighterC.Will = Will
        fighterC.Special = Special
        
        


# In[2]:


c = character("Chris", 10, 10, 10, 11, 10, 10, 10, 3, 30,"Fighter")

f = fighter(0,0,0,0,0,0)


    


# In[3]:


m = monster(1, "Ghoul", 14, 12, "Bite" )
m.name


# In[4]:


import random
club = random.randint(1,6)
print(club)


# In[5]:


def rollToHit(character):
    accuracy = random.randint(1,20)
    prof = proficiency(character)
    
    return accuracy + prof


# In[6]:


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


# In[7]:


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


# In[8]:


def Battle1(character, monster):
    accuracy = rollToHit(character)
    if accuracy >= monster.AC:
        attack = attack1(character) + club + PlayerClassDamage(character)
        return attack
    elif accuracy < monster.AC:
        return 0
    


# In[9]:


def attack1(character):
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
        return 17


# In[ ]:





# In[ ]:





# In[10]:


def PlayerClassDamage(x):
    if(x.Class == "Fighter"):
        return ClassFighterDamage(x)
        print("called functionfighter")


# In[ ]:





# In[11]:



def ClassFighterDamage(x):
    print("in classfighter")
    if(x.Class == "Fighter"):
        
        if(x.level == 3):
            f.BaseAttackBonus = 1
            return f.BaseAttackBonus
    


# In[12]:


def monBattle(character,monster):
    accuracy = rollToHitMon(monster)
    if accuracy >= character.AC:
        attack = attackMon(monster)
        return attack
    elif accuracy < character.AC:
        return 0
        
  
        


# In[13]:


def rollToHitMon(monster):
    accuracy = random.randint(1,20)
#    prof = proficiencyMon(character)
    
    return accuracy 


# In[14]:


def attackMon(monster):
    return monster.CR


# In[15]:


Battle(c,m)


# In[ ]:




