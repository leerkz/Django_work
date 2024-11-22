from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('catalog/', views.catalog, name='catalog'),  # Каталог
    path('category/', views.category, name='category'),  # Категории
    path('contacts/', views.contacts, name='contacts'),  # Категории
]