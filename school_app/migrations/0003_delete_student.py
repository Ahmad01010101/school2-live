# Generated by Django 4.0.4 on 2022-05-12 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0002_student_delete_d'),
    ]

    operations = [
        migrations.DeleteModel(
            name='student',
        ),
    ]