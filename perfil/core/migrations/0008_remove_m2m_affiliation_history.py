# Generated by Django 2.1.1 on 2018-09-12 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("core", "0007_add_asset_history_to_politician")]

    operations = [
        migrations.RemoveField(model_name="politician", name="affiliation_history")
    ]
