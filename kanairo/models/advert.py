from django.conf import settings
from django.db import models


class Advert(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="adverts"
    )

    title = models.CharField(max_length=4096)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="images/")

    class Meta:
        verbose_name = "Advert"
        verbose_name_plural = "Adverts"

    def __str__(self):
        return self.title
