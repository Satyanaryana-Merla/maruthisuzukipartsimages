from django.contrib import admin # type: ignore
from django.contrib import admin
from .models import CarModel, Customer, Products, Orders, Variant, MakingYear

admin.site.register(CarModel)
admin.site.register(MakingYear)
admin.site.register(Variant)
# admin.site.register(Customer)
admin.site.register(Products)
# admin.site.register(Orders)


