from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
# from .sitemap import StaticViewSitemap, PostSitemap, staffUnitSitemap

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('doctors/', doctors, name='doctors'), # catalog of doctors
    path('doctors/doctor-details/', doctor_details, name='doctor_details'), # an example of a single doctor's page
    path('about-clinic/', about_clinic, name='about-clinic'), #о клинике
    path('service/price/', price, name='price'), #price
    path('faq/', faq, name='faq'), #FAQ
    path('service/', service, name='service'), #service
    path('time_table/', time_table, name='time_table'), #time_table
    path('contact/', contact, name='contact'), # contact
    path('service/appointment/', appointment, name='appointment'), # Записаться на прием
    path('mail-success/', mail_success, name='mail_success'), # mail-success
    path('blog-grid/', blog_grid, name='blog_grid'), # Блог, каталог статей
    path('blog-grid/blog-single/', blog_single, name='blog_single'), # Блог, одна статья
    path('privacy_policy/', privacy_policy, name='privacy_policy'), #privacy_policy
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]



# sitemaps = {
#    'static': StaticViewSitemap,
#    'posts': PostSitemap,
#    'staff': staffUnitSitemap,
# }
