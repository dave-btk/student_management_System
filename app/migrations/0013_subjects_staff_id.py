# Generated by Django 3.2.7 on 2021-09-27 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacherapp', '0005_alter_staffs_role'),
        ('app', '0012_feedbackstudent_leavereportstudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='staff_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='teacherapp.staffs'),
        ),
    ]
