from django.db import models
from django.conf import settings  
from django.core.validators import MinValueValidator


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

    language = models.ForeignKey('Language', on_delete=models.PROTECT, verbose_name='Язык', related_name='courses', null=True, blank=True)

    # Если курс рассчитан на один уровень:
    # level = models.ForeignKey('Level', on_delete=models.PROTECT, verbose_name='Уровень', related_name='courses')

    # Если на несколько уровней:
    # levels = models.ManyToManyField('Level', verbose_name='Уровни', related_name='courses', blank=True)

    # teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Преподаватель', related_name='taught_courses')
    # students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='enrolled_courses', verbose_name='Студенты', blank=True)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Language(models.Model):
    name = models.CharField('Название языка', max_length=50, unique=True)
    code = models.CharField('Код языка', max_length=10, unique=True)
    description = models.TextField('Описание языка', blank=True)

    is_active = models.BooleanField(
        'Активный',
        default=True,
        help_text='Отображается ли язык на платформе'
    )

    popularity = models.PositiveIntegerField('Популярность', default=0)
    flag_icon = models.CharField('Иконка флага', max_length=50, blank=True)

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'
        ordering = ['name']
        indexes = [
            models.Index(fields=['is_active']),
            models.Index(fields=['popularity']),
        ]

    def __str__(self):
        return self.name

    def get_total_courses(self):
        return self.courses.count()

    def get_total_students(self):
        from django.db.models import Sum
        return self.courses.aggregate(total_students=Sum('total_students'))['total_students'] or 0


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
