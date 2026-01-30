from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator, MaxLengthValidator



# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва предмету")
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предмети"
        
class Grade(models.Model):
    value = models.IntegerField(validators=[MinLengthValidator(1), 
                                            MaxLengthValidator(12)],
                                            verbose_name = "Оцінка")
    student = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE,
                                related_name='grades',
                                limit_choices_to={'is_student': True},
                                verbose_name="Студент")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,
                                verbose_name="Предмет")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    comment = models.TextField(blank=True, verbose_name="Коментар",
                                max_length=255)
    def __str__(self):
        return f"{self.student.username} - {self.subject.name} - {self.value}"
    
    class Meta:
        verbose_name = "Оцінка"
        verbose_name_plural = "Оцінки"
        ordering = ['-date']
        
    
