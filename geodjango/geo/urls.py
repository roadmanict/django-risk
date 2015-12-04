from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^api/get_country/(-?\d+\.\d+)/(-?\d+\.\d+)/$', views.get_country),
    url(r'^api/get_random_country_name', views.get_random_country_name),
    url(r'^api/get_countries_in_rectangle/(-?\d+\.\d+)/(-?\d+\.\d+)/(-?\d+\.\d+)/(-?\d+\.\d+)/',
        views.get_countries_in_rectangle),
    url(r'^api/get_markers', views.get_markers),
]
