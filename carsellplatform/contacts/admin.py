from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'car_title', 'city', 'created_date')
    list_display_links = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email', 'car_title')
    list_per_page = 20
    
admin.site.register(Contact, ContactAdmin)
