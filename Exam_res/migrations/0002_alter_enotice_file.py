# Generated by Django 4.1.2 on 2022-12-22 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exam_res', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enotice',
            name='File',
            field=models.FileField(upload_to='media'),
        ),
    ]
