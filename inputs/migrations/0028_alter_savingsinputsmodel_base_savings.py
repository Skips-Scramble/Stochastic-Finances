# Generated by Django 4.2.7 on 2024-02-17 15:53

import django.core.validators
from django.db import migrations, models
import inputs.model_validators


class Migration(migrations.Migration):

    dependencies = [
        ("inputs", "0027_alter_generalinputsmodel_retirement_age_yrs_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="savingsinputsmodel",
            name="base_savings",
            field=models.FloatField(
                validators=[
                    django.core.validators.MinValueValidator(-100000000),
                    django.core.validators.MaxValueValidator(100000000),
                    inputs.model_validators.decimal_validator,
                ]
            ),
        ),
    ]
