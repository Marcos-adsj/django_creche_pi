# Generated by Django 5.0.3 on 2024-04-07 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todo",
            old_name="endreco",
            new_name="endereco",
        ),
    ]
