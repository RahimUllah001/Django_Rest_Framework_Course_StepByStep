# Generated by Django 5.1.7 on 2025-03-13 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('roll', models.IntegerField()),
                ('city', models.CharField(max_length=70)),
            ],
        ),
    ]
