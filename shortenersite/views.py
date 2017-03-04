from django.shortcuts import render_to_response, get_object_or_404, render, redirect
import random, string, json
from shortenersite.models import Urls
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.template.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from django.urls import reverse_lazy

class IndexView(generic.ListView):
	template_name = 'shortenersite/index.html'
	context_object_name = 'popular_urls'

	def get_queryset(self):
		"""Return the most popular 20 urls."""
		return Urls.objects.all()[:20]

class DetailView(generic.DetailView):
	model = Urls
	context_object_name = 'current_url'
	template_name = 'shortenersite/details.html'

def redirect_original(request, short_id):
	url = get_object_or_404(Urls, pk = short_id)
	url.count += 1
	url.save()
	return HttpResponseRedirect(url.httpurl)

def shorten_url(request):
	url = request.POST.get("url", '')

	if url == '':
		from django.contrib import messages
		messages.warning(request, "Url field is empty. Nothing to shorten.")
		return redirect('shortenersite:home')

	short_id = get_short_code()
	b = Urls(httpurl = url, short_id = short_id)
	b.save()

	return redirect(b)

def get_short_code():
	length = Urls._meta.get_field('short_id').max_length
	char = string.ascii_uppercase + string.digits + string.ascii_lowercase

	# if the randomly generated short_id is used then generate next
	while True:
		short_id = ''.join(random.choice(char) for x in range(length))
		try:
			temp = Urls.objects.get(pk = short_id)
		except:
			return short_id

class UrlsListView(generic.ListView):
	context_object_name = 'urls'
	template_name = 'shortenersite/list.html'

	def get_queryset(self):
		urls = Article.objects.all()
		paginator = Paginator(urls, 10)
		page = self.request.GET.get('page')

		try:
			urls = paginator.page(page)
		except PageNotAnInteger:
			urls = paginator.page(1)
		except EmptyPage:
			urls = paginator.page(paginator.num_pages)

		return urls


class DeleteView(generic.DeleteView):
	model = Urls
	success_url = reverse_lazy('home')