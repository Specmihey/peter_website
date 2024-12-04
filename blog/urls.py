from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
# from .sitemap import StaticViewSitemap, PostSitemap, staffUnitSitemap

from .views import *

urlpatterns = [
    path('', index, name='home'),
    # Doctors' Block -- Блок врачей
    path('doctors/', doctors, name='doctors'), # catalog of doctors
    path('doctors/doctor-details/', doctor_details, name='doctor_details'), # an example of a single doctor's page
    # About clinic -- О клинике
    path('service/price/', price, name='price'), #price
    path('about-clinic/', about_clinic, name='about-clinic'), #о клинике
    path('faq/', faq, name='faq'), #FAQ
    path('time_table/', time_table, name='time_table'), #time_table
    path('service/appointment/', appointment, name='appointment'), # Записаться на прием
    path('contact/', contact, name='contact'), # contact
    path('mail-success/', mail_success, name='mail_success'), # mail-success
    path('privacy_policy/', privacy_policy, name='privacy_policy'), #privacy_policy
    # Articles -- Блок статей
    path('blog-grid/', blog_grid, name='blog_grid'), # Блог, каталог статей
    path('blog-grid/blog-single/', blog_single, name='blog_single'), # Блог, одна статья
    # Treatment unit -- Блок лечения
    path('service/', service, name='service'), # Лечение
    path('service/consultation/', consultation, name='consultation'), # Консультация
    path('service/aesthetic-dentistry/', aesthetic_dentistry, name='aesthetic_dentistry'), # эстетическая стоматология
    path('service/aesthetic-dentistry/teeth-whitening/', teeth_whitening, name='teeth_whitening'), # Отбеливание зубов

]



# sitemaps = {
#    'static': StaticViewSitemap,
#    'posts': PostSitemap,
#    'staff': staffUnitSitemap,
# }
