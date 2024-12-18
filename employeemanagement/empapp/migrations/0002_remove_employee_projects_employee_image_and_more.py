# Generated by Django 5.1.2 on 2024-10-28 10:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("empapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employee",
            name="projects",
        ),
        migrations.AddField(
            model_name="employee",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="employees/images/"
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="company",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="empapp.company"
            ),
        ),
    ]
