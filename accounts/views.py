from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#returns http response
#def home(request):
 #   return HttpResponse('home')

 #render templatesby from django.shortcut.....
def home(request):
    return render(request,'accounts/dashboard.html')

#def products(request):
 #   return HttpResponse('products')

#def customer(request):
    #return HttpResponse('customer')

def products(request):
    return render(request,'accounts/products.html')
def customer(request):
    return render(request,'accounts/customer.html')


