# Generated by Django 3.1.4 on 2021-06-15 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0007_stuuser_roll'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submit_Ass',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('roll', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('document', models.FileField(upload_to='media/')),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
