from django.urls import path
from . import views
# when it comes from url of crm here then it triggers these 3 function which takes us to views file
urlpatterns = [
    # base url
    path('', views.home, name="home"),
    # other pages
    path('products/', views.products,name='products'),
    # <str:pk_tests>/ added this for dynamic url routing i.e we can find customer by id i.e /customer/4/
    path('customer/<str:pk_test>/', views.customer,name="i"),
    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
     path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
]
