from django.db import models

from config import settings
from users.models import User

NULLABLE: dict[str, bool] = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название курса', **NULLABLE)
    image = models.ImageField(upload_to='course_image/', verbose_name='изображение', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    price = models.IntegerField(default=0, verbose_name='стоимость курса')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        ordering = ('title',)


class Lessons(models.Model):
    title = models.CharField(max_length=100, verbose_name='название курса', **NULLABLE)
    image = models.ImageField(upload_to='Lessons_image/', verbose_name='изображение', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    link = models.CharField(max_length=500, verbose_name='Ссылка', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'лекция'
        verbose_name_plural = 'лекции'
        ordering = ('course',)


class Payment(models.Model):
    PAYMENT_METHOD = [
        ('CARD', 'перевод на счет'),
        ('CASH', 'наличными средствами'),
    ]

    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.SET_NULL, **NULLABLE)
    pay_date = models.DateField(verbose_name='дата оплаты', auto_now_add=True, **NULLABLE)
    course = models.ForeignKey(Course, verbose_name='название курса', on_delete=models.CASCADE, **NULLABLE)
    price = models.IntegerField(default=0, verbose_name='стоимость курса')
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHOD, verbose_name='Способ оплаты')

    def __str__(self):
        return f'{self.course} - {self.price}'

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'
        ordering = ('price',)
