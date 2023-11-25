from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    categoryN = models.CharField(max_length=100)

    def __str__(self):
        return self.categoryN



class Listing(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    starting_bid = models.FloatField()
    url = models.CharField(max_length=300, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")

class Watchlist(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    url = models.CharField(max_length=300, blank=True)
    bid = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user1")

class Bids(models.Model):
    title = models.CharField(max_length=300, default=0)
    bids = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user2")

    def __str__(self):
        return self.title

class Comments(models.Model):
    comment = models.CharField(max_length=300, default=None)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user3")
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.comment
