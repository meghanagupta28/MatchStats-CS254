# Generated by Django 4.2 on 2023-05-01 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="nationality",
            field=models.CharField(default="", max_length=64),
            preserve_default=False,
        ),
    ]
