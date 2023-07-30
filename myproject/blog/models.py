from django.db import models
import os

FEELING_LIST = [
    ('Bad', 'Bad'),
    ('Good', 'Good'),
    ('Stress', 'Stress'),
    ('Angry', 'Angry'),
    ('Happy', 'Happy')
]
def upload_location(instance, filename):
    return f'{instance.id}, {filename}'
class DailyPlan(models.Model):
    plan_name = models.CharField(max_length=100)
    plan_description = models.TextField()
    plan_date = models.DateField()
    plan_time = models.TimeField()
    completed = models.BooleanField(default=False)

# Create your models here.
class Blog_Post(models.Model):
    post_name = models.CharField (max_length=50)
    post_description = models.TextField()
    post_date = models.DateField()
    post_time = models.TimeField()
    Feeling = models.CharField(max_length=100, choices=FEELING_LIST, default='Choice')
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return self.post_name