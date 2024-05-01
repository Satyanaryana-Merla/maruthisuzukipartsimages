from django.db import models # type: ignore
import datetime
from django.core.validators import RegexValidator
import re
from django.core.exceptions import ValidationError   

from django.db import models

class CarModel(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class MakingYear(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.car_model} - {self.year}"

class Variant(models.Model):
    making_year = models.ForeignKey(MakingYear, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.making_year} - {self.name}"


def validate_part_id(value):
    pattern = r'^[A-Z0-9]+$'
    if not re.match(pattern, value):
        raise ValidationError('Part ID must contain only uppercase letters (A-Z) and digits (0-9).')

#product
class Products(models.Model):
    part_ID = models.CharField(max_length=50, validators=[validate_part_id])
    Part_name = models.CharField(max_length=50)
    productDetails = models.CharField(max_length=500)
    Compatibility = models.CharField(max_length=500)
    Price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to='uploads/product')

    variants = models.ManyToManyField('Variant', related_name='products')

    def save(self, *args, **kwargs):
        # Convert Part_name to uppercase before saving
        self.Part_name = self.Part_name.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.part_ID



#customers
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.first_name}{self.lastname}'



#Order
class Orders(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default="", blank=True)
    phone = models.CharField(max_length=13, default="",blank=True)
    date =models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.product