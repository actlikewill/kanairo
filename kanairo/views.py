from django.views.generic import DetailView, ListView

from .models import Advert


class AdvertListView(ListView):
    """The advert list view."""

    model = Advert
    template_name = "kanairo/advert_list.html"
    context_object_name = "adverts"


class AdvertDetailView(DetailView):
    """The advert detail view."""

    model = Advert
    template_name = "kanairo/advert_detail.html"
    context_object_name = "advert"
