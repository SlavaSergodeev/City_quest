from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^quest/(?P<quest_id>[0-9]+)/$', views.get_quest, name='quest'),
    url(r'^quest/(?P<quest_id>[0-9]+)/start/', views.start_quest, name='quest_start'),
    url(r'^quest/(?P<quest_id>[0-9]+)/finish/', views.finish_quest, name='quest_finish')

]
