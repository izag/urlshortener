from django.conf import settings


def global_settings(request):
	# return any necessary values
	return {
		'SITE_URL': settings.SITE_URL,
	}