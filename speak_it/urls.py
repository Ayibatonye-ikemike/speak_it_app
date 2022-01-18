from django.urls import path
from. import views


urlpatterns = [path('', views.translate_app, name = 'trans')]