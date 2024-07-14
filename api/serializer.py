from rest_framework import serializers
from student.models import Student
from teachers.models import Teachers
from classperiod.models import ClassPeriod




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
