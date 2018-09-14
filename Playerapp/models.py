from django.db import models
from django.urls import reverse
class Player(models.Model):
    PlayerName = models.CharField(max_length=100, blank=True, null=True)
    Born = models.DateField()
    Birthplace = models.CharField(max_length=100, blank=True, null=True)
    Height = models.FloatField()
    City=models.CharField(max_length=100,blank=True,null=True)
    BattingStyle = models.CharField(max_length=100, blank=True, null=True)
    BowlingStyle = models.CharField(max_length=100, blank=True, null=True)
    Awards = models.CharField(max_length=100, blank=True, null=True)
    Teams = (
        ('India', 'India'),
        ('Englnd', 'England'),
        ('Srilanka', 'Srilanka'),
        ('Austalia', 'Austalia'),
        ('NewsLand', 'Newsland'),
        ('South Africa', 'South Africa'),
        ('Bangladesh', 'Bangladesh')

    )

    ownrole = (
        ('Batsman', 'Batsman'),
        ('Bowler', 'Bowler'),
        ('All-rounder', 'All-rounder')

    )
    Country = models.CharField(max_length=100, blank=True, null=True, choices=Teams)
    Role = models.CharField(max_length=100, blank=True, null=True, choices=ownrole)


    def __str__(self):
        return self.PlayerName
    def get_absolute_url(self):
        return reverse('Playerapp:detail',kwargs={'pk':self.pk})



