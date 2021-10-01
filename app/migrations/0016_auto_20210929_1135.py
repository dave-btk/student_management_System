# Generated by Django 3.2.7 on 2021-09-29 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacherapp', '0007_attendancereportstaff'),
        ('app', '0015_auto_20210929_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackstudent',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacherapp.staffs'),
        ),
        migrations.AlterField(
            model_name='feedbackstudent',
            name='user_type',
            field=models.TextField(max_length=30),
        ),
    ]
