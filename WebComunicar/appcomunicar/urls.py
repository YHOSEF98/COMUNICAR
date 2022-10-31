from django.urls import path

from . import views

urlpatterns = [
    path("", views.index,name="index"),
    path("contacto/", views.contacto, name="contacto"),
    path("blog/", views.blog, name="blog"),
    path("servicios/", views.servicios, name="servicios"),
    path("careers/", views.careers, name="careers"),
    path("single/", views.about, name="single"),
    path("about/", views.about, name="about"),
]