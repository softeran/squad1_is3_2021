# Generated by Django 3.2.4 on 2021-07-02 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeTra', '0009_remove_task_time_spent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='starting_date',
            field=models.BigIntegerField(),
        ),
    ]
