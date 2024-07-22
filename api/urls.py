from django.urls import path
from .views import StudentListView
from .views import TeachersListView
from .views import ClassPeriodListView
from .views import CourseListView
from .views import StudentDetailView
from .views import CoursesDetailView
from .views import ClassPeriodDetailView
from .views import ClassRoomDetailView


urlpatterns=[
    path("students/",StudentListView.as_view(),name="student_list_view"),
    path("teachers/",TeachersListView.as_view(),name="teachers_list_view"),
    path("course/",CourseListView.as_view(),name="course_list_view"),
    path("classperiod/",ClassPeriodListView.as_view(),name="classperiod_list_view"),
    path("students/<int:id>", StudentDetailView.as_view(), name="student_Detail_views"),
    path("courses/<int:id>", CoursesDetailView.as_view(), name="Course_Detail_view"),
    path("class/<int:id>", ClassPeriodDetailView.as_view(), name="classPeriod_Details_views"),
    path("classroom/<int:id>", ClassRoomDetailView.as_view(), name="classroom_details_views")
]

