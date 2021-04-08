from django.contrib import admin

# Register your models here.
from app1.models import Users, Leaderboard, Questions, Timer

admin.site.register(Users)
admin.site.register(Leaderboard)
admin.site.register(Questions)
admin.site.register(Timer)