from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
#returns http response
#def home(request):
 #   return HttpResponse('home')

 #render templatesby from django.shortcut.....
# after step1 of product modify this home
#1.def home(request):
   # return render(request,'accounts/dashboard.html')
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    total_customer = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status = "delivered").count()
    pending = orders.filter(status = "pending").count()
    context = {'orders':orders,'customers':customers,'delivered':delivered,'pending':pending,'total_orders':total_orders}

    return render(request,'accounts/dashboard.html',context)
#def products(request):
 #   return HttpResponse('products')

#def customer(request):
    #return HttpResponse('customer')

#def products(request):
 #   return render(request,'accounts/products.html')
# 1.this step when making queries {'products':products} we can use 'list' or anything inside it but use the same as usedin products.html in loop
def products(request):
    products = Product.objects.all()
    return render(request,'accounts/products.html',{'products':products})
def customer(request):
    return render(request,'accounts/customer.html')


