from django.urls import path
from . import views
# when it comes from url of crm here then it triggers these 3 function which takes us to views file
urlpatterns = [
    # base url
    path('', views.home),
    # other pages
    path('products/', views.products),
    path('customer/', views.customer),
]
