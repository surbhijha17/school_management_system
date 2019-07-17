# Generated by Django 2.1 on 2019-06-15 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='media/assignment')),
                ('duedate', models.DateField(auto_now_add=True)),
                ('class_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.ClassInfo')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher')),
            ],
        ),
    ]
