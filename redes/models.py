from django.db import models
from django.utils import timezone

class Red(models.Model):
	name=models.CharField(max_length=100)
	admin=models.ForeignKey('auth.User')
	description=models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	is_active=models.BooleanField(default=True)

	def __str__(self):
		return self.name

	def deactivate(self):
		self.is_active=False
		self.save()

	def activate(self):
		self.is_active=True
		self.save()


class Post(models.Model):
	author=models.ForeignKey('auth.User')
	title=models.CharField(max_length=50)
	text=models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	publish_date=models.DateTimeField(blank=True,null=True)
	redes=models.ManyToManyField('Red')

	def __str__(self):
		return self.title
	def publish(self):
		self.publish_date=timezone.now()
		self.save()