import os
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    print('This job is run every three minutes.')
    os.system('python3 /home/rahul/Public/Work/django/mypc/MyPclub2/cronfile.py')


sched.start()