from django.shortcuts import render, get_object_or_404
from django.views import View

from catalog.models import Category, Style, Color, Product
from content.models import Benefit


class CatalogView(View):
    def get(self, request):

        context = {
            "categories": Category.objects.all().order_by('order'),
            "styles": Style.objects.all().order_by('order'),
        }

        return render(request, template_name='catalog.html', context=context)


class CategoryView(View):
    def get(self, request, **kwargs):
        category = get_object_or_404(Category, slug=kwargs.get('slug'))

        context = {
            "category": category,
            "colors": Color.objects.all().order_by('title'),
            "products": category.products.all().order_by('order'),
        }

        return render(request, template_name='category.html', context=context)


class StyleView(View):
    def get(self, request, **kwargs):
        style = get_object_or_404(Style, slug=kwargs.get('slug'))

        context = {
            "style": style,
            "colors": Color.objects.all().order_by('title'),
            "products": style.products.all().order_by('order'),
        }

        return render(request, template_name='style.html', context=context)


class ProductView(View):
    def get(self, request, **kwargs):
        product = get_object_or_404(Product, slug=kwargs.get('slug'))

        context = {
            "product": product,
            "benefits": Benefit.objects.all(),
        }

        return render(request, template_name='product.html', context=context)
