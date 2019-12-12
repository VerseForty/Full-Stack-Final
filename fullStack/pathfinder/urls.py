#references to other pages that are needed
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    #path('characterCreator/', views.characterCreator, name='characterCreator'),
    #path('beginnersGuide/', views.beginnersGuide, name='beginnersGuide'),
    #path('battleSim/', views.battleSim, name='battleSim'),
    #path('info/', views.info, name='info'),
    #path('login/', views.login, name='login')

    url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^characterCreator/$', views.CharacterCreatorView.as_view(), name='characterCreator'),
    url(r'^battleSim/$', views.battleSimView.as_view(), name='battleSim'),
    url(r'^beginnersGuide/$', views.beginnersGuideView.as_view(), name='beginnersGuide'),
    url(r'^info/$', views.infoView.as_view(), name='info'),

]
