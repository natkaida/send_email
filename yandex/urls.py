from django.urls import path
from django.contrib import admin
from .views import ContactView, ContactSuccessView

app_name = 'yandex'

urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
    path('success/', ContactSuccessView.as_view(), name='success'),
]