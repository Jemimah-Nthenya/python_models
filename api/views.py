from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from student.models import Student
from teachers.models import Teachers
from classperiod.models import ClassPeriod
from course.models import Course
from .serializer import Student
from .serializer import Teachers
from .serializer import ClassPeriod
from .serializer import Course

class StudentListView(APIView):
    def get(self, request, format=None):
        Student = Student.object.all()
        serializer = StudentSerializer(Student, many=True)
    
class TeachersListView(APIView):
    def get(self, request, format=None):
        Teachers = Teachers.object.all()
        serializer = TeachersSerializer(Teachers, one=True)
        return Response(serializer.data)

class ClassPeriodListView(APIView):
    def get(self, request, format=None):
        ClassPeriod = ClassPeriod.cbject.all()
        serializer = ClassPeriodSerializer(ClassPeriod, many=True)
        return Response(serializer.data)
    
class CourseListView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)



