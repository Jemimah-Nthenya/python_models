from django.db import models

# Create your models here.

class Class(models.Model):
    class_name = models.CharField(max_length=20)
    class_teacher = models.CharField(max_length=20)
    class_size =models.SmallIntegerField()
    class_rep = models.CharField(max_length=15)
    class_enrollment = models.SmallIntegerField()
    class_vision = models.CharField(max_length=20)
    class_goal = models.CharField(max_length=50)
    class_equipment= models.CharField(max_length=20)
    class_lesson = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

