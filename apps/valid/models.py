from __future__ import unicode_literals
from django.db import models
import re

emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class EmailValid(models.Manager):
	def validation(self, email):
		if emailRegex.match(email):
			User.objects.create(email=email)
			return True
		else:
			return False
		

class User(models.Model):
	email = models.CharField(max_length=30)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = EmailValid()
