from django.urls import path
from .views import StudentListView
from .views import TeachersListView
from .views import ClassPeriodListView
from .views import CourseListView

urlpatterns=[
    path("students/",StudentListView.as_view(),name="student_list_view"),
    path("teachers/",TeachersListView.as_view(),name="teachers_list_view"),
    path("course/",CourseListView.as_view(),name="course_list_view"),
    path("classperiod/",ClassPeriodListView.as_view(),name="classperiod_list_view"),
    # path("class/",classListView.as_view(),name="class_list_view")
]

