from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from lend. models import *


from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Book.CATEGORY_CHOICE
        context['categories'] = {category[0]: Book.objects.filter(category=category[0]) for category in categories}
        return context