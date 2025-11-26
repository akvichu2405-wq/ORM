# Ex01 Django ORM Web Application
## Date: 26/11/2025
## AIM
To develop a Django Application to store and retrieve data from a E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Amazon,AmazonAdmin
admin.site.register(Amazon,AmazonAdmin)

models.py

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
```


## OUTPUT
![alt text](<Screenshot 2025-11-26 180922.png>)


## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully
