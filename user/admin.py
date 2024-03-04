from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'district', 'city', 'state', 'number']
    list_filter = ['email', 'name', 'district', 'city', 'state', 'number']
    
    search_fields = ['email', 'name', 'district', 'city', 'state', 'number']

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['user_email', 'booked', 'area', 'floor',  'city', 'bedrooms', 'kitchen', 'hall', 'cost', 'balcany', 'date']
    list_filter = ['user_email', 'area', 'floor',  'city', 'bedrooms', 'kitchen', 'hall', 'cost', 'balcany', 'date']
      
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['user_email', 'booked', 'dimention', 'district', 'city', 'cost', 'bedrooms', 'kitchen', 'hall', 'balcany', 'date']
    list_filter = ['user_email', 'dimention', 'district', 'city', 'cost', 'bedrooms', 'kitchen', 'hall', 'balcany', 'date']
    
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer', 'house', 'room', 'booked', 'date']

# admin.site.register(User)
# admin.site.register(House)
# admin.site.register(Room)
admin.site.register(Contact)
# admin.site.register(Booking)