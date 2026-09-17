from uuid import uuid4

from django.conf import settings
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction
from django.contrib.auth.models import User
from django.db.models import Q, Prefetch
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
from django.core.mail import send_mail
from django.contrib import messages

from catalog.models import Category, Product
from content.models import Page, Contact, Vacancy, Review, Benefit, AboutHome, Slider
from faq.models import CategoryFaq, QuestionFaq


class HomePage(View):
    def get(self, request):
        context = {
            "benefits": Benefit.objects.all(),
            "about": AboutHome.objects.first(),
            "categories": Category.objects.all().order_by("order"),
            "slider": Slider.objects.all().order_by("order"),
            "products": Product.objects.all(),
        }
        return render(request, 'home.html', context=context)


class PageView(View):
    def get(self, request, **kwargs):
        page = get_object_or_404(Page, slug=kwargs.get('slug'))

        context = {
            'page': page
        }

        if page.type == 'faq':
            faq_categories = CategoryFaq.objects.all().order_by('order').prefetch_related(
                Prefetch('questions', queryset=QuestionFaq.objects.all().order_by('order'))
            )
            context['faq_categories'] = faq_categories

        if page.type == 'contacts':
            context['contacts'] = Contact.objects.all().order_by('order')

        if page.type == 'career':
            context['vacancies'] = Vacancy.objects.all().order_by('order')

        if page.type == 'reviews':
            context['reviews'] = Review.objects.all().order_by('published_at')

        return render(request, 'page.html', context=context)


class ApplicationView(View):
    pass


class ArticlePage(View):
    pass
