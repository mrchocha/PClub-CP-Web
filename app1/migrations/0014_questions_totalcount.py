# Generated by Django 3.1 on 2021-03-30 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_questions_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='totalCount',
            field=models.IntegerField(default=0),
        ),
    ]