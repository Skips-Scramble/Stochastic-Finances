# Generated by Django 4.2.7 on 2024-01-07 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inputs", "0005_remove_paymentsinputsmodel_base_monthly_bills_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="savingsinputsmodel",
            name="base_monthly_bills",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
