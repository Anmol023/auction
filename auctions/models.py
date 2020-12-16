from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class AuctionList(models.Model):
	title = models.CharField(max_length=64)
	description = models.TextField()
	price = models.IntegerField()
	category = models.CharField(max_length=64)
	link = models.CharField(max_length=64, blank=True, null=True)

class Bid(models.Model):
	title = models.CharField(max_length=64)
	bamount = models.IntegerField()
	listid = models.IntegerField()
	user = models.CharField(max_length=64)

class Comments(models.Model):
	user = models.CharField(max_length=64)
	comment = models.TextField()
	listid = models.IntegerField()



