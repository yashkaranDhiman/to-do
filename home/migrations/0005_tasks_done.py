# Generated by Django 4.2.4 on 2023-10-14 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_tasks_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
