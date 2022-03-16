from django.shortcuts import render
from django.views.generic import ListView

from .models import Product


class HomeView(ListView):
    model = Product
    template_name = 'market/home.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
                'products_for_men': Product.objects.filter(gender='M'),
                'products_for_women': Product.objects.filter(gender='F'),
                'accessories': Product.objects.filter(category='Accessories')

        })

    def get_queryset(self):
        return Product.objects.filter(gender='N')
