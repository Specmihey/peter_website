from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
# from .sitemap import StaticViewSitemap, PostSitemap, staffUnitSitemap

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('doctors/', doctors, name='doctors'),
    path('about-clinic/', about_clinic, name='about-clinic'), #о клинике
    path('price/', price, name='price'), #price
    path('faq/', faq, name='faq'), #FAQ
    path('service/', service, name='service'), #service
    path('time_table/', time_table, name='time_table'), #time_table
    path('contact/', contact, name='contact'), # contact
    path('privacy_policy/', privacy_policy, name='privacy_policy'), #privacy_policy
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]



# sitemaps = {
#    'static': StaticViewSitemap,
#    'posts': PostSitemap,
#    'staff': staffUnitSitemap,
# }
