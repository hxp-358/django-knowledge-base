# Generated by Django 2.0.6 on 2020-04-22 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_auto_20200422_1002'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DemoModel',
            new_name='Post',
        ),
    ]