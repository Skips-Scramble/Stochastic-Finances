# Generated by Django 4.2.7 on 2023-12-14 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "financial_situation",
            "0015_remove_financialinputs_payment_2_item_down_pmt_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="financialinputs",
            name="base_monthly_rent",
        ),
    ]