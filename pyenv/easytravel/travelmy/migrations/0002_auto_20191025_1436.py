# Generated by Django 2.2.6 on 2019-10-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelmy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='offer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
