# PClub-CP-Web

<p  align="center" >
<img src="https://github.com/mrchocha/PClub-CP-Web/blob/master/snapshots/Black_T.png" height="250">
  <h1 align="center" >Programming Club</h1>
</p>

A full fledged working website made using django framework aimed at able to show list of Practice Questions for enhancing Competitive Coding skills and rank the 
registered users based on the number of Questions solved by them. Specific ranks are not given, so that it encourages students to not secure good rank but allowing them to focus more on the question solving part.

# Technologies-Used
* Django [V3.0](https://www.djangoproject.com/download/)
* Python [V3.8](https://www.python.org/downloads/)
* JavaScript
* BootStrap [V4.5](https://getbootstrap.com/)
* Cron [ Software utility in UNIX-like computer operating systems which sets up a cron job ]

# Workflow
* Get yourself registered and only <b>#AhmedabadUniversity</b> Students are allowed to register.
<br>

<p  align="center" >
<img src="https://github.com/mrchocha/PClub-CP-Web/blob/master/snapshots/home.png" height="270">
</p>
<br>

* Solve handpicked <b>#Codeforces</b> questions by our brilliant committee members.
<br>

<p  align="center" >
<img src="https://github.com/mrchocha/PClub-CP-Web/blob/master/snapshots/questions.png" height="270">
</p>
<br>

* See your name on the leaderboard and keep track of the number of questions solved.
<br>

<p  align="center" >
<img src="https://github.com/mrchocha/PClub-CP-Web/blob/master/snapshots/leaderboard.png" height="270">
</p>


# Challenges Faced

* As we were supposed to deploy this whole django project, and lederboard needs to be refreshed every 10 minutes which was not possible to do it because of long response time of the leaderboard update algorithm (because it checks all submissions of all the users and then count the accepted verdicts in all the submissions and all this takes place for more than 90 users).

## Solution

We have brought whole time consuming process of leaderboard updation to our local system and then updating the django backend which in turn reflect changes on to the website.

### Cron Job

* Cron job is a time-based job scheduler in Unix-like computer operating systems.

* Below are the steps to setup cron job.
   * First write below to open system file (edit this file to introduce tasks to be run by cron) in nano editor
    ```
    crontab -e
    ```
   * Then, add below line to run it periodically (runs every 10 minutes)
   ```
     */10 * * * * python /path/to/cron/job/file/fetch_user.py >> /path/to/log/file/logfile.log
   ```
   
### Mechanism behind Leaderboard updation [Cron job]
<p  align="center" >
<img src="https://github.com/mrchocha/PClub-CP-Web/blob/master/snapshots/Mechanism_Cron_Job.png">
  <h2 align="center" >Refer "fetch_user.py"</h2>
</p>
<br>

* Whole above shown process takes place on the local system [ through running fetch_user.py file ] and the cron job is set which repeats the process.

