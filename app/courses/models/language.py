from django.db import models
from django.conf import settings  

class Language(models.Model):
    name = models.CharField('Название языка', max_length=50, unique=True)
    code = models.CharField('Код языка', max_length=10, unique=True)
    description = models.TextField('Описание языка', blank=True)

    is_active = models.BooleanField( 'Активный', default=True)

   
    flag_icon = models.CharField('Иконка флага', max_length=50, blank=True)

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'
        ordering = ['name']
        indexes = [
            models.Index(fields=['is_active']),
           
        ]

    def __str__(self):
        return self.name

    def get_total_courses(self):
        return self.courses.count()

    def get_total_students(self):
        from django.db.models import Sum
        return self.courses.aggregate(total_students=Sum('total_students'))['total_students'] or 0


