# Generated by Django 2.2.17 on 2021-06-18 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='node',
            field=models.CharField(default='other', max_length=40),
        ),
    ]
