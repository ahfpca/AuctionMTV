from django.conf.urls import url
from . import views

# Must include links to the
urlpatterns = [
    url(r'^$', views.index),
    url(r'^auction/by_title', views.sort_by_title),
    url(r'^auction/by_categ', views.sort_by_categ),
    url(r'^auction/create', views.create),
    url(r'^auction/process_auc', views.process_new_auc),
    url(r'^auction/process_med', views.process_new_media),
    # url(r'^auction/generate_form', views.generate_form)
    # url(r'^auction/media_form.html', views.media_form_html)
]