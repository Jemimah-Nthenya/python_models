from django.db import models

# Create your models here.

class Class(models.Model):
    class_name = models.CharField(max_length=20)
    class_teacher = models.CharField(max_length=20)
    class_size =models.SmallIntegerField()
    class_laptop = models.CharField(max_length=15)
    class_television = models.SmallIntegerField()
    class_window = models.SmallIntegerField()
    class_goal = models.CharField(max_length=50)
    class_lesson = models.PositiveBigIntegerField()
    

    def __str__(self):
        return f"{self.class_name} {self.class_teacher}"

