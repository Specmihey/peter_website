from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
#для отправки с вложением
from django.core.mail import EmailMessage
from django.contrib import messages

from django.core.paginator import Paginator


# Common variables.
based = {'title': 'DNP Dental',
         'phone': '+36 70 405 6646',
         'email': 'nnnyorba@gmail.com',
         'address': '1115 Budapest, Bartók Béla út 92-94., 1st floor',
         'time': '08:00 - 20:00',
         'face': '#',
         'insta': '#',
         'twitter': '#',
         'whatsapp': '#',
         'youtube': '#',
         'pinterest': '#'
         }

def index(request):
   context={
       'title': 'Стоматологическая клиника Digital Dental Art',
       'description': 'Стоматологическая клиника Digital Dental Art',
       'based': based,
       'doctors_grig': doctors_grig,

   }
   return render(request, 'blog/index.html', context=context)

def about_clinic(request):
   context={
       'title': 'О клинике',
       'super_title': 'О нас',
       'description': 'Стоматологическая клиника Digital Dental Art',
       'based': based,
   }
   return render(request, 'blog/about_clinic.html', context=context)

def price(request):
   context={
       'title': 'Прайс',
       'super_title': 'Наши цены',
       'description': 'Стоматологическая клиника Digital Dental Art',
       'based': based,
   }
   return render(request, 'blog/price.html', context=context)


def faq(request):
   context={
       'title': 'Frequently Asked Questions',
       'super_title': 'Часто задаваемые вопросы',
       'description': 'Стоматологическая клиника Digital Dental Art',
       'based': based,
   }
   return render(request, 'blog/faq.html', context=context)

def time_table(request):
   context={
       'title': 'Время работы',
       'super_title': 'Время работы клиники',
       'description': 'Время работы стоматологической клиники Digital Dental Art',
       'based': based,
   }
   return render(request, 'blog/time_table.html', context=context)

def privacy_policy(request):
   context={
       'title': 'Политика конфиденциальности',
       'super_title': 'Privacy Policy',
       'description': 'Privacy Policy стоматологической клиники Digital Dental Art',
       'based': based,
   }
   return render(request, 'blog/privacy_policy.html', context=context)

def contact(request):
   context={
       'title': 'Контакты клиники',
       'super_title': 'Как нас найти',
       'description': 'Контакты стоматологической клиники Digital Dental Art',
       'based': based,
   }
   return render(request, 'blog/contact.html', context=context)

def appointment(request):
   context={
       'title': 'Записаться на прием',
       'super_title': 'Записаться на прием',
       'description': 'Записаться на прием к врачу клиники Digital Dental Art',
       'based': based,
   }
   return render(request, 'blog/appointment.html', context=context)

def mail_success(request):
   context={
       'title': 'Ваше сообщение отправлено',
       'super_title': 'Ваше сообщение отправлено',
       'description': 'Записаться на прием к врачу клиники Digital Dental Art',
       'based': based,
   }
   return render(request, 'sections/mail-success.html', context=context)

def blog_grid(request):
   context={
       'title': 'Статьи',
       'super_title': 'Каталог статей',
       'description': 'Полезные статьи клиники ',
       'based': based,
   }
   return render(request, 'blog/articles/blog-grid.html', context=context)

def blog_single(request):
   context={
       'title': 'Пример одной статьи',
       'super_title': 'Каталог статей',
       'description': 'Полезные статьи клиники ',
       'based': based,
   }
   return render(request, 'blog/articles/blog-single.html', context=context)

# Вывод списка врачей -- Displaying a list of doctors
doctors_grig = [
    {'title': 'Dr. Nyorba Peter', 'ships_crew': 'Медицинский руководитель', 'img_name': '/static/blog/img/doctors/Dr_Nyorba_Peter.jpg', 'url_name': 'Dr_Nyorba_Peter'},
    {'title': 'Nyorba Peter', 'ships_crew': 'Финансовый директор', 'img_name': '/static/blog/img/doctors/Nyorba_Peter.jpg', 'url_name': 'Nyorba_Peter'},
    {'title': 'Mósa Rita Emese', 'ships_crew': 'Главная ассистентка', 'img_name': '/static/blog/img/doctors/Rita_Emese.jpg', 'url_name': 'Mosa_Rita_Emese'},
    {'title': 'Kiss Anna', 'ships_crew': 'Администратор', 'img_name': '/static/blog/img/doctors/Kiss_Anna.jpg', 'url_name': 'Kiss_Anna'},
    {'title': 'Toth Viktoria', 'ships_crew': 'Ассистентка ', 'img_name': '/static/blog/img/doctors/Toth_Viktoria.jpg', 'url_name': 'Toth_Viktoria'},
    {'title': 'Farkas Fanni', 'ships_crew': 'Ассистентка ', 'img_name': '/static/blog/img/doctors/Farkas_Fanni.jpg', 'url_name': 'Farkas_Fanni'},
    {'title': 'Dr. Aydin Yazdizadeh', 'ships_crew': ' Врач-стоматолог-хирург', 'img_name': '/static/blog/img/doctors/Dr_Aydin_Yazdizadeh.jpg', 'url_name': 'Dr_Aydin_Yazdizadeh'},
    {'title': 'Dr. Ali Fatemi', 'ships_crew': 'Эндодонтист ', 'img_name': '/static/blog/img/doctors/Dr_Ali_Fatemi.jpg', 'url_name': 'Dr_Ali_Fatemi'},
]
def doctors(request):
   context={
       'title': 'Наши врачи',
       'super_title': 'Познакомьтесь с нашей командой',
       'description': 'Лучшие врачи клиники Digital Dental Art',
       'doctors_grig': doctors_grig,
       'based': based,
   }
   return render(request, 'blog//doctors/doctors.html', context=context)

def Dr_Nyorba_Peter(request):
   context={
       'title': 'Dr. Nyorba Peter',
       'super_title': 'Медицинский руководитель',
       'description': 'Медицинский руководитель',
       'based': based,
   }
   return render(request, 'blog/doctors/Dr_Nyorba_Peter.html', context=context)

def Nyorba_Peter(request):
   context={
       'title': 'Nyorba Peter',
       'super_title': 'Финансовый директор',
       'description': 'Финансовый директор',
       'based': based,
   }
   return render(request, 'blog/doctors/Nyorba_Peter.html', context=context)

def Mosa_Rita_Emese(request):
   context={
       'title': 'Mósa Rita Emese ',
       'super_title': 'Главная ассистентка',
       'description': 'Главная ассистентка',
       'based': based,
   }
   return render(request, 'blog/doctors/Mosa_Rita_Emese.html', context=context)

def Kiss_Anna (request):
   context={
       'title': 'Kiss Anna',
       'super_title': 'Ассистентка',
       'description': 'Ассистентка',
       'based': based,
   }
   return render(request, 'blog/doctors/Kiss_Anna.html', context=context)

def Toth_Viktoria(request):
   context={
       'title': 'Tóth Viktória ',
       'super_title': 'Ассистентка',
       'description': 'Ассистентка',
       'based': based,
   }
   return render(request, 'blog/doctors/Toth_Viktoria.html', context=context)

def Farkas_Fanni(request):
   context={
       'title': 'Farkas Fanni',
       'super_title': 'Ассистентка',
       'description': 'Ассистентка',
       'based': based,
   }
   return render(request, 'blog/doctors/Farkas_Fanni.html', context=context)

def Dr_Aydin_Yazdizadeh(request):
   context={
       'title': 'Dr. Aydin Yazdizadeh',
       'super_title': 'Врач-стоматолог-хирург',
       'description': 'Врач-стоматолог-хирург',
       'based': based,
   }
   return render(request, 'blog/doctors/Dr_Aydin_Yazdizadeh.html', context=context)


def Dr_Ali_Fatemi(request):
   context={
       'title': 'Dr. Ali Fatemi ',
       'super_title': 'Эндодонтист',
       'description': 'Эндодонтист',
       'based': based,
   }
   return render(request, 'blog/doctors/Dr_Ali_Fatemi.html', context=context)

# ------------------------------- Лечение
view_list_aesthetic_dentistry = [
    {'title': 'Отбеливание зубов', 'img_path': '/static/blog/img/teeth/smile_400_300.jpg',
     'url_name': 'teeth_whitening', 'decription': 'Ваши зубы изменили цвет и пятна, и из-за этого вы не смеете улыбаться? Мы поможем вам с вашей проблемой!'},
    {'title': 'Удаление зубного камня', 'img_path': '/static/blog/img/teeth/del_1_400_300.jpg',
     'url_name': 'removal_tartar', 'decription': 'Когда рекомендуется приступать к удалению зубного камня?'},
    {'title': 'Прессованная керамическая оболочка E.max', 'img_path': '/static/blog/img/teeth/press_2_400_300.jpg',
     'url_name': 'pressed_ceramic_shell_e_max', 'decription': 'Исправить эстетические недостатки зубов'},
    #{'title': '', 'img_path': '', 'url_name': '', 'decription': ''},
]

def consultation(request):
   context={
       'title': 'Консультация',
       'super_title': 'Лечение',
       'description': 'Полезные статьи клиники ',
       'based': based,
   }
   return render(request, 'blog/therapy/consultation.html', context=context)

def aesthetic_dentistry(request):
   context={
       'title': 'Эстетическая стоматология',
       'super_title': 'Услуги клиники',
       'description': 'Стоматологическая клиника Digital Dental Art',
       'based': based,
       'view_list_aesthetic_dentistry': view_list_aesthetic_dentistry,
   }
   return render(request, 'blog/therapy/aesthetic_dentistry.html', context=context)

def teeth_whitening(request):
   context={
       'title': 'Отбеливание зубов',
       'super_title': 'Услуги клиники',
       'description': 'Стоматологическая клиника Digital Dental Art',
       'based': based,
   }
   return render(request, 'blog/therapy/teeth_whitening.html', context=context)

def removal_tartar(request):
   context={
       'title': 'Удаление зубного камня',
       'super_title': 'Услуги клиники',
       'description': 'Когда рекомендуется делать удаление зубного камня?',
       'based': based,
   }
   return render(request, 'blog/therapy/removal_tartar.html', context=context)

def pressed_ceramic_shell_e_max(request):
   context={
       'title': 'Прессованная керамическая оболочка E.max',
       'super_title': 'Когда прессованная керамическая оболочка является лучшим решением?',
       'description': 'Когда прессованная керамическая оболочка является лучшим решением?',
       'based': based,
   }
   return render(request, 'blog/therapy/pressed_ceramic_shell.html', context=context)

# korona
view_list_korona = [
    {'title': 'Керамическая коронка E.Max', 'img_path': '/static/blog/img/service/corona/cirkonium-korona-teeth-whitening_1.jpg',
     'url_name': 'e_max_ceramic_crown', 'decription': 'Когда рекомендуется использовать прессованную керамическую коронку?'},
    {'title': 'Циркониевая коронка', 'img_path': '/static/blog/img/service/corona/preskeramia-korona-emax_3.jpg',
     'url_name': 'zirconium_crown', 'decription': 'Каковы преимущества циркониевой коронки?'},
    {'title': 'Металлокерамическая коронка', 'img_path': '/static/blog/img/service/corona/femkeramia-korona-femkeramia-korona-fogpotlas-femporc-8.jpg',
     'url_name': 'ceramic_metal_crown', 'decription': 'Когда рекомендуется металлическая керамическая коронка?'},
    #{'title': '', 'img_path': '', 'url_name': '', 'decription': ''},
]
def korona(request):
   context={
       'title': 'korona',
       'super_title': 'korona',
       'description': 'Когда рекомендуется использовать прессованную керамическую коронку?',
       'based': based,
       'view_list_korona': view_list_korona,
   }
   return render(request, 'blog/therapy/korona.html', context=context)

def e_max_ceramic_crown(request):
   context={
       'title': 'Керамическая коронка E.Max',
       'super_title': 'Когда рекомендуется использовать прессованную керамическую коронку?',
       'description': 'Когда рекомендуется использовать прессованную керамическую коронку?',
       'based': based,
   }
   return render(request, 'blog/therapy/e_max_ceramic_crown_3.html', context=context)

def zirconium_crown(request):
   context={
       'title': 'Циркониевая коронка',
       'super_title': 'Каковы преимущества циркониевой коронки?',
       'description': 'Каковы преимущества циркониевой коронки?',
       'based': based,
   }
   return render(request, 'blog/therapy/zirconium_crown_4.html', context=context)

def ceramic_metal_crown(request):
   context={
       'title': 'Металлокерамическая коронка',
       'super_title': 'Когда рекомендуется металлическая керамическая коронка?',
       'description': 'Когда рекомендуется металлическая керамическая коронка?',
       'based': based,
   }
   return render(request, 'blog/therapy/ceramic_metal_crown_5.html', context=context)


# --- Лечение общий список ???
def service(request):
   context={
       'title': 'Услуги клиники',
       'super_title': 'Услуги клиники',
       'description': 'Стоматологическая клиника Digital Dental Art',
       'based': based,
       'view_list_aesthetic_dentistry': view_list_aesthetic_dentistry,
   }
   return render(request, 'blog/therapy/service.html', context=context)

# --- Вывод статей блога

def blog_list(request):
    posts = PageItem.objects.all()
    paginator = Paginator(posts, 5)  # Show 5 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    category_list = Category.objects.all()
    review_category_list = Category.objects.all()
    excellence = Category.objects.all()
    context = {
        'posts': posts,
        'category_list': category_list,
        'title': 'Блог клиники',
        'description': 'Блог стоматологической клиники Digital Dental Art.',
        'based': based,
        'page_obj': page_obj,
        'review_category_list': review_category_list,
        'excellence': excellence,
    }
    return render(request, 'blog/articles/blog-grid.html', context=context)


def show_post(request, post_slug):
    post = get_object_or_404(PageItem, slug=post_slug)
    context = {
        'title': post.title,
        'description': post.description,
        'based': based,
        'post':post,
    }
    return render(request, 'blog/articles/blog-single.html', context=context)



