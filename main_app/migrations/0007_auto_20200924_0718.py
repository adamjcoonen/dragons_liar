# Generated by Django 3.0.8 on 2020-09-24 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20200924_0652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adventurer',
            options={'ordering': ['-lootnumber']},
        ),
        migrations.AlterField(
            model_name='adventurer',
            name='lootnumber',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]