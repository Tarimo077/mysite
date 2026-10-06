"""
URL configuration for mysite project.
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('resume/', views.resume_view, name='resume'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('sitemap.xml', views.sitemap_xml, name='sitemap_xml'),
]
