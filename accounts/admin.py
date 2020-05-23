from django.contrib import admin

# Register your models here.
# now after running python manage.py makemigrations and python maange.py migration we need to register table of customer inthis admin
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)