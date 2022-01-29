from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.portfolio, name="portfolio"),
    path("wallets/", views.wallets, name="wallets"),
    path("transactions/", views.transactions, name="transactions"),
]

