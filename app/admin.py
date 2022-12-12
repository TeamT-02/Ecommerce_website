from django.contrib import admin
from app.models import *


admin.site.register(Category),
admin.site.register({Sub_Category, Product}),
admin.site.register({Contact_us, Order, Brand}),
# Register your models here.
