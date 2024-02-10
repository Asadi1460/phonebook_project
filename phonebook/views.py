from django.http import HttpResponse
from django.shortcuts import render
from .models import Phonebook
from django.db.models import Q


def add_contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        Phonebook.objects.create(first_name=first_name, last_name=last_name, phone_number=phone_number)
        return HttpResponse('Contact added successfully! <br><a href="/phonebook/">Phonebook</a>')
    else:
        return render(request, 'phonebook/add_contact.html')


def search_contact(request):
    query = request.GET.get('query', '')
    contacts = []
    if query:
        contacts = Phonebook.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(phone_number__icontains=query)
        )
    return render(request, 'phonebook/search_contact.html', {'query': query, 'contacts': contacts})


def contact_list(request):
    contacts = Phonebook.objects.all()
    return render(request, 'phonebook/contact_list.html', {'contacts': contacts})


def edit_contact(request, contact_id):
    contact = Phonebook.objects.get(pk=contact_id)
    if request.method == 'POST':
        contact.first_name = request.POST.get('first_name')
        contact.last_name = request.POST.get('last_name')
        contact.phone_number = request.POST.get('phone_number')
        contact.save()
        return HttpResponse('Contact updated successfully! <br><a href="/phonebook/">Phonebook</a>')

    else:
        return render(request, 'phonebook/edit_contact.html', {'contact': contact})


def delete_contact(request, contact_id):
    contact = Phonebook.objects.get(pk=contact_id)
    if request.method == 'POST':
        # If the user confirms the deletion, delete the contact
        contact.delete()
        return HttpResponse('Contact deleted successfully! <br><a href="/phonebook/">Phonebook</a>')
    else:
        # If the request method is not POST, render a confirmation page
        return render(request, 'phonebook/confirm_delete.html', {'contact': contact})
