from rest_framework.views import APIView
from rest_framework.response import Response
from student.models import Student
from .serializers import StudentSerializer
from teachers.models import Teachers
from .serializers import TeachersSerializer
# from class.models import Class 
# from .serializers import ClassSerializer
from classperiod.models import ClassPeriod
from .serializers import ClassPeriodSerializer
from course.models import Course
from .serializers import CourseSerializer


class StudentListView(APIView):
    def get(self, request):
        Students = Student.object.all()
        serializer = StudentSerializer(Students, many=True)
        return Response(serializer.data)
    
class TeachersListView(APIView):
    def get(self, request):
        Teachers = Teachers.object.all()
        serializer = TeachersSerializer(Teachers, one=True)
        return Response(serializer.data)

class ClassPeriodListView(APIView):
    def get(self, request):
        ClassPeriods = ClassPeriod.cbject.all()
        serializer = ClassPeriodSerializer(ClassPeriods, many=True)
        return Response(serializer.data)
    
class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
# class ClassListView(APIView):
#     def get(self, request):
#         classes = class.object.all()
#         serializer = classSerializer(classes,many=True)


