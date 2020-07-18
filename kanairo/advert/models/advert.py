from django.db import models
from django.conf import settings
from .category import Category
from taggit.managers import TaggableManager

def upload_status_image(instance, filename):
    return "status/{user}/{filename}".format(user=instance.user, filename=filename)

class Advert(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to=upload_status_image)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = TaggableManager()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
