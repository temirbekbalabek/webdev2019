# Generated by Django 2.2 on 2019-04-21 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_tasklist_created_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasklist',
            options={'verbose_name': 'TaskList', 'verbose_name_plural': 'TaskLists'},
        ),
    ]
