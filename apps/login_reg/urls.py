from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'confirm$', views.confirm),
    url(r'logout$', views.logout),
    url(r'success$', views.success),
    url(r'sign_up$', views.sign_up),
    url(r'register$', views.register),
    url(r'$', views.index),
]






