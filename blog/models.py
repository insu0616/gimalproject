from django.db import models
from django.conf import settings


class Category(models.Model):
    category = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category

class Shop(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=200)
    number = models.IntegerField()
    address = models.TextField()
    introduction = models.TextField()
    view = models.IntegerField(default=0)
    photo1 = models.FileField()
    photo2 = models.FileField(blank = True, null = True)
    photo3 = models.FileField(blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    shop = models.ForeignKey(Shop)
    commenter = models.ForeignKey(settings.AUTH_USER_MODEL)
    comment = models.TextField()
    photo1 = models.FileField(blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



