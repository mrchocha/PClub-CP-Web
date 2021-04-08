from django.shortcuts import render,HttpResponse, redirect
from django.http import JsonResponse
from .models import Questions, Users, Leaderboard, Timer
import requests
import time
import json
import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def Home(request):
    return render(request,'Home.html', {})

def Ques(request):
    current_time = datetime.datetime.now()
    if Timer.objects.exists():
        start_time = Timer.objects.all()[0].start_time_stamp
    else:
        start_time = current_time

    if current_time < start_time:
        return redirect('Home')    
    questions = Questions.objects.order_by('-uploadingTime')
    return render(request,'Questions.html', {'questions':questions})


def Leaderbord(request):
    
    questions = Questions.objects.all()
    
    leaders = Leaderboard.objects.order_by('-score')
    # print(leaders)
    return render(request,'Leaderbord.html', {'leaders':leaders, 'totalPros':len(questions)})

def AxYYzz786_rj(request):
    if not Timer.objects.exists():
        return JsonResponse({})
    
    end = Timer.objects.all()[0].end_time_stamp
    current = datetime.datetime.now()

    if(current>end):
        return JsonResponse({})
    
    lt = time.localtime()
    quedict = {}

    questions = Questions.objects.all()
    for question in questions:
        quedict[question.rcid()] = 1

    start = time.time()
    users = Users.objects.all()
    userlist = []
    for user in users:
        userlist.append(user.usr_name)

    data = {
        'response': userlist,
        'questionlist': quedict,
        'lastRefreshed': time.asctime(lt),
        'secondsTaken': time.time()-start
    }
    return JsonResponse(data)

@csrf_exempt
def AxYYzz786_rj_leaderboard_overcome_502(request):
    question_solved_by_user = json.loads(request.POST.getlist('question_solved_by_user')[0])
    for user in question_solved_by_user.keys():
        obj = Users.objects.filter(usr_name=user).update(solved_questions=question_solved_by_user[user])

    data=request.POST.getlist('score')
    user_handle = request.POST.getlist('handle')
    question_user_count = json.loads(request.POST.getlist('question_user_count')[0])
    print(question_user_count)
    j=0
    Leaderboard.objects.all().delete()
    for i in range(len(data)):
        l = Leaderboard(usr_name=user_handle[i], score=int(data[i]), profile_pic=Users.objects.get(usr_name=user_handle[i]).profile_pic)
        l.save()
    
    for key in question_user_count.keys():
        char = key[-1]
        num = ''
        last = ''
        if(char>='0' and char<='9'):
            num = key[:-2]
            last = key[-2:]
        else:
            num = key[:-1]
            last = key[-1]
        string = "https://codeforces.com/contest/"+num+"/problem/"+last
        ques = Questions.objects.get(Question_link=string)
        ques.totalCount = question_user_count[key]
        ques.save()
        # print(key)

    return JsonResponse({'user_handle':user_handle, 'user_score':data})

def Register(request):
    allow=1
    handle = request.GET.get('cf_id')
    mailid = request.GET.get('email')
    if (Users.objects.filter(usr_name=handle).exists()):
        allow=0
    else:
        u = Users(usr_name=handle, usr_mail=mailid)
        u.register()
        u.getPic()
        u.save()
    return JsonResponse({"response": allow})

def fetch_timer(request):
    if not Timer.objects.exists():
        return JsonResponse({})
    start = Timer.objects.all()[0].start_time_stamp
    end = Timer.objects.all()[0].end_time_stamp
    return JsonResponse({"start_ts": start.strftime("%b %d, %Y %H:%M:%S"), "end_ts": end.strftime("%b %d, %Y %H:%M:%S")})

def Question_User(request, id):
    usr_obj = Users.objects.get(usr_name=id)
    usr_fld = usr_obj.solved_questions.split(',')
    questions = Questions.objects.order_by('-uploadingTime')
    return render(request,'Questions.html', {'questions':questions, 'Question_solved_by_user':usr_fld})