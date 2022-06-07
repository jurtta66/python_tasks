from django.db import models


class Student(models.Model):
    name = models.CharField("Имя", max_length=50)
    spec = models.TextField("Специальность", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'