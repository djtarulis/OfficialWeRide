# Generated by Django 5.1.6 on 2025-02-27 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_donation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Donation',
            new_name='Sponsor',
        ),
    ]
