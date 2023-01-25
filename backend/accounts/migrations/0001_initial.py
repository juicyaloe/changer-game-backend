# Generated by Django 4.1.5 on 2023-01-25 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("userid", models.CharField(max_length=20, unique=True)),
                ("name", models.CharField(max_length=10)),
                ("address", models.TextField()),
                ("phone", models.CharField(max_length=15, unique=True)),
                ("phone_check", models.BooleanField(default=False)),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("email_check", models.BooleanField(default=False)),
                ("date_of_birth", models.DateField()),
                ("level", models.CharField(max_length=20)),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
            ],
            options={"abstract": False,},
        ),
    ]