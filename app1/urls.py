"""MyPclub2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home,name='Home'),
    path('Questions', views.Ques,name='Questions'),
    path('Leaderbord', views.Leaderbord,name='Leaderbord'),
    path('Register', views.Register,name='Register'),
    path('AxYYzz786_rj', views.getUserList,name='AxYYzz786_rj'),
    path('AxYYzz786_rj_leaderboard_overcome_502', views.updateLeaderboard, name='AxYYzz786_rj_leaderboard_overcome_502'),
    path('fetch_timer', views.fetch_timer, name="fetch_timer"),
    path('Questions/<slug:id>', views.Question_User,name='Questions')
]
