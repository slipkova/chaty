from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

'''
class Right(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Right", help_text="Enter a right")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

'''


class MyUser(models.Model):
    user = models.OneToOneField(User, unique=True, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        ordering = ["user"]

    def __str__(self):
        return f"{self.user.username}"


class Address(models.Model):
    town = models.CharField(max_length=40, unique=False, verbose_name="Town")
    street = models.CharField(max_length=40, unique=False, verbose_name="Street")
    number = models.IntegerField(blank=False, null=False, verbose_name="House number")
    PSC = models.IntegerField(blank=False, null=False, verbose_name="PSC")
    country = models.CharField(max_length=40, unique=False, verbose_name="Country")

    def __str__(self):
        return f"{self.street} {str(self.number)}, {self.town}, {str(self.PSC)}"


class Cottage(models.Model):
    name = models.CharField(max_length=100, unique=False, verbose_name="Cottage name", help_text="Enter a cottage name")
    description = models.TextField(blank=True, null=True, verbose_name="About cottage",
                                   help_text="Write some info about your cottage (not required)")
    spaces = models.IntegerField(blank=False, null=False, help_text="Enter a number of spaces the cottage has",
                                 verbose_name="Spaces")
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, blank=False, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class GroupMember(models.Model):
    name = models.CharField(max_length=100, unique=False, verbose_name="Name")
    is_child = models.BooleanField(default=False, verbose_name="Is this mamber a child")
    user = models.ForeignKey(MyUser, blank=False, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Reservation(models.Model):
    start_date = models.DateField(verbose_name="Start date")
    end_date = models.DateField(verbose_name="End date")
    is_private = models.BooleanField(default=True)
    user = models.ForeignKey(MyUser, blank=False, on_delete=models.CASCADE)
    members = models.ManyToManyField(GroupMember)
    cottage = models.ForeignKey(Cottage, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cottage}, {self.user}, {self.start_date} - {self.end_date}"



