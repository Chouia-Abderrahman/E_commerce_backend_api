from django.db import models

# Create your models here.
class Player(models.Model):
    POSITION_CHOICES = [
        ('defender', 'Defender'),
        ('midfielder', 'Midfielder'),
        ('forward', 'Forward'),
    ]

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class PlayerSkill(models.Model):
    skill_choices = [
        ('defense', 'Defense'),
        ('attack', 'Attack'),
        ('speed', 'Speed'),
        ('strength', 'Strength'),
        ('stamina', 'Stamina'),
    ]
    skill = models.CharField(max_length=100)
    skill_level = models.IntegerField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='skills')

    def __str__(self):
        return self.name