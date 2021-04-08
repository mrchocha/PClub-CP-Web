from django.db import models
from django.utils import timezone
import requests
from datetime import datetime

# Create your models here.
class Questions(models.Model):
    Question_name = models.TextField(max_length=1000)
    Question_link = models.TextField(max_length=10000)
    tags = models.TextField(max_length=100000, default="")
    totalCount = models.IntegerField(default=0)
    uploadingTime = models.DateTimeField('Question Uploading Time', default=datetime.now)

    def rcid(self):
        link = self.Question_link
        link = str(link).split('/')
        return link[len(link)-3]+link[len(link)-1]
    
    def totalUsers(self):
        peeps = len(Users.objects.all())
        return peeps
    
class Users(models.Model):
    usr_name = models.TextField(max_length=500, primary_key=True)
    usr_mail = models.EmailField(max_length=1000)
    regTime = models.DateTimeField('Registered Time')
    profile_pic = models.TextField(max_length=10000, default="")
    solved_questions = models.TextField(max_length=100000, default="")
    
    def register(self):
        self.regTime = timezone.now()
        self.save()
    
    def getPic(self):
        handle = self.usr_name
        response = requests.get("https://codeforces.com/api/user.info?handles="+handle)
        stat = response.json()["result"]
        self.profile_pic = stat[0]["titlePhoto"]
        self.save()

class Leaderboard(models.Model):
    usr_name = models.TextField(max_length=500)
    score = models.IntegerField(default=0)
    profile_pic = models.TextField(max_length=10000, default="")

class Timer(models.Model):
    start_time_stamp = models.DateTimeField()
    end_time_stamp = models.DateTimeField()