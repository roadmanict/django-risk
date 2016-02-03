from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

from geo import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^municipalities/$', views.MunicipalityList.as_view()),
    url(r'^municipalities/(?P<pk>[0-9]+)/$',
        views.MunicipalityDetail.as_view()),
    url(r'^municipalities/(?P<pk>[0-9]+)/adjacent$',
        views.AdjacentList.as_view()),
    url(r'^municipalities/(?P<pk>[0-9]+)/adjacent/(?P<to>[0-9]+)/$',
        views.IsAdjacent.as_view()),
    url(r'^municipality_owners/$', views.MunicipalityOwnerList.as_view()),
    url(r'^municipality_owners/(?P<pk>[0-9]+)/$',
        views.MunicipalityOwnerDetail.as_view()),
    url(r'^games/$', views.GameList.as_view()),
    url(r'^games/(?P<pk>[0-9]+)/$',
        views.GameDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view()),
    url(r'^auth/', include('rest_framework.urls',
        namespace='rest_framework')),
    url(r'^auth/token/$', obtain_auth_token)
]

urlpatterns = format_suffix_patterns(urlpatterns)
