# Generated by Django 4.2.7 on 2023-12-20 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("financial_situation", "0020_retirementinputsmodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="RatesInputsModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("base_rf_interest_per_yr", models.FloatField()),
                ("base_mkt_interest_per_yr", models.FloatField()),
                ("rf_interest_change_mos", models.FloatField()),
                ("base_inflation_per_yr", models.FloatField()),
            ],
            options={
                "verbose_name_plural": "Rates_Inputs",
            },
        ),
    ]
