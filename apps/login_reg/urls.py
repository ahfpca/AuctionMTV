from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'confirm$', views.confirm),
    url(r'edit$', views.edit),
    url(r'update$', views.update),
    url(r'logout$', views.logout),
    # url(r'login$', views.login),
    url(r'signup$', views.sign_up),
    url(r'register$', views.register),
    url(r'$', views.index),
]






