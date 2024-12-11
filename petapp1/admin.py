from django.contrib import admin
from .models import PetUser, Pet, Product

# Register your models here.
admin.site.site_header = 'Kalyanis Pet Store'
admin.site.site_title = 'My Pet Store'
admin.site.register(PetUser)
admin.site.register(Pet)
admin.site.register(Product)
