# Generated by Django 2.1 on 2019-06-15 18:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='date',
            field=models.DateField(default=datetime.date(2019, 6, 16)),
        ),
        migrations.AlterField(
            model_name='topic',
            name='examname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Subject'),
        ),
        migrations.DeleteModel(
            name='Examname',
        ),
    ]
