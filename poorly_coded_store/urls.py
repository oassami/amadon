from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('checking_out/<int:product_id>', views.checking_out),
    path('checkout/<int:order_id>', views.checkout),
]
