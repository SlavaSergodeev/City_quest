from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.serializers import json
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from  django import forms
from django.views.generic import FormView

from quest.models import Quest, Photo
import re

class CheckQuestResultForm(forms.Form):
    result = forms.CharField(label='Результат', max_length=50)



def view_for_form(request):
    pass

def home(request):
    """

    :param request:
    :return:
    """
    quests = Quest.objects.all()
    photos = Photo.objects.all()
    context = {
        'quests': quests,
        'photos': photos
    }
    return render(request, 'quest/about.html', context)


def finish_quest(request, quest_id):
    quest_obj = get_object_or_404(Quest, id=quest_id)
    quests = Quest.objects.all()

    context = {
        'quest': quest_obj,
        'quests': quests
    }
    return render(request, 'quest/questfinish.html', context)


def start_quest(request, quest_id):
    quest_obj = get_object_or_404(Quest, id=quest_id)
    quest_obj_task = re.split(r'[0-9]+\)', quest_obj.task)
    quest_obj_task = quest_obj_task[1:]
    quests = Quest.objects.all()

    if request.method == 'POST':
        form = CheckQuestResultForm(request.POST)
        if form.is_valid() and quest_obj.check == form.cleaned_data['result']:
            return render(request, 'quest/questfinish.html', {'quest': quest_obj, 'quests': quests})
    else:

        form = CheckQuestResultForm()

    context = {
        'quest': quest_obj,
        'quest_task': quest_obj_task,
        'quests': quests,
        'form': form
    }
    return render(request, 'quest/queststart.html', context)


def get_quest(request, quest_id):
    ques_obj = get_object_or_404(Quest, id=quest_id)
    quests = Quest.objects.all()
    context = {
        'quests': quests,
        'quest': ques_obj

    }
    return render(request, 'quest/quest.html', context)
