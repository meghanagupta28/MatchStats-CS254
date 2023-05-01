from django.db import models
from django.core.validators import MinValueValidator

class Stadium(models.Model):
    name = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=512)
    city = models.CharField(max_length=64)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=128, unique=True)
    code = models.CharField(max_length=3, unique=True)
    stadium = models.ForeignKey(Stadium, on_delete=models.SET_NULL, null=True, blank=True)
    goals_scored = models.PositiveSmallIntegerField()
    goals_conceded = models.PositiveSmallIntegerField()
    points = models.SmallIntegerField()

    def __str__(self):
        return self.name


class Player(models.Model):
    POSITION = [
        ('G',"Goalkeeper"),
        ('D',"Defender"),
        ('M',"Midfielder"),
        ('F',"Forward"),
    ]

    name = models.CharField(max_length=128)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete = models.SET_NULL)
    jersey_no = models.PositiveSmallIntegerField(null=True)
    dob = models.DateField()
    position = models.CharField(max_length=1, choices=POSITION)
    goals = models.PositiveSmallIntegerField(default=0)
    assists = models.PositiveSmallIntegerField(default=0)
    yellow_cards = models.PositiveSmallIntegerField(default=0)
    red_cards = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

class Match(models.Model):
    team_1 = models.ForeignKey(Team, null=True, related_name="team_1", on_delete=models.SET_NULL)
    team_2 = models.ForeignKey(Team, null=True, related_name="team_2", on_delete=models.SET_NULL)
    score_1 = models.PositiveSmallIntegerField(default=0)
    score_2 = models.PositiveSmallIntegerField(default=0)
    match_time = models.DateTimeField()
    completed = models.BooleanField(default=False)
    stadium = models.ForeignKey(Stadium, null=True, on_delete=models.SET_NULL)
    viewer_count = models.PositiveIntegerField(null=True, blank=True)

class Transfer(models.Model):
    team_from = models.ForeignKey(Team, null=True, related_name="team_from", blank=True, on_delete=models.SET_NULL)
    team_to = models.ForeignKey(Team, null=True, related_name="team_to", blank=True, on_delete=models.SET_NULL)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    transfer_date = models.DateField()

# class SupportStaff(models.Model):
#     STAFF_JOB_LIST = [
#         ('mgr', 'Manager'),
#         ('ch', 'Coach')
#     ]
#     staff_id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=30)
#     type = models.CharField(choices=STAFF_JOB_LIST, max_length=20)
#     team_id = models.ForeignKey(Teams, to_field='team_id', on_delete=models.CASCADE)

class Goal(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, null=True, on_delete = models.SET_NULL)
    scorer = models.ForeignKey(Player, null=True, related_name="goal_set", on_delete=models.SET_NULL)
    assist = models.ForeignKey(Player, null=True, related_name="assist_set",blank=True, on_delete=models.SET_NULL)
    match_time = models.DateTimeField()