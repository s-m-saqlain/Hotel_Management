""" Database For Hotel Management System """

import uuid
from django.db import models


class BaseModel(models.Model):
    """BaseModel Using Inheritance And Abstraction For ID Field"""

    id = models.UUIDField(
        default=uuid.uuid4, editable=False, auto_created=True, primary_key=True
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        """It's abstract the BaseModel so the BaseModel table Should not be created in DataBase"""

        abstract = True

    def __str__(self):
        return str(self.id)


class Admin(BaseModel):
    """AdminTable Where Email is Unique"""

    user_name = models.CharField(max_length=50, default="")
    full_name = models.CharField(max_length=25, default="")
    image = models.ImageField(upload_to="admin/",default="admin/dummy.png")
    email = models.EmailField(max_length=50, unique=True)
    password = models.TextField(null=False)

    def __str__(self):
        return str(self.email)


class Room(BaseModel):
    """RoomTable Where Room Number and Price"""

    choise = (("available", "available"), ("booked", "booked"))
    room_number = models.CharField(max_length=10, unique=True, default="")
    room_type = models.CharField(max_length=50, default="")
    price = models.CharField(max_length=20, default="")
    description = models.TextField(default="")
    status = models.CharField(choices=choise, default="available", max_length=50)
    image = models.ImageField(upload_to="room/", default="room/dummy.png")

    def __str__(self):
        return str(self.room_number)


class RoomImages(BaseModel):
    """Table For RoomImages"""

    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="roomimages/", default="")


class Customer(BaseModel):
    """Table For Customer Where FirstName And LastName"""

    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="customer/", default="customer/dummy.png")
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=250, default="")
    phone = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return str(self.email)


class Booking(BaseModel):
    """Booking Table Where Booking Detail of Specific Room is Sadfe"""

    choise = (("paid", "paid"), ("unpaid", "unpaid"))
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, blank=True, null=True
    )
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    chech_in_date = models.CharField(max_length=50, default="")
    chech_out_date = models.CharField(max_length=50, default="")
    payment_status = models.CharField(choices=choise, default="unpaid", max_length=50)
    customer_feedback = models.TextField()


class SliderImage(BaseModel):
    """Admin Can add Slider Images"""

    title = models.CharField(max_length=50, default="")
    description = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="slider/", default="")
