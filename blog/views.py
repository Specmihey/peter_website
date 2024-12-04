from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def index(request):
   context={
       'title': 'Стоматологическая клиника Digital Dental Art',
       'description': 'Стоматологическая клиника Digital Dental Art',

   }
   return render(request, 'blog/index.html', context=context)

def about_clinic(request):
   context={
       'title': 'О клинике',
       'super_title': 'О нас',
       'description': 'Стоматологическая клиника Digital Dental Art',

   }
   return render(request, 'blog/about_clinic.html', context=context)

def price(request):
   context={
       'title': 'Прайс',
       'super_title': 'Наши цены',
       'description': 'Стоматологическая клиника Digital Dental Art',

   }
   return render(request, 'blog/price.html', context=context)


def faq(request):
   context={
       'title': 'Frequently Asked Questions',
       'super_title': 'Часто задаваемые вопросы',
       'description': 'Стоматологическая клиника Digital Dental Art',

   }
   return render(request, 'blog/faq.html', context=context)

def time_table(request):
   context={
       'title': 'Время работы',
       'super_title': 'Время работы клиники',
       'description': 'Время работы стоматологической клиники Digital Dental Art',

   }
   return render(request, 'blog/time_table.html', context=context)

def privacy_policy(request):
   context={
       'title': 'Политика конфиденциальности',
       'super_title': 'Privacy Policy',
       'description': 'Privacy Policy стоматологической клиники Digital Dental Art',

   }
   return render(request, 'blog/privacy_policy.html', context=context)

def contact(request):
   context={
       'title': 'Контакты клиники',
       'super_title': 'Как нас найти',
       'description': 'Контакты стоматологической клиники Digital Dental Art',

   }
   return render(request, 'blog/contact.html', context=context)

def appointment(request):
   context={
       'title': 'Записаться на прием',
       'super_title': 'Записаться на прием',
       'description': 'Записаться на прием к врачу клиники Digital Dental Art',

   }
   return render(request, 'blog/appointment.html', context=context)

def mail_success(request):
   context={
       'title': 'Ваше сообщение отправлено',
       'super_title': 'Записаться на прием',
       'description': 'Записаться на прием к врачу клиники Digital Dental Art',

   }
   return render(request, 'sections/mail-success.html', context=context)

def blog_grid(request):
   context={
       'title': 'Статьи',
       'super_title': 'Каталог статей',
       'description': 'Полезные статьи клиники ',

   }
   return render(request, 'blog/articles/blog-grid.html', context=context)

def blog_single(request):
   context={
       'title': 'Пример одной статьи',
       'super_title': 'Каталог статей',
       'description': 'Полезные статьи клиники ',

   }
   return render(request, 'blog/articles/blog-single.html', context=context)

doctors_grig = [
    {'name': 'Dr. Nyorba Peter', 'ships_crew': 'Медицинский руководитель', 'url_name': '/static/blog/img/doctors/Dr_Nyorba_Peter.jpg'},
    {'name': 'Nyorba Peter', 'ships_crew': 'финансовый директор', 'url_name': '/static/blog/img/doctors/Nyorba_Peter.jpg'},
    {'name': 'Mósa Rita Emese', 'ships_crew': 'главная ассистентка', 'url_name': '/static/blog/img/doctors/Rita_Emese.jpg'},
    {'name': 'Kiss Anna', 'ships_crew': 'администратор', 'url_name': '/static/blog/img/doctors/Kiss_Anna.jpg'},
    {'name': 'Toth Viktoria', 'ships_crew': 'ассистентка ', 'url_name': '/static/blog/img/doctors/Toth_Viktoria.jpg'},
    {'name': 'Farkas Fanni', 'ships_crew': 'ассистентка ', 'url_name': '/static/blog/img/doctors/Farkas_Fanni.jpg'},
    {'name': 'Dr. Aydin Yazdizadeh', 'ships_crew': ' врач-стоматолог-хирург', 'url_name': '/static/blog/img/doctors/Dr_Aydin_Yazdizadeh.jpg'},
    {'name': 'Dr. Ali Fatemi', 'ships_crew': 'эндодонтист ', 'url_name': '/static/blog/img/doctors/Dr_Ali_Fatemi.jpg'},
]
def doctors(request):
   context={
       'title': 'Наши врачи',
       'super_title': 'Познакомьтесь с нашими врачами',
       'description': 'Лучшие врачи клиники Digital Dental Art',
       'doctors_grig': doctors_grig,
   }
   return render(request, 'blog//doctors/doctors.html', context=context)

def Dr_Nyorba_Peter(request):
   context={
       'title': 'Dr. Nyorba Peter',
       'super_title': 'Медицинский руководитель',
       'description': 'Медицинский руководитель',

   }
   return render(request, 'blog/doctors/Dr_Nyorba_Peter.html', context=context)


# ------------------------------- Лечение
def service(request):
   context={
       'title': 'Услуги клиники',
       'super_title': 'Услуги клиники',
       'description': 'Стоматологическая клиника Digital Dental Art',

   }
   return render(request, 'blog/therapy/service.html', context=context)

def consultation(request):
   context={
       'title': 'Консультация',
       'super_title': 'Лечение',
       'description': 'Полезные статьи клиники ',

   }
   return render(request, 'blog/therapy/consultation.html', context=context)

def aesthetic_dentistry(request):
   context={
       'title': 'эстетическая стоматология',
       'super_title': 'Услуги клиники',
       'description': 'Стоматологическая клиника Digital Dental Art',

   }
   return render(request, 'blog/therapy/aesthetic_dentistry.html', context=context)
def teeth_whitening(request):
   context={
       'title': 'Отбеливание зубов',
       'super_title': 'Услуги клиники',
       'description': 'Стоматологическая клиника Digital Dental Art',

   }
   return render(request, 'blog/therapy/teeth_whitening.html', context=context)





