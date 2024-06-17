from django.db import models

# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=20)
    course_trainer = models.CharField(max_length=20)
    course_careers =models.SmallIntegerField()
    course_id= models.CharField(max_length=15)
    course_description = models.CharField(max_length=50)
    course_score = models.CharField(max_length=20)
    course_duration = models.PositiveBigIntegerField()
    course_sessions = models.CharField(max_length=20)
    course_students = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


