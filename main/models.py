from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    avatar = models.ImageField(upload_to='student/', verbose_name='аватар', null=True, blank=True)

    is_active = models.BooleanField(default=True, verbose_name='учится')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ('last_name',)


class Subject(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание', null=True, blank=True)

    students = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'
