# Generated by Django 4.2.7 on 2024-02-15 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inputs", "0021_alter_savingsinputsmodel_base_savings"),
    ]

    operations = [
        migrations.AlterField(
            model_name="savingsinputsmodel",
            name="base_saved_per_mo",
            field=models.FloatField(help_text="This is some dummy help text"),
        ),
    ]
