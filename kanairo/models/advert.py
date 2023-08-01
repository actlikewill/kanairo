from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Advert(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="adverts"
    )

    title = models.CharField(max_length=4096)
    slug = models.SlugField(max_length=4096, blank=True)

    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    class Meta:
        verbose_name = "Advert"
        verbose_name_plural = "Adverts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("advert_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
