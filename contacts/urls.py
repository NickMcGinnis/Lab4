from django.urls import path

from . import views

app_name = 'contacts'
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('<int:contact_id>/', views.detail, name='detail')
]
