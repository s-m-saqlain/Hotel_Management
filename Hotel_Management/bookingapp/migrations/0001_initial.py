# Generated by Django 4.2.3 on 2023-10-22 10:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Admin",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        auto_created=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("user_name", models.CharField(default="", max_length=50)),
                ("full_name", models.CharField(default="", max_length=25)),
                ("email", models.EmailField(max_length=50, unique=True)),
                ("password", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        auto_created=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("first_name", models.CharField(default="", max_length=50)),
                ("last_name", models.CharField(default="", max_length=50)),
                (
                    "image",
                    models.ImageField(
                        default="customer/dummy.png", upload_to="customer/"
                    ),
                ),
                ("email", models.EmailField(max_length=50, unique=True)),
                ("password", models.CharField(default="", max_length=250)),
                ("phone", models.CharField(default="", max_length=20)),
                ("address", models.CharField(max_length=30, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        auto_created=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "room_number",
                    models.CharField(default="", max_length=10, unique=True),
                ),
                ("room_type", models.CharField(default="", max_length=20)),
                ("price", models.CharField(default="", max_length=20)),
                ("description", models.CharField(default="", max_length=50)),
                (
                    "status",
                    models.CharField(
                        choices=[("available", "available"), ("booked", "booked")],
                        default="available",
                        max_length=50,
                    ),
                ),
                (
                    "image",
                    models.ImageField(default="room/dummy.png", upload_to="room/"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SliderImage",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        auto_created=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("title", models.CharField(default="", max_length=50)),
                ("description", models.CharField(default="", max_length=50)),
                ("image", models.ImageField(default="", upload_to="slider/")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="RoomImages",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        auto_created=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("image", models.ImageField(default="", upload_to="room/")),
                (
                    "room",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bookingapp.room",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        auto_created=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("chech_in_date", models.CharField(default="", max_length=50)),
                ("chech_out_date", models.CharField(default="", max_length=50)),
                (
                    "payment_status",
                    models.CharField(
                        choices=[("paid", "paid"), ("unpaid", "unpaid")],
                        default="unpaid",
                        max_length=50,
                    ),
                ),
                ("customer_feedback", models.TextField()),
                (
                    "customer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bookingapp.customer",
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bookingapp.room",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
