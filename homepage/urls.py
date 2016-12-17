from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^Learning_Python$', views.Learning_Python, name='Learning_Python'),
    url(r'^resources$', views.resources, name='resources'),
    url(r'^podcast$', views.podcast, name='podcast'),
    url(r'^books$', views.books, name='books'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^', views.index, name='index'),
]
