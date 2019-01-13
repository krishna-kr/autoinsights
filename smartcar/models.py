from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class FeedbackData(models.Model):
	user=models.ForeignKey(User)
	name=models.CharField(max_length=255,blank=True,null=True)
	email=models.CharField(max_length = 255,blank=True,null=True)
	mobile=models.CharField(max_length = 255,blank=True,null=True)
	message=models.CharField(max_length = 255,blank=True,null=True)
	request_date=models.DateField(("Date"), default=datetime.date.today)

	def __str__(self):
		return self.email

