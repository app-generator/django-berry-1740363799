# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Customer(models.Model):

    #__Customer_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    account_number = models.CharField(max_length=255, null=True, blank=True)
    service_address = models.TextField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    #__Customer_FIELDS__END

    class Meta:
        verbose_name        = _("Customer")
        verbose_name_plural = _("Customer")


class Utilitydata(models.Model):

    #__Utilitydata_FIELDS__
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(blank=True, null=True, default=timezone.now)
    usage_kwh = models.IntegerField(null=True, blank=True)
    cost_rate = models.IntegerField(null=True, blank=True)

    #__Utilitydata_FIELDS__END

    class Meta:
        verbose_name        = _("Utilitydata")
        verbose_name_plural = _("Utilitydata")


class Solardata(models.Model):

    #__Solardata_FIELDS__
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    timestamp = models.IntegerField(null=True, blank=True)

    #__Solardata_FIELDS__END

    class Meta:
        verbose_name        = _("Solardata")
        verbose_name_plural = _("Solardata")


class Bill(models.Model):

    #__Bill_FIELDS__
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bill_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    billing_period_start = models.DateTimeField(blank=True, null=True, default=timezone.now)
    billing_period_end = models.DateTimeField(blank=True, null=True, default=timezone.now)
    utility_charges = models.IntegerField(null=True, blank=True)
    solar_credits = models.IntegerField(null=True, blank=True)
    total_amount_due = models.IntegerField(null=True, blank=True)
    payment_status = models.CharField(max_length=255, null=True, blank=True)
    processed = models.BooleanField()

    #__Bill_FIELDS__END

    class Meta:
        verbose_name        = _("Bill")
        verbose_name_plural = _("Bill")



#__MODELS__END
