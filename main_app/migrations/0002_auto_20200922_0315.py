# Generated by Django 3.0.8 on 2020-09-22 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dragon',
            name='age',
            field=models.CharField(choices=[('H', 'Wyrmling'), ('v', 'Very Young'), ('y', 'Young'), ('J', 'Juvenile'), ('Y', 'Young Adult'), ('A', 'Adult'), ('O', 'Old'), ('V', 'Very Old'), ('A', 'Ancient'), ('W', 'Wyrm'), ('G', 'Great Wyrm')], default=0, max_length=1),
        ),
        migrations.AddField(
            model_name='dragon',
            name='d_type',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dragon',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dragon',
            name='subtype',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
