from django.urls import path

app_name = 'catalog'

from .views import CatalogView, CategoryView, StyleView, ProductView

urlpatterns = [
    path('', CatalogView.as_view(), name='catalog'),
    path('<slug:slug>', ProductView.as_view(), name='product'),
    path('categories/<slug:slug>/', CategoryView.as_view(), name='category'),
    path('styles/<slug:slug>/', StyleView.as_view(), name='style'),
]
