# Generated by Django 4.2.4 on 2023-09-05 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nouapp', '0002_alter_student_contacton'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='yean',
            new_name='year',
        ),
    ]
