# Generated by Django 2.1 on 2019-06-15 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_topic_classname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='level',
            old_name='name',
            new_name='lname',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='classname',
            new_name='lassname',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='name',
            new_name='tname',
        ),
    ]
