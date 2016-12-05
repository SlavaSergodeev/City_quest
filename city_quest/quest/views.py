import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from  django import forms

from quest.models import Quest, Photo
import re

class CheckQuestResultForm(forms.Form):
    result = forms.CharField(label='Результат', max_length=50)



def create_post(request, quest_id):
    quests=Quest.objects.all()
    quest_obj = get_object_or_404(Quest, id=quest_id)
    print('fdsghjkhgdfsgjkhgfdsgdhfg', quest_obj)
    # return render(request, 'quest/questfinish.html', {'quest': quest_obj, 'quests': quests})

    if request.method == 'POST':

        print('dfdddddddddd')
        post_text = request.POST.get('the_post')
        response_data = {}
        print(post_text)
        print(quest_obj.check)
        # form = CheckQuestResultForm(request.POST)
        if quest_obj.check == post_text:
            # return render(request, 'quest/questfinish.html', {'quest': quest_obj, 'quests': quests})
            print('вапр')
            # post = request.POST(text=post_text)
            # #
            # print('dddddddddddddd',post.pk)

            response_data['result'] = 'finish'
            # response_data['postpk'] = post.pk
            # response_data['text'] = post.text
            # response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
            # response_data['author'] = post.author.username

            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
        else:
            return HttpResponse(
                json.dumps({"nothing to see": "this isn't happening"}),
                content_type="application/json")
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json")


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
    print('вапраопавыэ')
    quest_obj = get_object_or_404(Quest, id=quest_id)
    quest_obj_task = re.split(r'[0-9]+\)', quest_obj.task)
    quest_obj_task = quest_obj_task[1:]
    quests = Quest.objects.all()
    form = CheckQuestResultForm()
    #
    # if request.method == 'POST':
    #     form = CheckQuestResultForm(request.POST)
    #     if form.is_valid() and quest_obj.check == form.cleaned_data['result']:
    #         return render(request, 'quest/questfinish.html', {'quest': quest_obj, 'quests': quests})
    # else:
    #
    #     form = CheckQuestResultForm()

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
