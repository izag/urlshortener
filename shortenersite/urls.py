from django.conf.urls import url

from . import views


app_name = 'shortenersite'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='home'),

	url(r'^all/$', views.UrlsListView.as_view(), name='listall'),

	url(r'^(?P<short_id>\w{6})$', views.redirect_original, name='redirectoriginal'),

	url(r'^details/(?P<pk>\w{6})$', views.DetailView.as_view(), name='details'),

	url(r'^delete/(?P<pk>\w{6})$', views.DeleteView.as_view(), name='delete_url'),

	url(r'^makeshort/$', views.shorten_url, name='shortenurl'),
]