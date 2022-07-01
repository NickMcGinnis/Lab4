from multiprocessing import context
from re import I, template
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from contacts.models import Contact, ContactForm
# Create your views here.


def index(request):
    contacts_list = Contact.objects.order_by('-name')[:10]
    context = {'contacts_list': contacts_list}
    return render(request, 'contacts/index.html', context)


def detail(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'contacts/detail.html', {'contact': contact})


def add(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contacts')
    else:
        form = ContactForm

    return render(request, 'contacts/add.html', {'form': form})
