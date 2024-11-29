# Generated by Django 4.2.13 on 2024-10-29 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dbms", "0002_remove_bookissued_fine_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookissued",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="dbms.libraryinventory"
            ),
        ),
    ]