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

def doctors(request):
   context={
       'title': 'Наши врачи',
       'super_title': 'Познакомьтесь с нашими квалифицированными врачами',
       'description': 'Лучшие врачи клиники Digital Dental Art',

   }
   return render(request, 'blog/doctors.html', context=context)

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

def service(request):
   context={
       'title': 'Услуги',
       'super_title': 'Услуги клиники',
       'description': 'Стоматологическая клиника Digital Dental Art',

   }
   return render(request, 'blog/service.html', context=context)

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

