# Generated by Django 4.2.1 on 2023-05-22 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservas", "0004_reserva_cantidad_de_personas"),
    ]

    operations = [
        migrations.AddField(
            model_name="mesa",
            name="disponible",
            field=models.BooleanField(default=True),
        ),
    ]