from django.db import models
from django.conf import settings
from django.urls import reverse         #! NEW


# Create your models here.
class Thread(models.Model):
    title = models.CharField(max_length=255, verbose_name="Назва теми")
    description = models.TextField(blank=True, verbose_name="Опис теми")
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('thread_detail', kwargs={'pk': self.pk})
    class Meta:
        verbose_name = "Гілка форуму"
        verbose_name_plural = "Гілки форуму"
        
    

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Повідомлення")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Пост від {self.author.username} в {self.thread.title}"
    
    

    