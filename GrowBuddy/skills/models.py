from django.db import models
from django.urls import reverse

class Skill(models.Model):
    PROGRESS_CHOICES = [(i, f"{i}%") for i in range(0, 101, 10)]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    progress = models.IntegerField(choices=PROGRESS_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    last_practiced = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse('skill-detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.name
