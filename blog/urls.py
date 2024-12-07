from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
# from .sitemap import StaticViewSitemap, PostSitemap, staffUnitSitemap

from .views import *

urlpatterns = [
    path('', index, name='home'),
    # Doctors' Block -- Блок врачей
    path('doctors/', doctors, name='doctors'), # catalog of doctors
    path('doctors/Dr_Nyorba_Peter/', Dr_Nyorba_Peter, name='Dr_Nyorba_Peter'), # Dr_Nyorba_Peter
    path('doctors/Nyorba_Peter/', Nyorba_Peter, name='Nyorba_Peter'), # Nyorba Péter
    path('doctors/Mosa_Rita_Emese/', Mosa_Rita_Emese, name='Mosa_Rita_Emese'), # Mosa_Rita_Emese
    path('doctors/Kiss_Anna/', Kiss_Anna, name='Kiss_Anna'), # Kiss_Anna
    path('doctors/Toth_Viktoria/', Toth_Viktoria, name='Toth_Viktoria'), # Toth_Viktoria
    path('doctors/Farkas_Fanni/', Farkas_Fanni, name='Farkas_Fanni'), # Farkas_Fanni
    path('doctors/Dr_Aydin_Yazdizadeh/', Dr_Aydin_Yazdizadeh, name='Dr_Aydin_Yazdizadeh'), # Dr_Aydin_Yazdizadeh
    path('doctors/Dr_Ali_Fatemi/', Dr_Ali_Fatemi, name='Dr_Ali_Fatemi'), # Dr_Ali_Fatemi
    # About clinic -- О клинике
    path('price/', price, name='price'), #price
    path('about-clinic/', about_clinic, name='about-clinic'), #о клинике
    # path('faq/', faq, name='faq'), #FAQ
    path('time_table/', time_table, name='time_table'), #time_table
    path('appointment/', appointment, name='appointment'), # Записаться на прием
    path('contact/', contact, name='contact'), # contact
    path('mail-success/', mail_success, name='mail_success'), # mail-success
    path('privacy_policy/', privacy_policy, name='privacy_policy'), #privacy_policy
    path('warranty/', warranty, name='warranty'), # warranty.html
    # Articles -- Блок статей
    # path('blog-grid/', blog_grid, name='blog_grid'), # Блог, каталог статей
    # path('blog-grid/blog-single/', blog_single, name='blog_single'), # Блог, одна статья
    path('blog/', blog_list, name='blog'),
    path('blog/<slug:post_slug>/', show_post, name='post'),
    # Treatment unit -- Блок лечения
    path('service/', service, name='service'), # Лечение
    path('service/consultation/', consultation, name='consultation'), # Консультация
    # эстетическая стоматология
    path('service/aesthetic-dentistry/', aesthetic_dentistry, name='aesthetic_dentistry'), # эстетическая стоматология
    path('service/aesthetic-dentistry/teeth-whitening/', teeth_whitening, name='teeth_whitening'), # Отбеливание зубов
    path('service/aesthetic-dentistry/removal-tartar/', removal_tartar, name='removal_tartar'), # Удаление зубного камня
    path('service/aesthetic-dentistry/pressed-ceramic-shell/', pressed_ceramic_shell_e_max, name='pressed_ceramic_shell_e_max'), # Прессованная керамическая оболочка E.max
    # Короны
    path('service/korona/', korona, name='korona'), # korona
    path('service/korona/e_max_ceramic_crown', e_max_ceramic_crown, name='e_max_ceramic_crown'), # Керамическая коронка E.Max
    path('service/korona/zirconium-crown', zirconium_crown, name='zirconium_crown'), # Циркониевая коронка
    path('service/korona/ceramic-metal-crown', ceramic_metal_crown, name='ceramic_metal_crown'), # Металлокерамическая коронка

]



# sitemaps = {
#    'static': StaticViewSitemap,
#    'posts': PostSitemap,
#    'staff': staffUnitSitemap,
# }
