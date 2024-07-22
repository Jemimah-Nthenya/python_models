from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from student.models import Students
from .serializers import StudentSerializer
from teachers.models import Teachers
from .serializers import TeachersSerializer
from classroom.models import Class 
from .serializers import ClassroomSerializer
from classperiod.models import ClassPeriod
from .serializers import ClassPeriodSerializer
from course.models import Course
from .serializers import CourseSerializer



class StudentListView(APIView):
    def get(self, request):
        Students = Students.object.all()
        serializer = StudentSerializer(Students, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
   
class StudentDetailView(APIView):
    def get(self, request,id):
        Student= Student.objects.get(id=id)
        serializer=StudentSerializer(Student)
        return Response(serializer.data)
    
    student =Students.objects.get(id=id)
    def put(self, request, id):
        serializer= StudentSerializer(Students, data=request.data)
        if serializer():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        student = Students.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


        

class TeachersListView(APIView):

    def get(self, request):
        Teachers = Teachers.object.all()
        serializer = TeachersSerializer(Teachers, one=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TeachersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
class TeachersDetailView(APIView):
    def get(self, request,id):
        teachers= Teachers.objects.get(id=id)
        serializer=TeachersSerializer(teachers)
        return Response(serializer.data)
    
    teachers =Teachers.objects.get(id=id)
    def put(self, request, id):
        serializer= StudentSerializer(Teachers, data=request.data)
        if serializer():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        teachers = Teachers.objects.get(id=id)
        teachers.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
        

class ClassPeriodListView(APIView):
    def get(self, request):
        ClassPeriods = ClassPeriod.cbject.all()
        serializer = ClassPeriodSerializer(ClassPeriods, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
class ClassPeriodDetailView(APIView):
    def get(self, request,id):
        classPeriod= ClassPeriod.objects.get(id=id)
        serializer=ClassPeriodSerializer(ClassPeriod)
        return Response(serializer.data)
    
    ClassPeriod =ClassPeriod.objects.get(id=id)
    def put(self, request, id):
        serializer= ClassPeriodSerializer(ClassPeriod, data=request.data)
        if serializer():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        ClassPeriod = ClassPeriod.objects.get(id=id)
        ClassPeriod.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
        

class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)  
        
class CoursesDetailView(APIView):
    def get(self, request,id):
        course= Course.objects.get(id=id)
        serializer=CourseSerializer(ClassPeriod)
        return Response(serializer.data)
    
    Course =Course.objects.get(id=id)
    def put(self, request, id):
        serializer= CourseSerializer(Course, data=request.data)
        if serializer():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        Course = Course.objects.get(id=id)
        Course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
        


    
class ClassRoomListView(APIView):
    def get(self, request):
        classroom = Class.object.all()
        serializer = ClassroomSerializer(classroom,many=True)


    def post(self, request):
        serializer = ClassroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)  
        
class ClassRoomDetailView(APIView):
    def get(self, request,id):
        classroom= Class.objects.get(id=id)
        serializer=ClassroomSerializer(classroom)
        return Response(serializer.data)
    
    classroom =Class.objects.get(id=id)
    def put(self, request, id):
        serializer= ClassroomSerializer(Class, data=request.data)
        if serializer():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        classroom = Class.objects.get(id=id)
        Class.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
        



