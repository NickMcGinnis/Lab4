from django.urls import path

from . import views

app_name = 'contacts'
urlpatterns = [
    path('', views.ContactList.as_view(), name='contact_list'),
    path('<int:pk>', views.ContactDetail.as_view(), name='contact_detail'),
    path('create', views.ContactCreate.as_view(), name='contact_create'),
    path('update/<int:pk>', views.ContactUpdate.as_view(), name='contact_update'),
    path('delete/<int:pk>', views.ContactDelete.as_view(), name='contact_delete'),
]
