from django.conf.urls import url

from . import views


app_name = 'shortenersite'
urlpatterns = [
    url(r'^$', views.index, name='home'),

    url(r'^(?P<short_id>\w{6})$', views.redirect_original, name='redirectoriginal'),

    url(r'^makeshort/$', views.shorten_url, name='shortenurl'),
]