# Generated by Django 4.2.3 on 2023-07-29 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_youtubefeed'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=50, verbose_name='Set Subtitle')),
                ('title', models.CharField(max_length=50, verbose_name='Set Title')),
                ('img', models.ImageField(upload_to='media/%Y-%m-%d', verbose_name='Upload Background Image')),
                ('days_left', models.IntegerField(blank=True, verbose_name='Set Days')),
                ('hours_left', models.IntegerField(blank=True, verbose_name='Set Hours')),
                ('minutes_left', models.IntegerField(blank=True, verbose_name='Set Minutes')),
                ('seconds_left', models.IntegerField(blank=True, verbose_name='Set Seconds')),
                ('time', models.TimeField(verbose_name='Set Time')),
            ],
            options={
                'verbose_name': 'Ticket Section',
                'verbose_name_plural': 'Ticket Section',
            },
        ),
    ]