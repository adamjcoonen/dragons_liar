# Generated by Django 3.0.8 on 2020-09-24 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200924_0611'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adventurer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lootnumber', models.PositiveSmallIntegerField(default=5)),
                ('adventurer_type', models.CharField(choices=[('F', 'Fighter'), ('W', 'Wizard'), ('M', 'Monk'), ('R', 'Ranger'), ('B', 'Barbarian'), ('T', 'Thief'), ('C', 'Cleric')], default='F', max_length=1)),
                ('dragon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Dragon')),
            ],
        ),
        migrations.DeleteModel(
            name='Adventurers',
        ),
    ]