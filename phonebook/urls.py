from django.urls import path

from phonebook.views import delete_contact, contact_list, edit_contact, search_contact, add_contact

urlpatterns = [
    path('', contact_list, name='contact_list'),
    path('add_contact/', add_contact, name='add_contact'),
    path('search_contact/', search_contact, name='search_contact'),
    path('edit_contact/<int:contact_id>/', edit_contact, name='edit_contact'),
    path('delete_contact/<int:contact_id>/', delete_contact, name='delete_contact'),
]
