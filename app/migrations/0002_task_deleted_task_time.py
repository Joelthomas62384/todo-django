# Generated by Django 5.0.6 on 2024-07-02 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='time',
            field=models.CharField(default='', max_length=50),
        ),
    ]
