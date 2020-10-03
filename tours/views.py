from django.shortcuts import render
from django.views import View


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name='tours/index.html')


class DepartureView(View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name='tours/departure.html')


class TourView(View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name='tours/tour.html')


def page_not_found_view(request, exception):
    return render(request=request, template_name='tours/error.html', status=404, context={'code': '404'})


def error_view(request):
    return render(request=request, template_name='tours/error.html', status=500, context={'code': '500'})
