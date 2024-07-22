from django.db import models

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=20)
    data_of_birth = models.DateField()
    code = models.PositiveBigIntegerField()
    student_image = models.ImageField()
    enrollment_year = models.IntegerField()
    course = models.SmallIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
