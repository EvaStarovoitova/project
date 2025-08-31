from django.db import models
from django.core.validators import EmailValidator

from datetime import date



class Student(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    middle_name = models.CharField('Отчество', max_length=50, blank=True, null=True)
    email = models.EmailField('Email', unique=True, validators=[EmailValidator(message='Введите корректный email адрес')])
    birth_date = models.DateField('Дата рождения')


    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['last_name']

    def age(self):
        today=date.today()
        age=today.year-self.birth_date.year-(today.month, today.day)<(self.birth_date.month, self.birth_date.day)
        return age
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} "
