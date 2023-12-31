# Generated by Django 4.2.3 on 2023-10-22 10:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bookingapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="admin",
            name="image",
            field=models.ImageField(default="admin/dummy.png", upload_to="admin/"),
        ),
        migrations.AlterField(
            model_name="room",
            name="description",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="room",
            name="room_type",
            field=models.CharField(default="", max_length=50),
        ),
    ]
