from django.shortcuts import render

# Create your views here.
from .models import Course
from .forms import CourseForm


def courses_list(request):
    courses=Course.objects.order_by("-created_at")
    form=CourseForm()
    return render(request, 'courses/courses_list.html', {"courses":courses, "form":form})
    # s='Список кник\r\n\r\n\r\n'
    # for b in Book.objects.order_by('-published'):
    #     s+=b.name+'\r\n'+ b.description+'\r\n\r\n'
    # return HttpResponse(s, content_type='text/plain; charset=utf-8')

