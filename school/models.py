from django.db import models

NULLABLE: dict[str, bool] = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название курса', **NULLABLE)
    image = models.ImageField(upload_to='course_image/', verbose_name='изображение', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)

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

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'лекция'
        verbose_name_plural = 'лекции'
        ordering = ('title',)
