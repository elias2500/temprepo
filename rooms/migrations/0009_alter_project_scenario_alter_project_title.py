# Generated by Django 4.1 on 2023-06-08 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0008_alter_project_scenario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='scenario',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]