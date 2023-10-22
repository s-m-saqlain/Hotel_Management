""" AdminSite Registeration For Admin Panel """
from django.contrib import admin
from .models import Admin, Room, RoomImages, Customer, Booking, SliderImage

# Register your models here.

admin.site.register(Admin)
admin.site.register(Room)
admin.site.register(RoomImages)
admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(SliderImage)
