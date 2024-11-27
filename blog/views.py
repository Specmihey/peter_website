from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def index(request):
   context={
       'title': 'Digital Dental Art',
       'description': 'Стоматологическая клиника Digital Dental Art',

   }
   return render(request, 'blog/index.html', context=context)
