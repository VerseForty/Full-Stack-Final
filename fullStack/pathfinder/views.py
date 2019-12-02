# this file and implementation of static HTML based off of Amos Omondi's tutorial on scotch.io: https://scotch.io/tutorials/working-with-django-templates-static-files
from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView
from django.http import HttpResponse
from pathfinder.models import characterTable
from pathfinder.models import monsterTable

from django.shortcuts import get_object_or_404
#function to add a character string to our characterTable model in the database
#this implementation based off of Maddie Graham's solution on StackOverflow: https://stackoverflow.com/a/59079292/12352379
def addCharacter(sUserID, sPlayerName, sRace, sPlayerClass, sStr, sDex, sCon, sInt, sWis, sCha):
    c = characterTable()
    c.userID=sUserID
    c.playerName = sPlayerName
    c.race = sRace
    c.playerClass = sPlayerClass
    c.strength = sStr
    c.dexterity = sDex
    c.constitution = sCon
    c.intelligence = sInt
    c.wisdom = sWis
    c.charisma = sCha
    c.save()


# Add the two views we have been talking about  all this time :)
class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class CharacterCreatorView(TemplateView):
    template_name = "characterCreator.html"

    # this solution courtesy of Eliakin Costa on StackOverflow: https://stackoverflow.com/a/59112612/12352379
    def post(self, request, *args, **kwargs):
        userID = 'testUser'
        addCharacter(
            userID,
            str(request.POST.get('characterName')),
            str(request.POST.get('race')),
            str(request.POST.get('class')),
            str(request.POST.get('strength')),
            str(request.POST.get('dexterity')),
            str(request.POST.get('constitution')),
            str(request.POST.get('intelligence')),
            str(request.POST.get('wisdom')),
            str(request.POST.get('charisma'))
        )

        return render(request, self.template_name, {})

class battleSimView(TemplateView):
    template_name = "battleSim.html"


    def get(self, request, *args, **kwargs):
       character  = characterTable.objects.all() # use filter() when you have sth to filter ;)
       monster = monsterTable.objects.all()
       return render(request, self.template_name, {'characters':character, 'monsters':monster},)




class beginnersGuideView(TemplateView):
    template_name = "beginnersGuide.html"

class infoView(TemplateView):
    template_name = "info.html"
