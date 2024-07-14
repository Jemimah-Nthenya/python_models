from django.db import models

# Create your models here.

class Teachers(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    year_of_birth=models.DateField()
    gender = models.CharField(max_length=15)
    email = models.EmailField()
    teacher_image = models.ImageField()
    phone_number = models.BigIntegerField()
    nationality = models.CharField(max_length=20)
    teacher_id = models.PositiveBigIntegerField()
    course = models.CharField(max_length=20)
    years_of_experience = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

