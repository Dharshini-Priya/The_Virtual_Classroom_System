# Generated by Django 3.1.4 on 2021-06-15 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0010_auto_20210615_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submit_ass',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]
