from django.db import models
from django.contrib import admin
class Amazon (models.Model):
    ProductName=models.CharField(max_length=40)
    SerialNumber=models.IntegerField()
    Brand=models.CharField()
    Price=models.IntegerField()
    ManufacturingDate=models.DateField()
    ExpiryDate=models.DateField()
    Rating=models.IntegerField()

class AmazonAdmin(admin.ModelAdmin):
    list_display=('ProductName','SerialNumber','Brand','Price','ManufacturingDate','ExpiryDate','Rating')
