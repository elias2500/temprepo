# Generated by Django 4.1.1 on 2023-02-02 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_alter_project_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='number_of_riddles',
        ),
    ]
