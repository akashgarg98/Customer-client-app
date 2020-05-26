from django.contrib import admin

# Register your models here.
# now after running python manage.py makemigrations and python maange.py migration we need to register table of customer in this admin.py i.e admin panel of our app
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)