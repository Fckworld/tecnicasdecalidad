# Generated by Django 4.2.1 on 2023-05-17 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_auto_20180305_1855"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="categories",
            field=models.ManyToManyField(
                related_name="get_posts", to="blog.category", verbose_name="Categorías"
            ),
        ),
    ]