# Generated by Django 4.1.1 on 2023-02-03 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_remove_project_number_of_riddles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='scenario',
            field=models.TextField(blank=True),
        ),
    ]
