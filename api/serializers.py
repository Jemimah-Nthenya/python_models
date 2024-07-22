from rest_framework import serializers
from.models import Students, Teachers, ClassPeriod, Course, classroom





class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
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

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model =classroom
        fields ="__all__"
