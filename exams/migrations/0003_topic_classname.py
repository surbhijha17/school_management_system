# Generated by Django 2.1 on 2019-06-15 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
        ('exams', '0002_auto_20190616_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='classname',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='classes.ClassInfo'),
            preserve_default=False,
        ),
    ]
