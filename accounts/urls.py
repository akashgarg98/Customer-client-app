from django.urls import path
from . import views
# when it comes from url of crm here then it triggers these 3 function which takes us to views file
urlpatterns = [
    # base url
    path('', views.home),
    # other pages
    path('products/', views.products),
    # <str:pk_tests>/ added this for dynamic url routing i.e we can find customer by id i.e /customer/4/
    path('customer/<str:pk_test>/', views.customer),
]
