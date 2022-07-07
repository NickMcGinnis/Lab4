from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from contacts.models import Contact
from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'contacts/index.html')


def help(request):
    return render(request, 'contacts/help.html')


class ContactList(ListView):
    model = Contact
    template_name = 'contacts/contact_list.html'


class ContactDetail(DetailView):
    model = Contact
    template_name = 'contacts/contact_details.html'


class ContactCreate(CreateView):
    model = Contact
    template_name = 'contacts/contact_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('contacts:contact_list')


class ContactUpdate(UpdateView):
    model = Contact
    template_name = 'contacts/contact_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('contacts:contact_list')


class ContactDelete(DeleteView):
    model = Contact
    template_name = 'contacts/contact_confirm_delete.html'

    def get_success_url(self):
        return reverse('contacts:contact_list')
