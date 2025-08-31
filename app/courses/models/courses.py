from django.db import models
from django.conf import settings  
from django.core.validators import MinValueValidator
from .level import Level
from .student import Student

from .language import Language



class Course(models.Model):
    # Статусы курсов
    DRAFT = 'draft'
    PUBLISHED = 'published'
    ARCHIVED = 'archived'

    STATUS_CHOICES = [
        (DRAFT, 'Черновик'),
        (PUBLISHED, 'Опубликован'),
        (ARCHIVED, 'В архиве'),
    ]

    title = models.CharField('Название курса', max_length=100)
    subtitle = models.CharField('Подзаголовок', max_length=300, blank=True)

    short_description = models.CharField('Краткое описание', max_length=500)
    full_description = models.TextField('Полное описание')

    what_you_will_learn = models.TextField('Чему вы научитесь', blank=True)
    requirements = models.TextField('Требования', blank=True)

    status = models.CharField('Статус', max_length=10, choices=STATUS_CHOICES, default=DRAFT)
    is_featured = models.BooleanField('Рекомендуемый курс', default=False)
    certificate_available = models.BooleanField('Выдается сертификат', default=False)

    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    published_at = models.DateTimeField('Дата публикации', blank=True, null=True)

    total_students = models.PositiveIntegerField('Количество студентов', default=0)
    total_lessons = models.PositiveIntegerField('Количество уроков', default=0)

    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    discount_price = models.DecimalField( 'Цена со скидкой', max_digits=10, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0)])

    language = models.ForeignKey(Language, on_delete=models.PROTECT, verbose_name='Язык', related_name='courses', null=True, blank=True)

  
    level = models.ManyToManyField(Level, verbose_name='Уровень', related_name='courses',  null=True)



    #teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Преподаватель', related_name='taught_courses',  null=True)
    students = models.ManyToManyField(Student, related_name='courses', verbose_name='Студенты', blank=True)


    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
   
        

