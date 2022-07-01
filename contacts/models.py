from django.db import models
from django.forms import ModelForm

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(blank=True, max_length=10)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)

    def __str__(self) -> str:
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
