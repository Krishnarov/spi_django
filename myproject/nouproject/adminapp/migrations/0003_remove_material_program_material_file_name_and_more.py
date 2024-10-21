# Generated by Django 4.2.4 on 2023-09-17 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_material'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='Program',
        ),
        migrations.AddField(
            model_name='material',
            name='file_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='material',
            name='my_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='material',
            name='subject',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='material',
            name='year',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='branch',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='material',
            name='program',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
