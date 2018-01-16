from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about$', views.about, name='about'),

    url(r'^UK$', views.UK, name='UK'),
    url(r'^UK_pie$', views.UK_pie, name='UK_pie'),
    url(r'^UK_AS$', views.UK_AS, name='UK_AS'),
    url(r'^UK_table$', views.UK_table, name='UK_table'),

    url(r'^DE$', views.DE, name='DE'),
    url(r'^DE_pie$', views.DE_pie, name='DE_pie'),
    url(r'^DE_AS$', views.DE_AS, name='DE_AS'),
    url(r'^DE_table$', views.DE_table, name='DE_table'),
]