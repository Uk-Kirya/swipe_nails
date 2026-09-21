from typing import Any

from django.contrib.auth.models import User, Group
from django.http import HttpRequest

from content.models import Page, SocialNetwork, PaymentMethods, Vacancy, Contact, Review, Benefit, Slider
from catalog.models import Category, Style, Color, Product, AccessoriesCategory, Video
from faq.models import CategoryFaq, QuestionFaq
from instructions.models import InstructionCard, QuestionInstruction, ExpertAdvice


def context_all(request: HttpRequest) -> dict[str, Any]:

    context = {
        'pages': Page.objects.all().order_by('order'),
        'socials': SocialNetwork.objects.all(),
        'payment_methods': PaymentMethods.objects.all(),
    }

    return context


def admin_stats(request):
    if request.path.startswith('/admin/'):
        return {
            'categories_count': Category.objects.count(),
            'styles_count': Style.objects.count(),
            'colors_count': Color.objects.count(),
            'product_count': Product.objects.count(),
            'acessories_count': AccessoriesCategory.objects.count(),
            'categoriesfaq_count': CategoryFaq.objects.count(),
            'questions_count': QuestionFaq.objects.count(),
            'pages_count': Page.objects.count(),
            'vacancies_count': Vacancy.objects.count(),
            'contacts_count': Contact.objects.count(),
            'payments_count': PaymentMethods.objects.count(),
            'reviews_count': Review.objects.count(),
            'videos_count': Video.objects.count(),
            'benefits_count': Benefit.objects.count(),
            'sliders_count': Slider.objects.count(),
            'socials_count': SocialNetwork.objects.count(),
            'groups_count': Group.objects.count(),
            'users_count': User.objects.count(),
            'instructioncards_count': InstructionCard.objects.count(),
            'questioninstructions_count': QuestionInstruction.objects.count(),
            'expertadvices_count': ExpertAdvice.objects.count(),
        }
    return {}
