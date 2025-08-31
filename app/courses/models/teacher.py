from django.db import models
from django.core.validators import EmailValidator
from .courses import Course

class Teacher(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    middle_name = models.CharField('Отчество', max_length=50, blank=True, null=True)
    email = models.EmailField('Email', unique=True, validators=[EmailValidator(message='Введите корректный email адрес')])



    course=models.ManyToManyField(Course, verbose_name='Курсы', related_name='courses')

    class Meta:
        verbose_name='Преподаватель'
        verbose_name_plural='Преподаватели'
        #ordering=['']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
