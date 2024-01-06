from django.contrib.auth.models import User
from django.db import models


class GeneralInputsModel(models.Model):
    is_active = models.BooleanField(default=False)
    birthday = models.CharField(max_length=10, default="MM/DD/YYYY")
    retirement_age_yrs = models.FloatField()
    retirement_age_mos = models.FloatField()
    created_by = models.ForeignKey(
        User,
        related_name="general_inputs",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "General_Inputs"


class SavingsInputsModel(models.Model):
    is_active = models.BooleanField(default=False)
    base_savings = models.FloatField()
    base_saved_per_mo = models.FloatField()
    base_savings_per_yr_increase = models.FloatField()
    created_by = models.ForeignKey(
        User,
        related_name="savings_inputs",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Savings_Inputs"