from django import forms#хранение форм
from courses.models import Course 

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course#какую форму вывести 
        fields="__all__"#какие поля от формы