from django.forms import ModelForm
from django import forms
#from captcha.fields import CaptchaField
from .models import *

#from captcha.fields import CaptchaField

''' 
#Форма без модели
#--- Отправка почты
class ContactForm(forms.Form):
    country = forms.CharField(label='Страна', widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'class':'form-control', "rows": 5}))
    #captcha = CaptchaField()
'''

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Имя*")
    phone_number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Телефон*")
    from_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label="email*")
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', "rows": 5}), label="Сообщение")
    #captcha = CaptchaField()

#План лечения без модели
class ApplicationForm(forms.Form):
    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Страна*")
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Имя*")
    treatment = [('Выбрать', 'Выбрать'), ('Срочно', 'Срочно'), ('Через 3 мес', 'Через 3 мес'), ('Через полгода', 'Через полгода'),('Через год', 'Через год'),('Сбор информации', 'Сбор информации'),]
    treatment_type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-select form-select-lg mb-3'}), label="Как срочно необходимо лечение*",choices=treatment)
    phone_number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Телефон*")
    from_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label="email*")
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', "rows": 5}), label="Сообщение")
    #captcha = CaptchaField()
