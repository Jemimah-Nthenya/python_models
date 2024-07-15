from rest_framework import serializers
from student.models import Student
from teachers.models import Teachers
from classperiod.models import ClassPeriod
from course.models import Course





class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class TeachersSerializer(serializers.modelsSerializer):
    class Meta:
        model =  Teachers
        fields = "__all__"

class ClassPeriodSerializer(serializers.modelsSerializer):
    class Meta:
        model = ClassPeriod
        fields = "__all__"

class CourseSerializer(serializers.modelsSerializer):
    class Meta:
        model = Course
        fields = "__all__"
