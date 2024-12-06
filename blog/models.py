import os
from django.db import models
from PIL import Image
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# === Doctors
class Doctor(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255, verbose_name='Описание')
    name = models.CharField(max_length=200)
    ships_crew = models.CharField(max_length=200, verbose_name='Должность')
    img_name = models.ImageField(upload_to='img_doctors/%Y/%m/%d', blank=True, verbose_name='Фото')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Опубликовано')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Контент')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
