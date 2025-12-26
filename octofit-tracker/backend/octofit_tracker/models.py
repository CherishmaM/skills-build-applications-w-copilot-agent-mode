from djongo import models

class Team(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    class Meta:
        db_table = 'teams'
    def __str__(self):
        return self.name

class User(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, to_field='id')
    class Meta:
        db_table = 'users'
    def __str__(self):
        return self.email

class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id')
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # minutes
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'activities'

class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested_for = models.ManyToManyField(User, blank=True)
    class Meta:
        db_table = 'workouts'

class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, to_field='id')
    points = models.IntegerField(default=0)
    class Meta:
        db_table = 'leaderboard'
