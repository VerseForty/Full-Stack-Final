from django.db import models
from django.forms import ModelForm


class characterTable(models.Model):
    userID = models.CharField(max_length = 32)
    playerName = models.CharField(max_length = 32)
    race = models.CharField(max_length = 32)
    playerClass = models.CharField(max_length = 32)
    strength = models.CharField(max_length = 2)
    dexterity = models.CharField(max_length = 2)
    constitution = models.CharField(max_length = 2)
    intelligence = models.CharField(max_length = 2)
    wisdom = models.CharField(max_length = 2)
    charisma = models.CharField(max_length = 2)

    def __str__(self):
        return (self.userID + " " + self.playerName + " " + self.race + " " + self.playerClass + " " + self.strength + " " + self.dexterity + " " + self.constitution + " " + self.wisdom + " " + self.charisma)


class monsterTable(models.Model):
    monsterName = models.CharField(max_length = 32)
    monsterCR = models.CharField(max_length = 3)
    monsterHP = models.CharField(max_length = 3)
    monsterAC = models.CharField(max_length = 3)
    special = models.CharField(max_length = 32)

    def __str__(self):
        return(self.monsterName)
# Create your models here.
