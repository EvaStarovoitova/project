from django.db import models
from django.conf import settings  

class Level(models.Model):
    name = models.CharField('Название уровня', max_length=50, unique=True)
    code = models.CharField('Код уровня', max_length=10, unique=True, help_text='Например: A1, B2, C1')
    description = models.TextField('Описание уровня', help_text='Что студент должен уметь на этом уровне')
    order = models.PositiveIntegerField('Порядок', default=0, help_text='Порядок отображения (от меньшего к большему)')
    is_active = models.BooleanField('Активный', default=True)

    class Meta:
        verbose_name = 'Уровень владения языком'
        verbose_name_plural = 'Уровни владения языком'
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.code})"
