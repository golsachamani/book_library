# Generated by Django 4.2.7 on 2024-08-07 09:34

from django.db import migrations, models
import django.db.models.functions.text


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=225)),
                ("pages", models.PositiveIntegerField()),
                ("published_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
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
                ("name", models.CharField(max_length=225, unique=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name="genre",
            constraint=models.UniqueConstraint(
                django.db.models.functions.text.Lower("name"), name="first_name_unique"
            ),
        ),
        migrations.AddField(
            model_name="book",
            name="genre",
            field=models.ManyToManyField(related_name="books", to="books.genre"),
        ),
    ]
