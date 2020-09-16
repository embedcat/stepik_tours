from django.views.generic import ListView
from tours.models import DummyModel


class MainView(ListView):
    template_name = 'tours/index.html'
    model = DummyModel


class DepartureView(ListView):
    template_name = 'tours/departure.html'
    model = DummyModel


class TourView(ListView):
    template_name = 'tours/tour.html'
    model = DummyModel
