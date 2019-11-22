#!/usr/bin/env python
# coding: utf-8

# In[5]:


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
        


# In[6]:


c = character("Chris", 10, 10, 10, 11, 10, 10, 10, 3, 30)
c.name


# In[7]:


m = monster(1, "Ghoul", 14, 12, "Bite" )
m.name


# In[8]:


import random
club = random.randint(1,6)
print(club)


# In[9]:


def rollToHit(character):
    accuracy = random.randint(1,20)
    prof = proficiency(character)
    
    return accuracy + prof


# In[10]:


def proficiency(character):
    if character.level == 3:
        return 3
    


# In[12]:


def Battle(character, monster):
    
    monsterHP = monster.HP
    
    while monsterHP > 0:
        z = Battle1(character, monster)
        x = monsterHP - z
        monsterHP = x
        print(monsterHP)
        


# In[13]:


def Battle1(character, monster):
    accuracy = rollToHit(character)
    if accuracy >= monster.AC:
        attack = attack1(character) + club
        return attack
    elif accuracy < monster.AC:
        return 0


# In[14]:


def attack1(character):
    if character.strength == 11:
        return 1


# In[15]:


Battle(c,m)


# In[ ]:




