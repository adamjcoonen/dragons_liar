# Generated by Django 3.0.8 on 2020-09-24 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200922_0315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Adventurers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adventurer_type', models.CharField(choices=[('F', 'Fighter'), ('W', 'Wizard'), ('M', 'Monk'), ('R', 'Ranger'), ('B', 'Barbarian'), ('T', 'Thief'), ('C', 'Cleric')], default='F', max_length=1)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Dragon')),
            ],
        ),
    ]