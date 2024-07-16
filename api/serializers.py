from rest_framework import serializers
from student.models import Student
from teachers.models import Teachers
from classperiod.models import ClassPeriod
from course.models import Course
# from class.models import Class





class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class TeachersSerializer(serializers.modelSerializer):
    class Meta:
        model =  Teachers
        fields = "__all__"

class ClassPeriodSerializer(serializers.modelSerializer):
    class Meta:
        model = ClassPeriod
        fields = "__all__"

class CourseSerializer(serializers.modelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

# class ClassSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =Class
#         fields ="__all__"
