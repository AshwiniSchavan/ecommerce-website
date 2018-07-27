from . import views
from django.conf.urls import url

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^contact_page/$', views.contact_page, name='contact_page'),
]