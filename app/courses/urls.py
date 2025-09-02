from django.urls import path 
from .views import CoursesCreateView, CoursesListView


urlpatterns=[
  
    path('', CoursesListView.as_view(), name='home'),  # корневой URL
    path('create/', CoursesCreateView.as_view(), name="courses_create"),
    path('courses/', CoursesListView.as_view(), name="courses_list"),

]