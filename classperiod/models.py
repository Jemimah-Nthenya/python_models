from django.db import models

# Create your models here.
class ClassPeriod(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.CharField(max_length=30)
    classroom = models.CharField(max_length=30)
    day_of_week = models.CharField(max_length=7)
    duration = models.IntegerField()
    description = models.TextField()
    teacher = models.CharField()

    def _str_(self):
        return f"{self.course} - {self.day_of_week} to {self.end_time}"