# Generated by Django 4.2.3 on 2023-07-29 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_ticketsection_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TicketSection',
        ),
    ]