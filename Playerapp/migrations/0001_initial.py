# Generated by Django 2.1.1 on 2018-09-01 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PlayerName', models.CharField(blank=True, max_length=100, null=True)),
                ('Born', models.DateField()),
                ('Birthplace', models.CharField(blank=True, max_length=100, null=True)),
                ('Height', models.FloatField()),
                ('City', models.CharField(blank=True, max_length=100, null=True)),
                ('BattingStyle', models.CharField(blank=True, max_length=100, null=True)),
                ('BowlingStyle', models.CharField(blank=True, max_length=100, null=True)),
                ('Awards', models.CharField(blank=True, max_length=100, null=True)),
                ('Country', models.CharField(blank=True, choices=[('India', 'India'), ('Englnd', 'England'), ('Srilanka', 'Srilanka'), ('Austalia', 'Austalia'), ('NewsLand', 'Newsland'), ('South Africa', 'South Africa'), ('Bangladesh', 'Bangladesh')], max_length=100, null=True)),
                ('Role', models.CharField(blank=True, choices=[('Batsman', 'Batsman'), ('Bowler', 'Bowler'), ('All-rounder', 'All-rounder')], max_length=100, null=True)),
            ],
        ),
    ]