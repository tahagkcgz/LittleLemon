from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.
class Menu(models.Model):
    id = models.IntegerField(primary_key=True, validators=[MaxLengthValidator(11),MinLengthValidator(11)], auto_created=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(validators=[MaxLengthValidator(5),MinLengthValidator(1)])


class Booking(models.Model):
    id = models.IntegerField(primary_key=True, validators=[MaxLengthValidator(5),MinLengthValidator(5)], auto_created=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(validators=[MaxLengthValidator(6),MinLengthValidator(1)])
    booking_date = models.DateTimeField(auto_now=True)
