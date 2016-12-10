from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from  django import forms
from django.contrib import auth

from quest.models import Quest, Photo

import re
import json



class CheckQuestResultForm(forms.Form):
    result = forms.CharField(label='Результат', max_length=50)


def check_results_quest(request, quest_id):
    quest_obj = get_object_or_404(Quest, id=quest_id)
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        if quest_obj.check == post_text:
            return JsonResponse({'result': 'finish'}
                                )
        else:
            return HttpResponse(
                json.dumps({"nothing to see": "this isn't happening"}),
                content_type="application/json")
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json")


def base(request):
    """

    :param request:
    :return:
    """
    quests = Quest.objects.all()
    photos = Photo.objects.all()
    context = {
        'quests': quests,
        'photos': photos,
        'username': auth.get_user(request).username
    }
    return render(request, 'quest/about.html', context)


def finish_quest(request, quest_id):
    quest_obj = get_object_or_404(Quest, id=quest_id)
    quests = Quest.objects.all()

    context = {
        'quest': quest_obj,
        'quests': quests,
        'username': auth.get_user(request).username
    }
    return render(request, 'quest/questfinish.html', context)


def our_team(request):
    quests = Quest.objects.all()
    context = {
        'quests': quests,
        'username': auth.get_user(request).username
    }
    return render(request, 'quest/team.html', context)


def start_quest(request, quest_id):
    print('вапраопавыэ')
    quest_obj = get_object_or_404(Quest, id=quest_id)
    quest_obj_task = re.split(r'[0-9]+\)', quest_obj.task)
    quest_obj_task = quest_obj_task[1:]
    quests = Quest.objects.all()
    form = CheckQuestResultForm()
    context = {
        'quest': quest_obj,
        'quest_task': quest_obj_task,
        'quests': quests,
        'form': form,
        'username': auth.get_user(request).username
    }
    return render(request, 'quest/queststart.html', context)


def get_quest(request, quest_id):
    ques_obj = get_object_or_404(Quest, id=quest_id)
    quests = Quest.objects.all()
    context = {
        'quests': quests,
        'quest': ques_obj,
        'username': auth.get_user(request).username

    }
    return render(request, 'quest/quest.html', context)
