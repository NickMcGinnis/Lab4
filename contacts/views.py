from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from contacts.models import Contact
from django.shortcuts import render
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, ButtonHolder
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

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.form_method = "post"
        form.helper.add_input(
            Submit('submit', 'Submit', css_class="button is_success"))
        return form


class ContactUpdate(UpdateView):
    model = Contact
    template_name = 'contacts/contact_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('contacts:contact_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.form_method = "post"
        form.helper.add_input(
            Submit('submit', 'Submit', css_class="button is_success"))
        return form


class ContactDelete(DeleteView):
    model = Contact
    template_name = 'contacts/contact_confirm_delete.html'

    def get_success_url(self):
        return reverse('contacts:contact_list')
