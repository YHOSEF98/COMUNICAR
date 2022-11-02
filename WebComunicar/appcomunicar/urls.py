from django.urls import path
from rest_framework import routers

from . import views
#from .viewsets import ClienteViewSet

#router = routers.SimpleRouter()
#router.register('cliente', ClienteViewSet)

urlpatterns = [
    path("", views.index,name="index"),
    path("contacto/", views.contacto, name="contacto"),
    path("blog/", views.blog, name="blog"),
    path("servicios/", views.servicios, name="servicios"),
    path("careers/", views.careers, name="careers"),
    path("single/", views.about, name="single"),
    path("about/", views.about, name="about"),
]

