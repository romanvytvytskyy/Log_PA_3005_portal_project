from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    CATEGORY_CHOICES = [
        ('edu', 'Навчання'),
        ('rest', 'Відпочинок'),
        ('admin', 'Організаційні')
    ]
    
    title = models.CharField(max_length=255, verbose_name="Назва події")
    description = models.TextField(blank=True, verbose_name="Опис події")
    start_time = models.DateTimeField(verbose_name="Час початку події")
    end_time = models.DateTimeField(verbose_name="Час закінчення події")
    location = models.CharField(max_length=255, verbose_name="Місце проведення події")
    category = models.CharField(choices=CATEGORY_CHOICES, 
                                default='edu', 
                                verbose_name='Категорія')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, 
                               on_delete=models.CASCADE,
                               verbose_name='Організатор')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Подія"
        verbose_name_plural = "Події"
        
    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'pk': self.pk})
    
    @property
    def is_past(self):
        return timezone.now() > self.end_time

    @property
    def is_ongoing(self):
        return self.start_time <= timezone.now() <= self.end_time

    @property
    def is_upcoming(self):
        return timezone.now() < self.start_time


