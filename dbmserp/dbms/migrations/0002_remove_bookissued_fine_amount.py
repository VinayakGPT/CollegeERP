# Generated by Django 4.2.13 on 2024-10-29 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dbms", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bookissued",
            name="fine_amount",
        ),
    ]
