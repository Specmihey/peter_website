from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

#ckeditor
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = PageItem
        fields = '__all__'
#ckeditor




# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class PageItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_created', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published','time_created', 'cat')
    prepopulated_fields = {"slug": ("title",)}
    #fields - список редактируемых полей
    fields = ('title', 'slug', 'description','cat','photo','get_html_photo', 'content','is_published','time_created', 'time_updated')
    readonly_fields = ('time_created', 'time_updated','get_html_photo')
    form = PostAdminForm

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=85")

    get_html_photo.short_description = "Миниатюра"

class apartamentItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_created', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'introtext')
    list_editable = ('is_published',)
    list_filter = ('is_published','time_created')
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'longtitle', 'slug', 'description', 'introtext', 'content','img','get_html_photo', 'is_published','time_created', 'time_updated')
    readonly_fields = ('time_created', 'time_updated','get_html_photo')

    def get_html_photo(self, object):
        if object.img:
            return mark_safe(f"<img src='{object.img.url}' width=85")

    get_html_photo.short_description = "Миниатюра"

# ==============Gallery models
# class AlbumAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'slug', 'date_created', 'date_modified')
#     list_display_links = ('id', 'name')
#     search_fields = ('name',)
#     list_filter = ('date_created', 'date_modified')
#     prepopulated_fields = {"slug": ("name",)}

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_created', 'date_modified', 'get_html_photo', 'album')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'album')
    list_filter = ('date_created', 'date_modified', 'album')
    readonly_fields = ('get_html_photo', 'date_created', 'date_modified' )

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=85")

    get_html_photo.short_description = "Миниатюра"

class ImgPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_created', 'date_modified', 'get_html_photo', 'album')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'album')
    list_filter = ('date_created', 'date_modified', 'album')
    readonly_fields = ('get_html_photo', 'date_created', 'date_modified' )

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=85")

    get_html_photo.short_description = "Миниатюра"

# --- Contact Forms
class PatientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'created_at', 'reminder_days', 'emails', 'phone')
    list_display_links = ('id', 'last_name')
    search_fields = ('last_name', 'emails','reminder_days')
    list_editable = ('emails', 'phone','reminder_days')
    list_filter = ('last_name', 'phone','reminder_days')

# === Doctor
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'ships_crew', 'get_html_photo', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=85")

admin.site.register(Category, CategoryAdmin)
admin.site.register(PageItem, PageItemAdmin)
admin.site.register(apartamentItem, apartamentItemAdmin)
# admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(ImgPost, ImgPostAdmin)

admin.site.register(Patients, PatientsAdmin)
admin.site.register(TreatmentType)
admin.site.register(Country)
#admin.site.register(ReminderDay)
admin.site.register(TreatmentStatus)
admin.site.register(Doctor, DoctorAdmin)



