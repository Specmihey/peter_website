from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
# from .sitemap import StaticViewSitemap, PostSitemap, staffUnitSitemap

from .views import *

urlpatterns = [
    path('', index, name='home'),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]



# sitemaps = {
#    'static': StaticViewSitemap,
#    'posts': PostSitemap,
#    'staff': staffUnitSitemap,
# }
