import os
from django.db import models
from PIL import Image
from django.urls import reverse

# Статьи
class PageItem(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.CharField(max_length=255, verbose_name='Описание')
    content = models.TextField(blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')
    video_link = models.CharField(max_length=255, verbose_name='You-tube')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-time_created', 'title']


# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['id', 'name']

class ImgPost(models.Model):
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    image = models.ImageField(upload_to='post_photos/%Y/%m', verbose_name='Фото')
    album = models.ForeignKey(PageItem, on_delete=models.PROTECT, verbose_name='Пост')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото постов'
        verbose_name_plural = 'Фото постов'
        ordering = ['-date_modified', 'title']

# Апартаменты
class apartamentItem(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    longtitle = models.CharField(max_length=255, blank=True, verbose_name='Расширенный')
    description = models.CharField(max_length=255, blank=True, verbose_name='Описание')
    introtext = models.CharField(max_length=255, blank=True, verbose_name='Аннотация')
    content = models.TextField(blank=True, verbose_name='Контент')
    img = models.ImageField(upload_to='apartaments/%Y/%m/%d', verbose_name='Фото')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('apartament', kwargs={'apartament_slug': self.slug})

    class Meta:
        verbose_name = 'Апартамент'
        verbose_name_plural = 'Апартаменты'
        ordering = ['time_created', 'title']

# ==============Gallery models
# class Album(models.Model):
#     name = models.CharField(max_length=255, verbose_name='Название альбома')
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
#     summary = models.TextField(blank=True, verbose_name='Описание')
#     date_created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
#     date_modified = models.DateTimeField(auto_now=True, verbose_name='Изменено')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Альбом'
#         verbose_name_plural = 'Альбомы'
#         ordering = ['date_modified', 'name']

class Photo(models.Model):
    title = models.CharField(max_length=255)
    # summary = models.TextField(blank=True, null=True, verbose_name='Описание')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    image = models.ImageField(upload_to='gall_photos/%Y/%m', verbose_name='Фото')
    #album = models.ForeignKey('Album', on_delete=models.CASCADE, verbose_name='Альбом')
    # is_cover_photo = models.BooleanField(verbose_name='Обложка альбома')
    album = models.ForeignKey('apartamentItem', on_delete=models.PROTECT, verbose_name='Апартаменты')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии апартаментов'
        ordering = ['-date_modified', 'title']

#---- Contact Forms
class Patients(models.Model):
    last_name = models.CharField(max_length=15, blank=True, verbose_name='Фамилия')
    first_name = models.CharField(max_length=15, verbose_name='Имя')
    birth_day = models.DateField(blank=True, verbose_name='ДР')
    emails = models.EmailField(blank=True, verbose_name='email')
    #phone = PhoneField(blank=True, help_text='Введите номер телефона', verbose_name='Телефон')
    phone = models.IntegerField(help_text='Введите номер телефона',verbose_name='Телефон')
    description = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='patients_img/%Y/%m/%d/', verbose_name='Фото', blank=True)
    country = models.ForeignKey('Country', on_delete=models.PROTECT, null=True, verbose_name='Страна')
    reminder_days = models.DateTimeField(blank=True, verbose_name='Напоминание')
    # reminder_days = models.ForeignKey('ReminderDay', on_delete=models.PROTECT, null=True,verbose_name='День напоминания')
    treatment_types = models.ForeignKey('TreatmentType', on_delete=models.PROTECT, null=True,
                                        verbose_name='Вид лечения')
    treatment_status = models.ForeignKey('TreatmentStatus', on_delete=models.PROTECT, null=True,
                                         verbose_name='Статус лечения')

    # https://pypi.org/project/django-phone-field/ PhoneField

    def get_absolute_url(self):
        return reverse('patients-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        ordering = ['-created_at']


class Country(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Страна')

    def get_absolute_url(self):
        return reverse('country', kwargs={"country_id": self.pk})

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        ordering = ['title']

    def __str__(self):
        return self.title


# class ReminderDay(models.Model):
#     days = models.DateTimeField(blank=True,verbose_name='Напоминание')

# class Meta:
#     verbose_name = 'Напоминание'
#     verbose_name_plural = 'Напоминания'
#     ordering = ['days']
#
# def __str__(self):
#     #return self.days
#     return str(self.days)

class TreatmentType(models.Model):
    title = models.CharField(max_length=15, verbose_name='Вид лечения')

    # def get_absolute_url(self):
    # return reverse('treatment_type', kwargs={"country_id": self.pk})

    class Meta:
        verbose_name = 'Вид лечения'
        verbose_name_plural = 'Виды лечения'
        ordering = ['title']

    def __str__(self):
        return self.title


class TreatmentStatus(models.Model):
    title = models.CharField(max_length=15, verbose_name='Статус лечения')

    # def get_absolute_url(self):
    # return reverse('treatment_type', kwargs={"country_id": self.pk})

    class Meta:
        verbose_name = 'Статус лечения'
        verbose_name_plural = 'Статусы лечения'
        ordering = ['title']

    def __str__(self):
        return self.title


# === Doctors
class Doctor(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255, blank=True, verbose_name='Описание')
    name = models.CharField(max_length=200, blank=True, verbose_name='Резерв')
    ships_crew = models.CharField(max_length=200, verbose_name='Должность')
    photo = models.ImageField(upload_to='img_doctors/%Y/%m/%d', blank=True, verbose_name='Фото')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Опубликовано')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Контент')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('doctor', kwargs={'doctor_slug': self.slug})

    class Meta:
        ordering = ['-created_at']