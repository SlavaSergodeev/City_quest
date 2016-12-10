from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.base, name='home'),
    url(r'^our_team/$', views.our_team, name='ourteam'),
    url(r'^quest/(?P<quest_id>[0-9]+)/$', views.get_quest, name='quest'),
    url(r'^quest/(?P<quest_id>[0-9]+)/start/$', views.start_quest, name='quest_start'),
    url(r'^quest/(?P<quest_id>[0-9]+)/start/finish/$', views.finish_quest, name='quest_finish'),
    url(r'^quest/(?P<quest_id>[0-9]+)/start/check_quest/$', views.check_results_quest, name='check_quest')


]
