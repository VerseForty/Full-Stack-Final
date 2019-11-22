#!/usr/bin/env python
# coding: utf-8

# In[35]:


class character:
    def __init__(characterC, name, AC, dexterity, constitution, strength, intelligence, wisdom, charisma, level, HP):
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



        
class monster:
    def __init__(mon, CR, name, AC, HP, ability):
        mon.CR = CR
        mon.name = name
        mon.AC = AC
        mon.HP = HP
        mon.ability = ability
        


# In[102]:


c = character("Chris", 10, 10, 10, 11, 10, 10, 10, 3, 30)
c.name


# In[103]:


m = monster(1, "Ghoul", 14, 12, "Bite" )
m.name


# In[104]:


import random
club = random.randint(1,6)
print(club)


# In[105]:


def rollToHit(character):
    accuracy = random.randint(1,20)
    prof = proficiency(character)
    
    return accuracy + prof


# In[106]:


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


# In[107]:


def Battle(character, monster):
    
    monsterHP = monster.HP
    
    while monsterHP > 0:
        z = Battle1(character, monster)
        x = monsterHP - z
        monsterHP = x
        print(monsterHP)
        


# In[108]:


def Battle1(character, monster):
    accuracy = rollToHit(character)
    if accuracy >= monster.AC:
        attack = attack1(character) + club
        return attack
    elif accuracy < monster.AC:
        return 0


# In[111]:


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


# In[112]:


Battle(c,m)


# In[ ]:




