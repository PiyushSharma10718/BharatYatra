# Generated by Django 5.0 on 2024-03-01 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_package_package_count_package_package_life_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='package_count',
            new_name='package_left_count',
        ),
    ]
