from django.conf.urls import url
from . import views

# Must include links to the
urlpatterns = [
    url(r'by_title$', views.sort_by_title),
    url(r'by_categ', views.sort_by_categ),
    url(r'create', views.create),
    url(r'process_auc', views.process_new_auc),
    url(r'process_med', views.process_new_media),
    url(r'add_media', views.add_media),
    url(r'view_auc/(?P<id>\d+)', views.view_auc, name="place_bid"),
    url(r'add_bid', views.add_bid),
    url(r'$', views.index),
]


