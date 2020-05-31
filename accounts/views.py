from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.forms import inlineformset_factory
from .forms import OrderForm
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
def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {'customer':customer,'orders':orders,'order_count':order_count}
    return render(request,'accounts/customer.html',context)

def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('product','status'))
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(instance=customer)
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        #print('Printing POST:',request.POST)
        # before creating formset wala line form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset':formset}
    return render(request,'accounts/order_form.html',context)

def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        #print('Printing POST:',request.POST) we pass instance for updating order otherwise it would create new order
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'accounts/order_form.html',context)
#primary key as we want to delete particular item
def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context={'item':order}
    return render(request,'accounts/delete.html',context)
