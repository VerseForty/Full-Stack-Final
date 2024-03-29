# Generated by Django 2.2.7 on 2019-11-20 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='characterTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=32)),
                ('playerName', models.CharField(max_length=32)),
                ('race', models.CharField(max_length=32)),
                ('playerClass', models.CharField(max_length=32)),
                ('strength', models.CharField(max_length=2)),
                ('dexterity', models.CharField(max_length=2)),
                ('constitution', models.CharField(max_length=2)),
                ('intelligence', models.CharField(max_length=2)),
                ('wisdom', models.CharField(max_length=2)),
                ('charisma', models.CharField(max_length=2)),
            ],
        ),
    ]
