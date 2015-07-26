from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^mission/$', views.mission, name='mission'),
    url(r'^services/$', views.services, name='services'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^contact/$', views.contact, name='contact'),

    url(r'^what-we-do/$', views.whatwedo, name='whatwedo'),
    url(r'^how-we-work/$', views.howwework, name='howwework'),
    url(r'^where-we-work/$', views.wherewework, name='wherewework'),
    url(r'^get-involved/$', views.getinvolved, name='getinvolved'),
]