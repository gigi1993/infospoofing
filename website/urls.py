from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about$', views.about, name='about'),
    url(r'^remediation', views.remediation, name='remediation'),

    url(r'^au$', views.AU, name='AU'),
    url(r'^AU_pie$', views.AU_pie, name='AU_pie'),
    url(r'^AU_AS$', views.AU_AS, name='AU_AS'),
    url(r'^AU_table$', views.AU_table, name='AU_table'),

    url(r'^de$', views.DE, name='DE'),
    url(r'^DE_pie$', views.DE_pie, name='DE_pie'),
    url(r'^DE_AS$', views.DE_AS, name='DE_AS'),
    url(r'^DE_table$', views.DE_table, name='DE_table'),

    url(r'^it$', views.IT, name='IT'),
    url(r'^IT_pie$', views.IT_pie, name='IT_pie'),
    url(r'^IT_AS$', views.IT_AS, name='IT_AS'),
    url(r'^IT_table$', views.IT_table, name='IT_table'),

    url(r'^nl$', views.NL, name='NL'),
    url(r'^NL_pie$', views.NL_pie, name='NL_pie'),
    url(r'^NL_AS$', views.NL_AS, name='NL_AS'),
    url(r'^NL_table$', views.NL_table, name='NL_table'),

    url(r'^pl$', views.PL, name='PL'),
    url(r'^PL_pie$', views.PL_pie, name='PL_pie'),
    url(r'^PL_AS$', views.PL_AS, name='PL_AS'),
    url(r'^PL_table$', views.PL_table, name='PL_table'),

    url(r'uk$', views.UK, name='UK'),
    url(r'^UK_pie$', views.UK_pie, name='UK_pie'),
    url(r'^UK_AS$', views.UK_AS, name='UK_AS'),
    url(r'^UK_table$', views.UK_table, name='UK_table'),
]