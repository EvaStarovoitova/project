
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from .models.courses import Course, Language
from django.contrib import messages




class CoursesList(ListView):
    model=Course

class CoursesCreateView(CreateView):
    model = Course
    fields = ['title', 'what_you_will_learn', 'price']
    template_name = "courses/courses_create.html" 
    success_url = reverse_lazy("courses_list")

   
    def get_success_url(self):
       messages.success(self.request, "Создано успешно!")#не рабоет
       return super().get_success_url()


class CoursesListView(ListView):
    model = Course
    template_name = "courses/courses_list.html"
    context_object_name = "courses"


class CoursesDetailView(DetailView):
    model = Course
    template_name = "courses/courses_detail.html"
    context_object_name = "course"

class LanguageList(ListView):
    model=Language

class LanguageListView(ListView):
    model = Language
    template_name = 'courses/language.html'
    context_object_name = 'languages'
    
    def get_queryset(self):
        return Language.objects.filter(is_active=True).order_by('name')
