# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Comment(models.Model):
	name = models.CharField(max_length=20)
	message = models.CharField(max_length=100)

	def __str__(self):
		return self.name
	def __unicode__(self):
		return self.name
class Comment_for_nightmarket(models.Model):
	name = models.CharField(max_length=20)
	nightmarket_name = models.CharField(max_length=20)
	message = models.CharField(max_length=100)

	def __str__(self):
		return self.name
	def __unicode__(self):
		return self.name