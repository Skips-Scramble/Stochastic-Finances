# Generated by Django 4.2.7 on 2023-12-21 01:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("financial_situation", "0021_ratesinputsmodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="generalinputsmodel",
            name="created_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="generalinputsmodel",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="general_inputs",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]