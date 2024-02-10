from django.contrib import admin
from django.contrib.admin import register
from phonebook.models import Phonebook


# Register your models here.
@register(Phonebook)
class PhonebookAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number')
    search_fields = ('first_name', 'last_name', 'phone_number')
    list_filter = ('first_name', 'last_name', 'phone_number')
    ordering = ('last_name', 'first_name', 'phone_number')
