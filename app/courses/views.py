
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
# Create your views here.
from .models.courses import Course
from django.contrib import messages



#def courses_list(request):
#    courses=Course.objects.order_by("-created_at")
#    form=CourseForm()
#    return render(request, 'courses/courses_list.html', {"courses":courses, "form":form})
   

# class BookDetails(DetailView):
#   model = Book
    #template_name="books/book_details.html"
    #context_object_name="book"



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

#class CoursesCreateView(FormView):
#    template_name = "courses/courses_create.html"
#    form_class = CoursesForm  
#    success_url = reverse_lazy("courses_list")
#    
#    def form_valid(self, form):
#      
#        form.save()
#        return super().form_valid(form)

# class BookList(ListView):
# model = Book
 #template_name="books/book_list.html"
 #context_object_name="books"

 #по умолчанию template_name="название приложения/название модели_название view.html "
 # поумолчанию context_object_name="object_название view (list)"



