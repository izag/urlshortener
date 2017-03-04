from __future__ import unicode_literals

from django.db import models

class Urls(models.Model):
	short_id = models.SlugField(max_length = 6, primary_key = True)
	httpurl = models.URLField(max_length = 200)
	pub_date = models.DateTimeField(auto_now_add = True)
	count = models.IntegerField(default = 0)

	def __str__(self):
		return self.httpurl

	def get_absolute_url(self):
		from django.urls import reverse
		return reverse('shortenersite:details', kwargs={'pk': self.short_id})

	class Meta:
		ordering = ["-count", "-pub_date"]