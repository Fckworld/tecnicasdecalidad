# Generated by Django 4.2.1 on 2023-05-20 19:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("reservas", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="mesa",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Fecha de creación",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="mesa",
            name="updated",
            field=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición"),
        ),
        migrations.AddField(
            model_name="reserva",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Fecha de creación",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="reserva",
            name="updated",
            field=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición"),
        ),
    ]
