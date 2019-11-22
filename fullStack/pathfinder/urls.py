from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('characterCreator/', views.characterCreator, name='characterCreator'),
    path('beginnersGuide/', views.beginnersGuide, name='beginnersGuide'),
    path('battleSim/', views.battleSim, name='battleSim'),
    path('info/', views.info, name='info'),
    path('login/', views.login, name='login')




]
