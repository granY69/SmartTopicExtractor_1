from django.urls import path
from . import views

urlpatterns = [
    path('', views.root, name="root_url"),
    path('textinput/', views.textinput, name="textinput_url"),
    path('inputread/', views.read, name='inputread_url'),
    path('uploadfile/', views.uploadfile, name="uploadfile_url"),
    path('about/', views.about, name="about_url"),
    path('contact/', views.contact, name="contact_url")
    ]