# Generated by Django 2.1.15 on 2021-12-26 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='BusinessunitId',
            new_name='BusinessUnitId',
        ),
    ]
