from django.urls import path 
from .views import CoursesCreateView, CoursesListView, CoursesDetailView, LanguageListView


urlpatterns=[
  
    path('', CoursesListView.as_view(), name='home'),
    path('create/', CoursesCreateView.as_view(), name="courses_create"),
    path('courses/', CoursesListView.as_view(), name="courses_list"),
    path('courses/<int:pk>/', CoursesDetailView.as_view(), name="courses_detail"),
    path('language/',  LanguageListView.as_view(), name="language"),

]