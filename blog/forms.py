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
# HOME Contact
class ContactHomeForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Имя*")
    treatment = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Направление лечения*")
    phone_number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Телефон*")
    from_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label="email*")
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', "rows": 5}), label="Сообщение")
    #captcha = CaptchaField()

# Contact
class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Имя*")
    treatment = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Направление лечения*")
    phone_number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Телефон*")
    from_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label="email*")
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', "rows": 5}), label="Сообщение")
    #captcha = CaptchaField()

#Записаться на прием без модели
class ApplicationForm(forms.Form):
    #country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Страна*")
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Имя*")
    treatment = [('Kezelések', 'Лечение'), ('Csontpótlás', 'Замена кости'), ('All-on-4™ és All-on-6™ fogpótlások', 'Протезы All-on-4™ и All-on-6™'),
                 ('8 implantátumon rögzített körhíd', 'Круглый мост на 8 имплантах'),('Bölcsességfog eltávolítás', 'Удаление зуба мудрости'),
                 ('Foghúzás5', 'Удаление зуба'), ('Fog implantáció', 'Имплантация зубов'), ('Inlay/ Onlay', 'Inlay/ Onlay'), ('Gyökérkezelés', 'Лечение корней'),
                 ('Tömés', 'Пломбирование'), ('Ideiglenes fogpótlások', 'Временные протезы'), ('Implantátumokkal stabilizált kivehető fogsorok', 'Съемные протезы, стабилизированные имплантатами'),
                 ('Teljes/ részleges kivehető fogsorok', 'Полные/частичные съемные протезы'), ('Fogászati hidak', 'Зубные мосты'), ('E.Max péskerámia korona, héj', 'Керамическая коронка E.Max'),
                 ('Cirkónium korona', 'Циркониевая коронка'), ('Fémkerámia korona', 'Металлокерамическая коронка'), ('E.max préskerámia héj', 'Прессованная керамическая оболочка E.max'),
                 ('Fogfehérítés', 'Отбеливание зубов'), ('Fogászati konzultáció, fogászati állapotfelmérés', 'Консультация стоматолога, оценка состояния зубов'),
                 ('Fogkőeltávolítás', 'Удаление зубного камня'), ('Egyéb', 'Другое')]
    treatment_type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'nice-select form-control wide'}), label="Направление лечения*",choices=treatment)
    phone_number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Телефон*")
    from_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label="email*")
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', "rows": 5}), label="Сообщение")
    #captcha = CaptchaField()
