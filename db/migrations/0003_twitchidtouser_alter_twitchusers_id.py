# Generated by Django 4.1.7 on 2023-03-25 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0002_twitchusers"),
    ]

    operations = [
        migrations.CreateModel(
            name="TwitchIdToUser",
            fields=[
                ("twitch_id", models.IntegerField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name="twitchusers",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
